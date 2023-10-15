from src.Scraper import WebScraper
from src.FileManager import FileManager
from src.CsvManager import CSVHandler
import datetime

# Example usage
if __name__ == "__main__":
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d_%H-%M-%S')


    data_file_path = "data"
    url = "https://www.hostelworld.com/st/hostels/europe/england/london"
    list_cities = [
        {"england": "london"},
        {"netherlands": "amsterdam"},
        {"spain": "barcelona"},
        {"france": "paris"},
        {"germany": "berlin"},
    ]
    scraper = WebScraper(url)
    data = scraper.scrape()
    csv_handler = CSVHandler(f'data/{formatted_datetime}.csv')
    csv_handler.write_csv(data)

