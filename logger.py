from data_fetcher import *
from data_processor import *
import pandas as pd
from datetime import datetime
import os

"""
받아온 튜플 형태의 정보들을 csv로 변경해주고 싶음.
원래 csv가 있다면, append 해주기
"""


class Logger:
    def __init__(self ):
        self.df = pd.DataFrame(columns= ['city', 'temperature', 'time'])
        self.log_txt = []

    def logging_txt(self, text):
        self.log_txt.append(f"{datetime.now()} : {text}")

    def logging_data(self, data):
        self.df.loc[len(self.df)] = list(data)
        self.log_txt.append(f"{datetime.now()} : {data[0]}의 날씨가 기록되었습니다.")

    def save_logg_data(self,csv_name = 'weather_log'):
        try:    
            self.csv_name = csv_name
            read_df = pd.read_csv(f"./data/{csv_name}.csv", encoding='utf-8')
            result_df = pd.concat([read_df, self.df])
            result_df.to_csv(f"./data/{csv_name}.csv",encoding='utf-8', index=False)
        except:
            os.mkdir("data")
            self.df.to_csv(f"./data/{csv_name}.csv",encoding='utf-8', index=False)

    def save_logg_txt(self):
        with open("./data/logger.txt","a") as f:
            f.write(f"{datetime.now()} : 날씨 정보들이 {self.csv_name}.csv파일에 저장되었습니다.\n")
            for txt in self.log_txt:
                f.write(txt+"\n")

    def logger_reset(self):
        self.df = pd.DataFrame(columns= ['city', 'temperature', 'time'])
        self.log_txt = []

        

def main():
    api_key = "api_key"
    L = Logger()
    fethcer = DataFetcher("Busan", api_key)
    for i in range(10):
        data = fethcer.fetch_weather(L)
        processor = DataProcessor()
        data = processor.process_data(data)
        L.logging_data(data)
    L.save_logg()

if __name__ == "__main__":
    main()