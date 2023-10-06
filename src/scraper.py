import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.driver = None

    def scrape(self):
        if self.driver is None:
                raise Exception("Selenium driver not initialized. Call setup() method first.")

        try:
            # Send an HTTP GET request to the URL
            response = requests.get(self.url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the HTML content of the page
                soup = BeautifulSoup(response.text, "html.parser")

                # Extract and print the title of the webpage
                title = soup.title.text
                print(f"Title: {title}")

                # Extract and print all the links on the page
                links = soup.find_all("a")
                for link in links:
                    print("Link:", link.get("href"))

            else:
                print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

        except Exception as e:
            print(f"An error occurred: {e}")

            
# Example usage
if __name__ == "__main__":
    url = "https://google.com"
    scraper = WebScraper(url)
    scraper.scrape()
