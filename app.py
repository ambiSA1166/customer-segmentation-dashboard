import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Set Page Configuration
st.set_page_config(page_title="Customer Segmentation", page_icon="🛍️", layout="wide")

# 2. Header Section
st.title("🛍️ Customer Segmentation Engine")
st.markdown("""
Welcome to the Customer Segmentation Dashboard. This tool visualizes the results of an **RFM Analysis** combined with **PCA and K-Means Clustering** to divide our customer base into 4 strategic cohorts.
""")
st.divider()

# 3. Load the Data
@st.cache_data
def load_data():
    data = {
        'Segment Name': ['Recent/New', 'Loyal Customers', 'Champions', 'Hibernating'],
        'Recency (Days)': [19.6, 65.9, 11.3, 185.0],
        'Frequency (Trips)': [2.0, 4.3, 13.7, 1.3],
        'Monetary ($)': [498.5, 1823.9, 8128.5, 366.4],
        'Customer Count': [839, 1176, 704, 1619]
    }
    df = pd.DataFrame(data, index=['Cluster 0', 'Cluster 1', 'Cluster 2', 'Cluster 3'])
    return df

df = load_data()

# 4. Create Layout Columns
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📊 Segment Profiles")
    st.markdown("Average behavior metrics for each customer cohort.")
    st.dataframe(df, use_container_width=True)
    
    # --- THE NEW INTERACTIVE PIECE IS SAFELY INDENTED HERE ---
    st.markdown("### 🔍 Deep Dive")
    selected_segment = st.selectbox("Choose a segment to isolate:", df['Segment Name'])
    
    filtered_data = df[df['Segment Name'] == selected_segment]
    
    st.metric(
        label=f"Average Spend for {selected_segment}", 
        value=f"${filtered_data['Monetary ($)'].values[0]:,.2f}"
    )
    # ---------------------------------------------------------

with col2:
    st.subheader("🔥 Behavioral Heatmap")
    st.markdown("Visual contrast of Recency, Frequency, and Monetary values.")
    
    fig, ax = plt.subplots(figsize=(6, 4))
    heatmap_data = df[['Recency (Days)', 'Frequency (Trips)', 'Monetary ($)']]
    sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="YlGnBu", ax=ax, linewidths=.5)
    st.pyplot(fig)

st.divider()

# 5. Strategic Insights Section
st.subheader("🎯 Strategic Recommendations")
st.markdown("Based on the mathematical clustering, we recommend the following marketing actions:")

st.success("**🏆 Champions (Cluster 2):** High engagement and massive spend ($8k+). \n\n*Strategy:* Invite to exclusive VIP programs and offer early-access rewards.")
st.info("**🤝 Loyal Customers (Cluster 1):** Consistent buyers with steady value. \n\n*Strategy:* Execute personalized upsell and cross-sell email campaigns.")
st.warning("**👋 Recent/New (Cluster 0):** Low recency but low frequency; early in their journey. \n\n*Strategy:* Focus on onboarding sequences and 'second-purchase' discount codes.")
st.error("**💤 Hibernating (Cluster 3):** Inactive for over 6 months with the lowest overall spend. \n\n*Strategy:* Deploy automated, low-cost win-back efforts. Do not allocate heavy ad spend here.")