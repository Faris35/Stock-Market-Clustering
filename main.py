import joblib
from pydantic import BaseModel
from fastapi import FastAPI

from sklearn.metrics import pairwise_distances_argmin_min

# Load the pre-trained model and scaler
model = joblib.load('Stock_clustering.joblib')
scaler = joblib.load('scaler.joblib')

# Define the input schema
class InputFeatures(BaseModel):
    market_value_per_share: float
    ev_to_mv_ratio: float
    dividend_per_share: float
    sector: int

# Preprocessing function
def preprocessing(input_features: InputFeatures):
    dict_f = {
        'market_value_per_share': input_features.market_value_per_share,
        'ev_to_mv_ratio': input_features.ev_to_mv_ratio,
        'dividend_per_share': input_features.dividend_per_share,
        'sector': input_features.sector,
    }
    features_list = [dict_f[key] for key in sorted(dict_f)]  # Ensure consistent order
    scaled_features = scaler.transform([list(dict_f.values())])
    return scaled_features

# Initialize FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Tuwaiq Academy"}

@app.get("/items/")
def create_item(item: dict):
    return {"item": item}

@app.post("/predict")
async def predict(input_features: InputFeatures):
    try:
        # Preprocess the input
        data = preprocessing(input_features)

        # Predict the cluster
        cluster_label = model.predict(data)[0]
        return {"pred": int(cluster_label)}
    except Exception as e:
        return {"error": str(e)}