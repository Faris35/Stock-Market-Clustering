url ='https://stock-market-clustering.onrender.com/predict'
data = {
    "market_value_per_share": 100,
    "ev_to_mv_ratio": 2,
    "dividend_per_share": 1,
    "sector": 1
}
response = requests.post(url, json=data)
print(response.json())