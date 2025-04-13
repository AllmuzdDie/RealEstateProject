import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

with open(r'model.pkl', 'rb') as f:
    model = pickle.load(f)
    
@app.route('/')
def index():
    return "Test message. The server is running"


@app.route('/predict', methods=['POST'])
def predict():
    features = request.json
    df = pd.DataFrame(data=features.values(), index=features.keys()).T
    X = df.drop(['target'], axis=1)
    y = df['target'][0]
    prediction = round(np.exp(model.predict(X))[0], 0)
    result = f"Модель предсказала стоимость дома в {prediction} при реальной стоимости {round(y, 0)}"
            
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)