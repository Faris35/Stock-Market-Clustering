import streamlit as st
import requests

# API URL
API_URL = "https://stock-market-clustering.onrender.com/predict"

# Cluster descriptions
cluster_descriptions = {
    0: "Moderate market value, balanced debt and market valuation, with average dividends. Stable but not top-performing.",
    1: "Undervalued or heavily indebted companies, typically from high-risk sectors. Higher risk, potentially higher returns.",
    2: "Premium companies with high market value, low debt, and high dividends. Likely from stable sectors, offering stability and good returns.",
}

# Streamlit UI
st.title("📊 Stock Clustering Prediction App")
st.write("### Discover which cluster a stock belongs to by entering its features below.")

# Sidebar instructions
st.sidebar.header("ℹ️ How to Use")
st.sidebar.write(
    """
1. Enter the stock's features directly into the text boxes below.
2. Click **Predict Cluster** to get the result.
3. View the predicted cluster and its brief description at the bottom.
"""
)

# Feature input text boxes
st.write("#### Input Features")
market_value_per_share = st.text_input("Market Value per Share (in SAR)", "50.0")
ev_to_mv_ratio = st.text_input("EV to MV Ratio", "1.0")
dividend_per_share = st.text_input("Dividend per Share (in SAR)", "5.0")
sector = st.selectbox(
    "Sector (encoded)", 
    options={
        1: "Energy",
        2: "Financials",
        3: "Healthcare",
        4: "Technology",
        5: "Consumer Goods",
    }, 
    format_func=lambda x: f"{x} - {['Energy', 'Financials', 'Healthcare', 'Technology', 'Consumer Goods'][x-1]}"
)

# Display current selections
st.write("#### Your Selections")
st.write(
    f"""
- **Market Value per Share**: {market_value_per_share} SAR  
- **EV to MV Ratio**: {ev_to_mv_ratio}  
- **Dividend per Share**: {dividend_per_share} SAR  
- **Sector**: {sector} - {['Energy', 'Financials', 'Healthcare', 'Technology', 'Consumer Goods'][sector-1]}
"""
)

# Prediction button
if st.button("🔍 Predict Cluster"):
    # Ensure that the inputs are valid numbers
    try:
        market_value_per_share = float(market_value_per_share)
        ev_to_mv_ratio = float(ev_to_mv_ratio)
        dividend_per_share = float(dividend_per_share)
    except ValueError:
        st.error("❌ Please enter valid numbers for all features.")
    else:
        # Prepare data
        input_data = {
            "market_value_per_share": market_value_per_share,
            "ev_to_mv_ratio": ev_to_mv_ratio,
            "dividend_per_share": dividend_per_share,
            "sector": sector,
        }

        try:
            # Call API
            response = requests.post(API_URL, json=input_data)
            response_data = response.json()

            # Display result
            if "pred" in response_data:
                cluster_label = response_data["pred"]
                description = cluster_descriptions.get(cluster_label, "No description available.")
                st.success(f"🏷️ Predicted Cluster: **{cluster_label}**")
                st.write(f"### Description: {description}")
            else:
                st.error(f"❌ Error: {response_data.get('error', 'Unknown error')}")
        except Exception as e:
            st.error(f"❌ Could not connect to the API: {e}")