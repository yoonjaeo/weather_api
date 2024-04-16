from datetime import datetime, timedelta
from pytz import timezone
from time import strftime, localtime
from data_fetcher import *
from logger import *

class DataProcessor:
    def __init__(self) -> None:
        pass
    def process_data(self, data):
        if data == -1:
            return "No!!!"
        else:
            time_now = datetime.now(timezone('GMT')) + timedelta(hours = (data['timezone'])/3600)
            processed_data = (data['name'], data['main']['temp'], time_now.strftime('%Y-%m-%d %H:%M:%S'))
            return processed_data



def main():
    api_key = "api_key"
    L = Logger()
    fethcer = DataFetcher("Busan", api_key)
    data = fethcer.fetch_weather(L)
    processor = DataProcessor()
    print(processor.process_data(data))

if __name__ == "__main__":
    main()