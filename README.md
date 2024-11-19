# Stock Clustering Prediction App

## Overview
This is a Streamlit-based web app that predicts which cluster a stock belongs to based on its features such as market value, EV to MV ratio, dividend per share, and sector. The clustering model has been trained to categorize stocks into three distinct clusters with the following characteristics:

- **Cluster 0**: Moderate market value, balanced debt and market valuation, with average dividends. Stable but not top-performing.
- **Cluster 1**: Undervalued or heavily indebted companies, typically from high-risk sectors. Higher risk, potentially higher returns.
- **Cluster 2**: Premium companies with high market value, low debt, and high dividends. Likely from stable sectors, offering stability and good returns.

## Cluster Visualization

To understand the distribution of stocks within different clusters, the 2D visualization below shows how the clustering algorithm has grouped the data based on the main principal components:

[image](https://github.com/user-attachments/assets/d1dd0ad2-cfc0-4d7f-bea6-e617a7c6857f)

This plot highlights the spread and boundaries of each cluster, aiding in the interpretation of how stocks are categorized.


## Features
- **Predict Cluster**: Enter the stock's features in the text boxes (Market Value per Share, EV to MV Ratio, Dividend per Share, and Sector) and click "Predict Cluster" to get the predicted cluster and its brief description.
- **Interactive UI**: The app provides an interactive user interface where users can input their data and see results instantly.

## Technology Stack
- **Streamlit**: Used to build the interactive web interface.
- **FastAPI**: Used to serve the clustering model through an API.
- **Scikit-Learn**: Used for clustering and scaling the features.
- **Joblib**: Used to load pre-trained models and scalers.

## API URL
The app interacts with a REST API hosted at the following URL to get the cluster prediction:
https://stock-market-clustering.onrender.com/predict


## How to Run Locally
1. Clone this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Run the Streamlit app:
```bash
streamlit run streamlit_app.py
```
The app will be available at http://localhost:8501 in your browser.

## How to Use

1. Open the [app](https://stock-market-clustering.streamlit.app/) in your browser.
 in your browser.
2. In the **Input Features** section, provide the stock details:
   - **Market Value per Share** (in SAR)
   - **EV to MV Ratio**
   - **Dividend per Share** (in SAR)
   - **Sector** (encoded as an integer)
3. Click **Predict Cluster** to see the predicted cluster and a brief description of the cluster.
4. The description will provide insights into the cluster's characteristics, such as the market value, debt levels, and dividends.

## Example Output

- **Cluster 0**: Moderate market value, balanced debt and market valuation, with average dividends. Stable but not top-performing.
- **Cluster 1**: Undervalued or heavily indebted companies, typically from high-risk sectors. Higher risk, potentially higher returns.
- **Cluster 2**: Premium companies with high market value, low debt, and high dividends. Likely from stable sectors, offering stability and good returns.

## Data

All the data used to train the clustering model has been **scripted**. The model takes stock features as input and predicts the cluster based on these features. This app does not require any user-provided data files; it only requires the user to input the features directly in the UI.
