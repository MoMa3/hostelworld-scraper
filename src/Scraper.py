import requests
from bs4 import BeautifulSoup
from utils.helpers import extract_number, create_object


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.text = None
        self.current_page = 1
        self.entries_data = []

    def get_page(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.text = response.text
            else:
                print(
                    f"Failed to retrieve the webpage. Status code: {response.status_code}"
                )
        except Exception as e:
            print(f"An error occurred: {e}")

    def extract_data_from_listing_cards(self,
        listing_card, class_name, tag="span", inner_class=None
    ):
        try:
            element = listing_card.find("div", {"class": class_name})
            if element is None:
                return "N/A"
            else:
                if inner_class:
                    element = element.find(tag, {"class": inner_class})
                else:
                    element = element.find(tag)
                return element.text if element else None

        except Exception as e:
            print(f"Unable to extract tag:{tag} with class_name {class_name}, inner_class: {inner_class}, {e}")

    def extract_total_reviews(self,listing_card):
        try:
            property_rating = listing_card.find("div", {"class": "property-rating"})
            if property_rating:
                left_margin = property_rating.find("span", {"class": "left-margin"})
                if left_margin:
                    review_text = left_margin.text
                    total_reviews = int("".join(filter(str.isdigit, review_text)))
                    return total_reviews
            return None
        except Exception as e:
            print(f"Unable to extract total reviews, {e}")

    def does_next_page_exist(self):
        # Parse the HTML content of the page
        soup = BeautifulSoup(self.text, "html.parser")
        next_page_button_tag = soup.find("a", {"class": "nav-right"})
        return next_page_button_tag is not None

    def scrape(self):
        try:
            # Check if the request was successful (status code 200)
            self.get_page()
            # Parse the HTML content of the page
            soup = BeautifulSoup(self.text, "html.parser")
            # Extract and print all the links on the page
            listing_cards = soup.find_all("a", {"class": "property-listing-card"})
            for listing_card in listing_cards:
                url = listing_card.get("href")

                name = self.extract_data_from_listing_cards(
                    listing_card=listing_card, class_name="property-name"
                )
                description = self.extract_data_from_listing_cards(
                    listing_card=listing_card, class_name="property-description"
                )
                star_rating = self.extract_data_from_listing_cards(
                    listing_card=listing_card, class_name="property-rating", tag="span", inner_class="number"
                )
                keyword_rating = self.extract_data_from_listing_cards(
                    listing_card=listing_card, class_name="property-rating", tag="span", inner_class="keyword"
                )

                total_reviews = self.extract_total_reviews(listing_card)
                km_from_city_center = extract_number(
                    listing_card.find("span", {"class": "distance-description"}).text
                )

                # Inside your for loop for listing cards
                price_elements = listing_card.find(
                    "div", {"class": "property-accommodation-prices"}
                )
                # Initialize a dictionary to store labels and prices for the current listing
                prices_dict = {}
                for price_div in price_elements.find_all(
                    "div", {"class": "property-accommodation-price"}
                ):
                    label_element = price_div.find(
                        "div", {"class": "accommodation-label"}
                    )
                    price_element = price_div.find("strong", {"class": "current"})

                    if label_element and price_element:
                        label = label_element.text.strip()
                        price = price_element.text.strip()

                        prices_dict["currency"] = price[0:1]
                        prices_dict[label] = float(price[1:])

                self.entries_data.append(
                    create_object(
                        url=url,
                        name=name,
                        description=description,
                        star_rating=star_rating,
                        keyword_rating=keyword_rating,
                        total_reviews=total_reviews,
                        km_from_city_center=km_from_city_center,
                        currency=prices_dict["currency"],
                        min_dorm_price=prices_dict["Dorms From"]
                        if prices_dict.get("Dorms From") is not None
                        else "N/A",
                        min_privates_price=prices_dict["Privates From"]
                        if prices_dict.get("Privates From") is not None
                        else "N/A",
                    )
                )

            if self.does_next_page_exist():
                if self.current_page != 1:
                    self.url = self.url[:-4]
                self.url = self.url + f"/p/{self.current_page + 1}"
                print(self.url)
                self.current_page = self.current_page + 1
                self.scrape()

            return self.entries_data
        except Exception as e:
            print(f"An error occurred: Unable to scrape {e}")