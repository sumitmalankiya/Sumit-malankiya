WebScraper is a simple Python-based command-line tool to perform HTTP requests and retrieve content from a specified URL. It supports GET and POST requests and allows the user to pass custom headers.

pip install -r requirements.txt

python scraper.py -u https://quotes.toscrape.com/ -m GET -H upgrade-insecure-requests=1

-u or --url : The URL to scrape (required).

-m or --method : HTTP request method (default: GET). Options: GET, POST.

-H or --headers : Optional headers in key=value format (e.g., key1=value1 key2=value2).
