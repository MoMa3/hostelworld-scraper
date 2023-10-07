import requests
from bs4 import BeautifulSoup

from utils.helpers import extract_number

class WebScraper:
    def __init__(self, url):
        self.url = url
    def scrape(self):

        try:
            # Send an HTTP GET request to the URL
            response = requests.get(self.url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the HTML content of the page
                soup = BeautifulSoup(response.text, "html.parser")
                # Extract and print all the links on the page
                listing_cards = soup.find_all("a",{"class":"property-card-container"})
                for listing_card in listing_cards:
                    url = listing_card.get("href")
                    name = listing_card.find("div", {"class":"property-name"}).find("span").text
                    description = listing_card.find("div", {"class":"property-description"}).find("span").text
                    star_rating = listing_card.find("div", {"class":"property-rating"}).find("span", {"class":"number"}).text
                    keyword_rating = listing_card.find("div", {"class":"property-rating"}).find("span", {"class":"keyword"}).text
                    total_reviews = int(''.join(
                        filter(
                            str.isdigit, 
                            listing_card.find("div", {"class":"property-rating"}).find("span", {"class":"left-margin"}).text)))
                    km_from_city_center = extract_number(listing_card.find("span", {"class":"distance-description"}).text)
                    price_elements = listing_card.find("div", {"class":"property-accommodation-prices"})
                    # Initialize a dictionary to store labels and prices
                    prices = {}

                    for price_div in soup.find_all("div", class_="property-accommodation-price"):
                        label_element = price_div.find("div", class_="accommodation-label")
                        price_element = price_div.find("strong", class_="current")

                        if label_element and price_element:
                            label = label_element.text.strip()
                            price = price_element.text.strip()
                            prices[label] = price
                    
                    print(prices)
            else:
                print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

        except Exception as e:
            print(f"An error occurred: {e}")
