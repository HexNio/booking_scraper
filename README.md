# booking_scraper
[![PyPI version shields.io](https://img.shields.io/pypi/v/booking-scraper.svg)](https://pypi.org/project/booking-scraper/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)


I made this python 3.+ to prove that is possible to scrape complex websites with tons of data like booking.com, to study the Beautifulsoup module and to have fun programming.

For this project i started from the @ZoranPandovski [BookingScraper](https://github.com/ZoranPandovski/BookingScraper)

# How to install

`$ pip install booking-scraper`

# How to use 

## From bash

launch the script with :

`$ python3 -m booking_scraper.bkscraper --city "New York" --limit 0 `

#### Usable Parameters

| Parameter  | Description | Mandatory |
| ------------- | ------------- |------------- |
| `--people`  | Used to specify the number of people to the booking request. The default value is 1 | No |
| `--country`  | Used to specify the country for the scraping request.  | Yes if `--city` is not used |
| `--city`  | Used to specify the city for the scraping request.  | Yes if `--country` is not used |
| `--datein`  | Used to specifiy checkin day. If not setted the field will automatically be setted to today  | No |
| `--dateout`  | Used to specifiy checkout day. If not setted the field will automatically be setted to tomorrow  | No |
| `-o --outdir`  | Used to specify the output dir and filename. If not setted the field the script will automatically set the same execution script directory with the following nomenclature: **CountryCity_date_time.json** | No |
| `-d --detail`  | Used it if you want more details in the output. It will take time to produce the output (not reccomended for long analysis or `--limit` is not setted to 0)  | No |
| `-v --verbose`  | Used it if you want more logs during the process. | No |
| `-l --limit`  | Used to specify the number of page to fetch. If the number will be greater than the effective number of pages retrieved from the search it will be ignored like if the input number will be < 0. If will be 0 the process will fetch all the pages and if the number will be less than the effective number of page retrieved it will process only those pages | No |

### Bash Example

`$ python3 -m booking_scraper.bkscraper --city "New York" --limit 0 -d -v -o ./test.json`

## From python Code
you can import the module with:

`from booking_scraper import bkscraper`

to use it the only available method is:

`bkscraper.get_result(**kwargs)`

it use the same logic as the bash execution mode and the available params are:

| Parameter  | Description | Mandatory |
| ------------- | ------------- |------------- |
| `people`  | Used to specify the number of people to the booking request. The default value is 1 | No |
| `country`  | Used to specify the country for the scraping request.  | Yes if `city` is not used |
| `city`  | Used to specify the city for the scraping request.  | Yes if `country` is not used |
| `datein`  | Used to specifiy checkin day. If not setted the field will automatically be setted to today  | No |
| `dateout`  | Used to specifiy checkout day. If not setted the field will automatically be setted to tomorrow  | No |
| `detail`  | Used it if you want more details in the output. It will take time to produce the output (not reccomended for long analysis or `limit` is not setted to 0)  | No |
| `limit`  | Used to specify the number of page to fetch. If the number will be greater than the effective number of pages retrieved from the search it will be ignored like if the input number will be < 0. If will be 0 the process will fetch all the pages and if the number will be less than the effective number of page retrieved it will process only those pages | No |

If either city or country param is not setted the script will rise an Exception. 

### Code Example
```python
import json
from booking_scraper import bkscraper

#It fetches only the first page for New York city with details
result = bkscraper.get_result(city="New York", limit=1, detail=True)


with open("output.json", 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
    f.close()
```
## Public

This script was first featured on Reddit at /r/learnpython - [see here](https://www.reddit.com/r/learnpython/comments/g60qui/my_first_python_project/) for the thread. I’ve finally decided to release the script.

## ToDo List

- [x] Scrape the "all facility checklist" offered in the structure divided by groups like the website in the detail view

- [x] Make the script as module

- [ ] Apply filters in the search

- [ ] code review to make it lighter

# Disclaimer

**This project is for educational and research purposes only. Any actions and/or activities related to the material contained on this GitHub Repository is solely your responsibility. The misuse of the information in this GitHub Repository can result in criminal charges brought against the persons in question. The author will not be held responsible in the event any criminal charges be brought against any individuals misusing the information in this GitHub Repository to break the law.**


You are not allowed to copy and paste content from Booking.com on to your own or third party pages (including social media pages such as Facebook, Twitter, Instagram etc.).

This applies to all types of content that can be found on Booking.com pages, including but not limited to hotel descriptions, reviews, hotel and room photos, hotel facility information, and prices. Moreover, this restriction also applies to content from Booking.com partner hotel websites and Booking Holdings Group company brands: such as Agoda, Priceline, Kayak, OpenTable, Rentalcars.

Clause 4.1.5 from Booking.com Affiliate Agreement: The Affiliate shall not programmatically evaluate and extract information (including guest reviews) from any part of the Booking.com Website (e.g. screen scrape).
