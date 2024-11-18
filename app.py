import streamlit as st
import requests
import json

# API URL
API_URL = "https://stock-market-clustering.onrender.com/predict"

# Streamlit UI
st.title("📊 Stock Clustering Prediction App")
st.write("### Discover which cluster a stock belongs to by entering its features below.")

# Sidebar instructions
st.sidebar.header("ℹ️ How to Use")
st.sidebar.write(
    """
1. Adjust the sliders and dropdowns to enter the stock's features.
2. Click **Predict Cluster** to get the result.
3. View the predicted cluster at the bottom.
"""
)

# Feature input sliders and dropdown
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
            st.success(f"🏷️ Predicted Cluster: **{cluster_label}**")
        else:
            st.error(f"❌ Error: {response_data.get('error', 'Unknown error')}")
    except Exception as e:
        st.error(f"❌ Could not connect to the API: {e}")