# 🛍️ Customer Segmentation Engine

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Machine Learning](https://img.shields.io/badge/Scikit--Learn-K--Means-F7931E?logo=scikit-learn&logoColor=white)]()

**👉 See it in action:** [Live Streamlit Dashboard](https://ambika-uci-customer-segmentation.streamlit.app/)

## What is this?
I built this project to see if I could take a massive, messy dataset of raw retail receipts and turn it into something a marketing team could actually use. 

Using the UCI Online Retail dataset (over 500,000 rows of transactional data), I built a machine learning pipeline that automatically groups customers based on their buying behavior. I then wrapped the results in a clean, interactive Streamlit web app so non-technical folks can explore the data and see the business strategies for each group.

## How I built it (The Pipeline)

Dealing with half a million rows of raw data isn't pretty. Here is exactly how I got from raw CSV to a live web app:

### 1. Cleaning the Mess
Real-world data is dirty. Before running any math, I had to scrub the dataset:
* **Missing IDs:** Dropped rows without Customer IDs. If we don't know who bought it, we can't build a profile for them.
* **Cancellations & Returns:** Filtered out negative quantities and cancelled invoices so the revenue numbers actually reflect retained money.

### 2. Feature Engineering (RFM)
Machine learning models can't read a receipt, so I aggregated the 500,000+ transactions into about 4,300 unique customer profiles using the **RFM** framework:
* **Recency:** Days since their last purchase.
* **Frequency:** How many distinct times they shopped with us.
* **Monetary:** Total amount of money they spent.

### 3. The Math & Machine Learning
* **Taming the Skew:** Financial data is always skewed by a few massive spenders. I applied a log transformation so the algorithm wouldn't get confused by the outliers.
* **Scaling:** Scaled everything using `StandardScaler` so that days and dollars were weighed equally.
* **PCA:** Ran Principal Component Analysis to compress the data, making it easier for the algorithm to process and allowing me to plot it on a 2D graph.
* **K-Means Clustering:** Used the K-Means algorithm to group the customers. I used the "Elbow Method" to mathematically prove that splitting them into **4 distinct segments** was the optimal choice.

### 4. The Final Segments
The model naturally divided the customers into these four strategic buckets:
1. **🏆 Champions:** High spenders who buy frequently.
2. **🤝 Loyal Customers:** Steady, consistent buyers.
3. **👋 Recent/New:** Just made their first few purchases.
4. **💤 Hibernating:** Haven't bought anything in months.

## What's in this repository?

To make the web app run lightning-fast on the free cloud tier, I separated the heavy machine learning logic from the app UI. 

* `Untitled.ipynb`: This is where all the heavy lifting, data cleaning, and scikit-learn model training happens.
* `Online Retail.csv`: The original raw dataset (541k rows).
* `app.py`: The interactive Streamlit dashboard code using Plotly for the visualizations.
* `requirements.txt`: list of Python libraries needed to run the app online.
* `.streamlit/`: Contains the `config.toml` file to give the app a custom, warm pastel UI theme instead of the default Streamlit look.
* `pca_data.csv` & `inertia_data.csv`: Lightweight data exports from the Jupyter notebook so the web app doesn't have to recalculate the ML math every time someone clicks the link.

