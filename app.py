import streamlit as st
import requests
import google.generativeai as genai




# API
API_URL = "https://stock-market-clustering.onrender.com/predict"

# GEMINI_API_KEY
# genai.configure(api_key=GEMINI_API_KEY)

# # Create the model
# generation_config = {
#   "temperature": 1,
#   "top_p": 0.95,
#   "top_k": 40,
#   "max_output_tokens": 8192,
#   "response_mime_type": "text/plain",
# }

# model = genai.GenerativeModel(
#   model_name="gemini-1.5-flash",
#   generation_config=generation_config,
# )

# chat_session = model.start_chat(
#   history=[
#   ]
# )

# Cluster descriptions
cluster_descriptions = {
    0: "Moderate market value, balanced debt and market valuation, with average dividends. Stable but not top-performing.",
    1: "Undervalued or heavily indebted companies, typically from high-risk sectors. Higher risk, potentially higher returns.",
    2: "Premium companies with high market value, low debt, and high dividends. Likely from stable sectors, offering stability and good returns.",
}

# Sector encoding
sector_mapping = {
    5: "Financial Services",
    0: "Basic Materials",
    7: "Industrials",
    2: "Consumer Cyclical",
    8: "Real Estate",
    3: "Consumer Defensive",
    6: "Healthcare",
    1: "Communication Services",
    4: "Energy",
    9: "Technology",
    10: "Utilities",
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
symbol = st.text_input("Symbol", "2222")
market_value_per_share = st.text_input("Market Value per Share", "50.0")
ev_to_mv_ratio = st.text_input("EV to MV Ratio", "1.0")
dividend_per_share = st.text_input("Dividend per Share", "5.0")
sector = st.selectbox(
    "Sector", 
    options=sector_mapping.keys(), 
    format_func=lambda x: f"{sector_mapping[x]}"
)

# Display current selections
st.write("#### Your Selections")
st.write(
    f"""
- **Market Value per Share**: {market_value_per_share}   
- **EV to MV Ratio**: {ev_to_mv_ratio}  
- **Dividend per Share**: {dividend_per_share}   
- **Sector**: {sector_mapping[sector]}
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
                
                # response = chat_session.send_message(f"Provide a brief description of the company associated with the stock symbol {symbol} in the Saudi market. The description should include general information about the company's sector and primary activities. It is ok if it not Real-time data")
                
                # st.write(response.text)

            else:
                st.error(f"❌ Error: {response_data.get('error', 'Unknown error')}")
        except Exception as e:
            st.error(f"❌ Could not connect to the API: {e}")