import streamlit as st

st.set_page_config(page_title="Power BI Dashboard", layout="wide")

st.title("📊 Power BI Dashboard")

st.markdown("""
This dashboard is embedded from Power BI.  
If you don't see it below, make sure the embed link is public.
""")

# 👇 Replace this URL with your own Power BI embed link
embed_url = "https://app.powerbi.com/view?r=eyJrIjoiZTk3Y..."

st.components.v1.iframe(embed_url, width=1300, height=800, scrolling=True)
