import requests
import argparse


class WebScraper:
    def __init__(self, url, headers, request_method):
        self.url = url
        self.headers = headers
        self.request_method = request_method.upper()
    
    def scrape(self):
        try:
            response = requests.request(method=self.request_method, url=self.url, headers=self.headers)
            if response.status_code == 200:
                print("Response: ", response.text)
                print("Response code: ", response.status_code)
            else:
                print("Wrong Response: ", response.text)
                print("Wrong Response code: ", response.status_code)
        except Exception as e:
            print("Error while requesting: ", e)
            exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Web Scraper Command Line Tool')
    parser.add_argument('-u', '--url', type=str, required=True, help='The URL to scrape')
    parser.add_argument('-m', '--method', type=str, default='GET', choices=['GET', 'POST'],
                        help='HTTP request method (default: GET)')
    parser.add_argument('-H', '--headers', type=str, nargs='*', default=[],
                        help='Headers for the request in key=value format (e.g., key1=value1 key2=value2)')
    
    args = parser.parse_args()
    
    # Parse headers from key=value format into a dictionary
    headers_dict = {}
    for header in args.headers:
        if '=' in header:
            key, value = header.split('=', 1)
            headers_dict[key.strip()] = value.strip()
    
    # Initialize the scraper object
    scraper = WebScraper(url=args.url, headers=headers_dict, request_method=args.method)
    
    # Perform the scraping
    scraper.scrape()
