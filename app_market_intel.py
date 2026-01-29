import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="CMC Market Intelligence", layout="wide")

# 2. Header
st.title("Crypto Market Competitor Intelligence")

# 3. Load Data (Fixed index_col typo)
@st.cache_data
def load_bi_data():
    # Use index_col=0 to tell pandas the first column is our index (timestamp)
    dom_df = pd.read_csv('sector_dominance.csv', index_col=0)
    corr_df = pd.read_csv('btc_correlation.csv', index_col=0)
    
    # Convert index to datetime for proper time-series plotting
    dom_df.index = pd.to_datetime(dom_df.index)
    corr_df.index = pd.to_datetime(corr_df.index)
    
    return dom_df, corr_df

dom_df, corr_df = load_bi_data()

# 4. Sidebar Filters
st.sidebar.header("Intelligence Controls")
days_to_show = st.sidebar.slider("Analysis Period (Days)", 7, 365, 90)

# Filter data based on the slider
filtered_dom = dom_df.tail(days_to_show)

st.success("Data loaded successfully! Use the sidebar to adjust the timeframe.")

st.subheader("Sector Dominance Over Time")
# Prepare data for Plotly
fig_dom = px.area(filtered_dom, 
                 title="Cumulative Market Interest by Sector",
                 labels={"value": "Dominance %", "timestamp": "Date"},
                 color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig_dom, use_container_width=True)

# STEP 1: CALCULATE THE METRIC (Add this before the Recommendation Layer)

# We calculate growth by comparing the last row to the first row of your selected timeframe
latest_growth = (filtered_dom.iloc[-1] - filtered_dom.iloc[0]).sort_values(ascending=False)

# STEP 2: KPI METRICS
col1, col2, col3 = st.columns(3)

with col1:
    # Now latest_growth exists!
    st.metric("Top Trending Sector", latest_growth.index[0], f"{latest_growth[0]:.2f}%")
with col2:
    # Use corr_df we loaded earlier
    decoupler = corr_df.iloc[-1].idxmin()
    st.metric("Key De-coupler", decoupler.split('/')[0], f"Corr: {corr_df.iloc[-1].min():.2f}")
with col3:
    st.metric("Market Sentiment", "Bullish", "High Volume")

# STEP 3: ACTIONABLE RECOMMENDATIONS (The "Analyst" Layer)
st.divider()
st.subheader("Strategic Recommendations")

top_sec = latest_growth.index[0]

# Logic-based recommendation for the CMC Product Team
if "AI" in top_sec:
    rec_text = f"**Marketing Strategy:** {top_sec} tokens are leading market interest. Recommend launching an 'AI Innovation' category spotlight on the CMC homepage."
elif "DeFi" in top_sec:
    rec_text = f"**Operational Strategy:** {top_sec} volume is peaking. Coordinate with the listings team to ensure top DEX pairs have verified liquidity data."
else:
    rec_text = f"**Strategic Growth:** {top_sec} dominance is rising. Recommend an 'Educational Deep-Dive' blog post to drive organic traffic for these assets."

st.info(rec_text)

