import argparse
import requests
from bs4 import BeautifulSoup
import datetime
import sys
import json
from .core.ThreadScraper import ThreadScraper
from .core import core

session = requests.Session()
today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(1)

is_verbose = False

REQUEST_HEADER = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"}
BOOKING_PREFIX = 'https://www.booking.com'
ROW_PER_OFFSET = 25


def get_max_offset(soup):
    all_offset = []
    if soup.find_all('li', {'class': 'sr_pagination_item'}) is not None:
        all_offset = soup.find_all('li', {'class': 'sr_pagination_item'})[-1].get_text().splitlines()[-1]

    return all_offset


def create_url(people, country, city, datein, dateout, offset):

    url = "https://www.booking.com/searchresults.it.html?checkin_month={in_month}" \
        "&checkin_monthday={in_day}&checkin_year={in_year}&checkout_month={out_month}" \
        "&checkout_monthday={out_day}&checkout_year={out_year}&group_adults={people}" \
        "&group_children=0&order=price&ss={city}%2C%20{country}&offset={offset}"\
        .format(in_month=str(datein.month),
                in_day=str(datein.day),
                in_year=str(datein.year),
                out_month=str(dateout.month),
                out_day=str(dateout.day),
                out_year=str(dateout.year),
                people=people,
                city=city,
                country=country,
                offset=offset)

    return url


def process_data(people, country, city, datein, dateout, is_detail, limit):
    offset = 0
    threads = []
    max_offset = 0

    starting_url = create_url(people, country, city, datein, dateout, offset)
    # print(starting_url)
    if is_verbose:
        print("[~] Url created:" + "\n" + "\t" + starting_url)

    response = session.get(starting_url, headers=REQUEST_HEADER)
    soup = BeautifulSoup(response.text, "lxml")

    if limit < 0:
        max_offset = int(get_max_offset(soup))
    elif limit > 0:
        max_off = int(get_max_offset(soup))
        if limit > max_off:
            max_offset = max_off
        else:
            max_offset = limit

    if is_verbose:
        print("[~] Page to fetch: " + str(max_offset))

    if is_verbose:
        print("[~] Initializing Threads...")

    if max_offset > 0:
        for i in range(int(max_offset)):
            offset += 25
            t = ThreadScraper(session, offset, people, country, city,
                              datein, dateout, is_detail, parsing_data)
            threads.append(t)
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    else:
        t = ThreadScraper(session, offset, people, country, city, datein, dateout, is_detail, parsing_data)
        threads.append(t)
        t.start()
        t.join()

    return ThreadScraper.process_result


def parsing_data(session, people, country, city, datein, dateout, offset, is_detail):

    result = []
    data_url = create_url(people, country, city, datein, dateout, offset)

    response = session.get(data_url, headers=REQUEST_HEADER)
    soup = BeautifulSoup(response.text, "lxml")

    hotels = soup.select("#hotellist_inner div.sr_item.sr_item_new")

    # print(len(soup.select_one("li.bui-pagination__pages")))
    if(is_verbose):
        print("[~] Start fetching structures")
        if(is_detail):
            print("[~] It will take a while with details")

    for hotel in hotels:
        hotel_info = {}

        hotel_info['name'] = core.get_hotel_name(hotel)

        hotel_info['score'] = core.get_hotel_score(hotel)

        hotel_info['price'] = core.get_hotel_price(hotel)

        hotel_info['link'] = core.get_hotel_detail_link(hotel)

        if hotel_info['link'] is not None:
            
            if is_detail:
                details = {}
                detail_page_response = session.get(BOOKING_PREFIX + hotel_info['link'], headers=REQUEST_HEADER)
                soup_detail = BeautifulSoup(detail_page_response.text, "lxml")

                details['latitude'] = core.get_coordinates(soup_detail)[0]

                details['longitude'] = core.get_coordinates(soup_detail)[1]

                details['important_facilities'] = core.get_important_facilites(soup_detail)

                details['neighborhood_structures'] = core.get_neighborhood_structures(soup_detail)

                details['services_offered'] = core.get_services_offered(soup_detail)

                hotel_info['details'] = details

        hotel_info['thumbnail_image'] = core.get_thumbnail_image(hotel)

        result.append(hotel_info)

    if is_verbose:
        print("[~] Retrieving fetched structures")

    session.close()

    return result


def get_result(**kwargs):
    result = []
    today = datetime.datetime.now()
    tomorrow = today + datetime.timedelta(1)

    people = kwargs.get('people', 1)
    country = kwargs.get('country', None)
    city = kwargs.get('city', None)
    datein = kwargs.get('datein', today)
    dateout = kwargs.get('datein', tomorrow)
    is_detail = kwargs.get('detail', False)
    limit = kwargs.get('limit', -1)

    if city == None and country == None:
        raise Exception('set the \"city\" or \"country\" param at least')


    if isinstance(datein, str) or isinstance(dateout, str):
        datein = datetime.datetime.strptime(datein, "%Y-%m-%d")
        dateout = datetime.datetime.strptime(dateout, "%Y-%m-%d")

    result = process_data(people, country, city, datein, dateout, is_detail, limit)

    return result


def retrieve_data(people, country, city, datein, dateout, outdir, is_detail, limit):

    result = []
    if isinstance(datein, str) or isinstance(dateout, str):
        datein = datetime.datetime.strptime(datein, "%Y-%m-%d")
        dateout = datetime.datetime.strptime(dateout, "%Y-%m-%d")

    result = process_data(people, country, city, datein, dateout, is_detail, limit)

    if outdir == "":
        outdir = ("./" + country + city + "_" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ".json").replace(" ", "_").replace(":", "_")

    if is_verbose:
        print("[~] Saving under the path: " + outdir)

    with open(outdir, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
        f.close()

    print("[~] Process finished!")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--people",
                        help='Used to specify the number of people to the booking request.',
                        default=1,
                        type=int)
    parser.add_argument("--country",
                        help='Used to specify the country to the booking request.',
                        default='')
    parser.add_argument("--city",
                        help='Used to specify the city to the booking request.',
                        default='')
    parser.add_argument("--datein",
                        help='Used to specifiy checkin day.',
                        default=today)
    parser.add_argument("--dateout",
                        help='Used to specifiy checkout day.',
                        default=tomorrow)
    parser.add_argument("-o", "--outdir",
                        help='Used to specify the output dir and filename',
                        default="")
    parser.add_argument("-d", '--detail',
                        default=False,
                        help='Use it if you want more details in the output',
                        action='store_true')
    parser.add_argument("-v", '--verbose',
                        default=False,
                        help='Use it if you want more logs during the process',
                        action='store_true')
    parser.add_argument("-l", '--limit',
                        default=-1,
                        type=int,
                        help='Used to specify the number of page to fetch')

    args = parser.parse_args()
    if args.country == '' and args.city == '':
        parser.error('No action performed, use the --city or --country param at least')
    if args.verbose:
        is_verbose = True

    retrieve_data(args.people, args.country, args.city, args.datein, args.dateout, args.outdir, args.detail, args.limit)
