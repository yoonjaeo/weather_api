import requests
from logger import *


class DataFetcher:

    def __init__(self, city, api_key):
        self.city = city
        self.url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={api_key}&units=metric"
        self.response = requests.get(self.url)
    
    def fetch_weather(self, logger):
        try : 
            if self.response.status_code == 200:
                self.data = self.response.json()
                logger.logging_txt("api를 정상적으로 불러왔습니다.")
                return self.data
        except:
            logger.logging_txt("api를 정상적으로 불러오지 못했습니다.")
            return -1
        
def main():
    api_key = "api_key"
    fethcer = DataFetcher("Busan", api_key)
    L =Logger()
    print(fethcer.fetch_weather(L))
    print(fethcer.city)

if __name__ == "__main__":
    main()

    