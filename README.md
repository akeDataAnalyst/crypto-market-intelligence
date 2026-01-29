# Crypto Market Competitor Intelligence Dashboard

[![Live Demo](https://img.shields.io/badge/Streamlit-Live%20Demo-brightgreen)](https://crypto-market-intelligence-hyeqcs3cpjzjxkokkjbxcu.streamlit.app/)

## Executive Summary
In the hyper-competitive 2026 digital asset landscape, market share is won and lost in hours. This project provides a high-level strategic overview of the cryptocurrency market, focusing on Sector Dominance and Competitor Benchmarking. 
By aggregating live data visualizes capital rotation across different blockchain ecosystems, enabling strategists to identify which protocols are gaining "Relative Strength" compared to their peers.

## Key Features
- **Dynamic Market Share Visualization:** Real-time Treemaps and Sunburst charts showing the dominance of L1s (Ethereum, Solana) vs. L2s (Arbitrum, Base).
- **Sector Performance Heatmaps:** A birds-eye view of which narrative (e.g., DePIN, RWA, AI) is currently attracting the most capital.
- **Competitor Correlation Matrix:** Analyzes price-action synergy between rival projects (e.g., BNB vs. SOL) to detect diverging market sentiment.
- **Top 50 Gainer/Loser Intelligence:** Automated reporting on the "So What?" behind market moves, filtering out noise to highlight structural growth.

## Technical Stack
- **Language:** Python 3.10+
- **Data Ingestion:** CoinMarketCap Professional API / CoinGecko Pro API.
- **Data Engineering:** - `Pandas`: Multi-index data structures for sector-based grouping.
  - `Requests`: Robust API polling with error handling and rate-limit management.
- **Visualization:** Plotly (Interactive charts) & Streamlit (Web deployment).

## Strategic Analysis Logic
The dashboard calculates "Competitor Health" through three proprietary metrics:
1. **Relative Dominance Index (RDI):** Measuring an asset's market cap growth relative to the Total Crypto Market Cap ($TOTAL$).
2. **Capital Velocity:** Tracking 24h Volume-to-Market Cap ratios to identify "Overheated" vs. "Under-accumulated" sectors.
3. **Ecosystem Stickiness:** Mapping TVL (Total Value Locked) and developer activity as a lead indicator of market share retention.

## Business Value
- **Strategic Benchmarking:** Helps projects understand their positioning relative to direct competitors.
- **Trend Identification:** Early-warning system for "Narrative Rotations," allowing for proactive portfolio rebalancing.
- **Stakeholder Reporting:** Generates C-suite ready visuals that distill 10,000+ coins into 5 critical market signals.
