# booking_scraper

I made this python 3.+ to prove that is possible to scrape complex websites with tons of data like booking.com, to study the Beautifulsoup module and to have fun programming.

For this project i started from the @ZoranPandovski [BookingScraper](https://github.com/ZoranPandovski/BookingScraper)

# How to install

`$ pip install -r requirements.txt`

# How to use 

launch the script with :

`$ python3 bkscraper.py --city "New York" --limit 0 `

### Usable Parameters

| Parameter  | Description | Mandatory |
| ------------- | ------------- |------------- |
| `--people`  | Used to specify the number of people to the booking request.  | No |
| `--country`  | Used to specify the country for the scraping request.  | Yes if `--city` is not used |
| `--city`  | Used to specify the city for the scraping request.  | Yes if `--country` is not used |
| `--datein`  | Used to specifiy checkin day. If not setted the field will automatically be setted to today  | No |
| `--dateout`  | Used to specifiy checkout day. If not setted the field will automatically be setted to tomorrow  | No |
| `-o --outdir`  | Used to specify the output dir and filename. If not setted the field the script will automatically set the same script directory with the following nomenclature: **CountryCity_date_time.json** | No |
| `-d --detail`  | Used it if you want more details in the output. It will take time to produce the output (not reccomended for long analysis or `--limit` is not setted to 0)  | No |
| `-v --verbose`  | Used it if you want more logs during the process. | No |
| `-l --limit`  | Used to specify the number of page to fetch. If the number will be greater than the effective number of pages retrieved from the search it will be ignored like if the input number will be < 0. If will be 0 the process will fetch only the first page and if the number will be less than the effective number of page retrieved it will process only those pages | No |

### Example

`$ python3 bkscraper.py --city "New York" --limit 0 -d -v -o ./test.json`

## ToDo List

- [x] Scrape the "all facility checklist" offered in the structure divided by groups like the website in the detail view

- [ ] Apply filters in the search

- [ ] code review to make it lighter

# Disclaimer

**Strictly for educational purposes only; If you use it other than educational or learning purposes, I will not be responsible for any damages caused by improper use of this repo/project.**


You are not allowed to copy and paste content from Booking.com on to your own or third party pages (including social media pages such as Facebook, Twitter, Instagram etc.).

This applies to all types of content that can be found on Booking.com pages, including but not limited to hotel descriptions, reviews, hotel and room photos, hotel facility information, and prices. Moreover, this restriction also applies to content from Booking.com partner hotel websites and Booking Holdings Group company brands: such as Agoda, Priceline, Kayak, OpenTable, Rentalcars.

Clause 4.1.5 from Booking.com Affiliate Agreement: The Affiliate shall not programmatically evaluate and extract information (including guest reviews) from any part of the Booking.com Website (e.g. screen scrape).
