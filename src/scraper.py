import requests
from bs4 import BeautifulSoup
import json
from utils.helpers import extract_number, create_object


class WebScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        try:
            # Send an HTTP GET request to the URL
            response = requests.get(self.url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                entries_data = []
                # Parse the HTML content of the page
                soup = BeautifulSoup(response.text, "html.parser")
                # Extract and print all the links on the page
                listing_cards = soup.find_all("a", {"class": "property-card-container"})
                for listing_card in listing_cards:
                    url = listing_card.get("href")
                    name = (
                        listing_card.find("div", {"class": "property-name"})
                        .find("span")
                        .text
                    )
                    description = (
                        listing_card.find("div", {"class": "property-description"})
                        .find("span")
                        .text
                    )
                    star_rating = (
                        listing_card.find("div", {"class": "property-rating"})
                        .find("span", {"class": "number"})
                        .text
                    )
                    keyword_rating = (
                        listing_card.find("div", {"class": "property-rating"})
                        .find("span", {"class": "keyword"})
                        .text
                    )
                    total_reviews = int(
                        "".join(
                            filter(
                                str.isdigit,
                                listing_card.find("div", {"class": "property-rating"})
                                .find("span", {"class": "left-margin"})
                                .text,
                            )
                        )
                    )
                    km_from_city_center = extract_number(
                        listing_card.find(
                            "span", {"class": "distance-description"}
                        ).text
                    )

                    # Inside your for loop for listing cards
                    price_elements = listing_card.find(
                        "div", {"class": "property-accommodation-prices"}
                    )
                    # Initialize a dictionary to store labels and prices for the current listing
                    prices_dict = {}

                    for price_div in price_elements.find_all(
                        "div", class_="property-accommodation-price"
                    ):
                        label_element = price_div.find(
                            "div", class_="accommodation-label"
                        )
                        price_element = price_div.find("strong", class_="current")

                        if label_element and price_element:
                            label = label_element.text.strip()
                            price = price_element.text.strip()

                            prices_dict["currency"] = price[0:1]
                            prices_dict[label] = float(price[1:])

                    entries_data.append(
                        create_object(
                            url=url,
                            name=name,
                            description=description,
                            star_rating=star_rating,
                            keyword_rating=keyword_rating,
                            total_reviews=total_reviews,
                            km_from_city_center=km_from_city_center,
                            currency=prices_dict["currency"],
                            min_dorm_price = prices_dict["Dorms From"] if prices_dict.get("Dorms From") is not None else "N/A",
                            min_privates_price = prices_dict["Privates From"] if prices_dict.get("Privates From") is not None else "N/A"
                        )
                    )
                print(json.dumps(entries_data, indent=1,sort_keys=True))
            else:
                print(
                    f"Failed to retrieve the webpage. Status code: {response.status_code}"
                )

        except Exception as e:
            print(f"An error occurred: {e}")
