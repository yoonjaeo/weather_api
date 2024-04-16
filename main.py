from data_fetcher import *
from data_processor import *
import time
from logger import * 
from Visualizer import *

def main():
    api_key = "api_key"

    L = Logger()
    V = Visualizer()

    city_list = ['Busan', 'Seoul','London']
    i = 0
    while True:
        i += 1
        
        for city in city_list:
            fethcer = DataFetcher(city, api_key)
            data = fethcer.fetch_weather(L)
            processor = DataProcessor()
            data = processor.process_data(data)
            L.logging_data(data)
        
        if i % 10 == 0:
            L.save_logg_data()
            for city in city_list:
                V.plot_data(city, L,f"{city}.png")
            L.save_logg_txt()
            L.logger_reset()

        time.sleep(600)

        if i == 20:
            break


if __name__ == "__main__":
    main()