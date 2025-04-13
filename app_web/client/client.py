import requests
import json
import pandas as pd

if __name__ == '__main__':
    # выполняем POST-запрос на сервер по эндпоинту predict с параметром json
    for i in range(0, 10):
        df = pd.read_csv('data/test_df.csv', usecols=lambda col: col!='Unnamed: 0').loc[i].to_json()
        r = requests.post('http://localhost:5000/predict', json=json.loads(df))
        
        if r.status_code == 200:
            # если запрос выполнен успешно (код обработки=200),
            # выводим результат на экран
            print(r.json())
        else:
            # если запрос завершён с кодом, отличным от 200,
            # выводим содержимое ответа
            print(r.text)

