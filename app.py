from src.scraper import WebScraper


# Example usage
if __name__ == "__main__":
    url = "https://www.hostelworld.com/st/hostels/europe/england/london"
    list_cities = [
        {"england":"london"},
        {"netherlands":"amsterdam"},
        {"spain":"barcelona"},
        {"france":"paris"},
        {"germany":"berlin"}
        ]
    scraper = WebScraper(url)
    scraper.scrape()
