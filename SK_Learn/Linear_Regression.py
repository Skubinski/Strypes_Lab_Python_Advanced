import numpy as np
import requests
from sklearn.linear_model import LinearRegression

API_KEY = 'ce9ed943f4f24a49a29105348250108'

city = 'London'

url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=14"
response = requests.get(url)

data = response.json()

days = data['forecast']['forecastday']

y = [day['day']['avgtemp_c'] for day in days]
x = list(range(1, len(y) + 1))

X = np.array(x).reshape(-1, 1)
Y = np.array(y)

model = LinearRegression()
model.fit(X, Y)

future_days = np.array([15, 16, 17]).reshape(-1, 1)

for i in range(len(future_days)):
    np.append(future_days, i)
    predictions = model.predict(future_days)

    print(f"Day {future_days[i][0]}: {predictions[i]:.2f} C")


