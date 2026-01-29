# Crypto Market Competitor Intelligence Dashboard

[![Live Demo](https://img.shields.io/badge/Streamlit-Live%20Demo-brightgreen)](https://crypto-market-intelligence-hycvzqrn8zlttjykahsyc3.streamlit.app/)

## Executive Summary
In the hyper-competitive digital asset landscape, market leadership can shift within hours.  
This project delivers a strategic business intelligence view of the cryptocurrency market, focusing on sector dominance, competitor benchmarking, and capital rotation.

By aggregating and normalizing data from multiple public crypto market data sources, the dashboard visualizes how capital flows across blockchain ecosystems, enabling analysts and decision-makers to identify which protocols are gaining relative strength versus their peers.

---

## Key Features

- **Dynamic Market Share Visualization**  
  Interactive Treemaps and Sunburst charts illustrating dominance shifts between Layer 1 and Layer 2 ecosystems (e.g., Ethereum, Solana, Arbitrum, Base).

- **Sector Performance Heatmaps**  
  High-level views of capital concentration across emerging narratives such as AI, DePIN, and RWA.

- **Competitor Correlation Matrix**  
  Measures price-action relationships between competing assets (e.g., BNB vs. SOL) to detect converging or diverging market sentiment.

- **Top 50 Gainers & Losers Intelligence**  
  Automated reporting that contextualizes short-term market movements and highlights structurally significant trends rather than noise.

---

## Technical Stack

- **Language:** Python 3.10+
- **Data Ingestion:** Public crypto market data APIs (e.g., price, volume, market capitalization endpoints)
- **Data Engineering:**
  - `Pandas` — data normalization, sector grouping, and KPI computation
  - `Requests` — resilient API ingestion with error handling and rate-limit awareness
- **Visualization & Deployment:**
  - `Plotly` — interactive analytical visualizations
  - `Streamlit` — web-based BI dashboard deployment

---

## Strategic Analysis Logic

The dashboard evaluates competitive positioning and ecosystem health using derived analytics and comparative indicators:

1. **Relative Dominance Index (RDI)**  
   Measures asset-level market capitalization growth relative to the broader crypto market to identify outperformers.

2. **Capital Velocity**  
   Uses Volume-to-Market-Cap ratios to assess capital efficiency and distinguish between overheated and under-accumulated sectors.

3. **Ecosystem Stickiness (Proxy Indicators)**  
   Combines liquidity persistence, relative valuation stability, and ecosystem growth signals as leading indicators of market share retention.

---

## Business Value

- **Strategic Benchmarking**  
  Enables projects, analysts, and researchers to assess competitive positioning within crowded market segments.

- **Trend & Narrative Detection**  
  Acts as an early-warning system for sector rotations, supporting proactive strategy and allocation decisions.

- **Executive-Ready Reporting**  
  Condenses thousands of assets into a small set of decision-critical market signals suitable for stakeholder communication.

