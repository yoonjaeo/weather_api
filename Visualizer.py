import plotly.graph_objects as go
import pandas as pd
from data_fetcher import *
from data_processor import *
from logger import * 

class Visualizer:

  def __init__(self) -> None:
    pass

  
  def plot_data(self, city,L, output_file='./data/output.png',  csv_name = "weather_log"):

    try:
      self.data = pd.read_csv(f"./data/{csv_name}.csv", encoding='utf-8')
      L.logging_txt("시각화를 위해 csv 파일을 열었습니다.")
    except:
      L.logging_txt("csv파일을 실행하지 못했습니다.")

    # 원하는 city만 추출
    data = self.data[self.data['city'] == city]

    # 'time'과 'temperature' 열 데이터 추출
    if len(data) > 10:
      data = data.tail(10)
    
    times = data['time'].tolist()  # 'time' 열을 리스트로 변환
    temperatures = data['temperature'].tolist()  # 'temperature' 열을 리스트로 변환

    # 그래프 객체 생성
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=times, y=temperatures, mode='lines+markers', name='Temperature'))

    # 그래프 레이아웃 업데이트
    fig.update_layout(title=f"{output_file.split('.')[0]} Temperature Over Time",
                      xaxis_title='Time',
                      yaxis_title='Temperature (°C)',
                      template='plotly_dark')

    # 이미지 파일로 저장
    fig.write_image(f"./data/{output_file}")
    L.logging_txt(f"Graph saved to {output_file}")
    

def main():
    api_key = "053de8cde01f3c2907748c88ac557933"
    L = Logger()
    city_list = ['Busan', 'Seoul','London']
    for i in range(2):
        for city in city_list:
          fethcer = DataFetcher(city, api_key)
          data = fethcer.fetch_weather(L)
          processor = DataProcessor()
          data = processor.process_data(data)
          L.logging_data(data)
    L.save_logg_data()
    V = Visualizer()
    for city in city_list:
      V.plot_data(city, L,f"{city}.png")
    L.save_logg_txt()

if __name__ == "__main__":
    main()