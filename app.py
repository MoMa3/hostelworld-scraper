from src.Scraper import WebScraper
from src.FileManager import FileManager
from src.CsvManager import CSVHandler
import datetime

# Example usage
if __name__ == "__main__":
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

    data_file_path = "data"
    list_cities = [
        {"London": "england"},
        {"Amsterdam": "netherlands"},
        {"Barcelona": "spain"},
        {"Paris": "france"},
        {"Berlin": "germany"},
    ]
    for indx, city_dict in enumerate(list_cities):
        print(f"{indx+1}: {list(city_dict.keys())[0]}")
    user_input = input("Pick a city using the number associated with it: ")
    index = int(user_input)-1
    if 0 <= index < len(list_cities):
        city_country_dict = list_cities[index]
        city = list(city_country_dict.keys())[0]  # City name (key of the dictionary)
        country = list(city_country_dict.values())[0]  # Country name (value of the dictionary)
        print(f"City: {city}")
    else:
        print("Index out of range")
        
    url = f"https://www.hostelworld.com/st/hostels/europe/{country}/{city}"
    print(url)

    scraper = WebScraper(url)
    data = scraper.scrape()

    csv_handler = CSVHandler(f"data/{formatted_datetime}.csv")
    csv_handler.write_csv(data)
