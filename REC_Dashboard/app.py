"""
I-REC Market Dashboard - March 2026
A comprehensive dashboard for understanding the I-REC market
"""


import streamlit as st

import os
from pathlib import Path


# Page configuration
st.set_page_config(
    page_title="I-REC Market Dashboard - March 2026",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a more colorful, modern look
st.markdown("""
<style>
    .metric-card {
        background: linear-gradient(135deg, #43cea2 0%, #185a9d 100%);
        border-radius: 14px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    .metric-value {
        font-size: 36px;
        font-weight: bold;
        color: #fff;
        text-shadow: 1px 1px 2px #185a9d44;
    }
    .metric-label {
        font-size: 15px;
        color: #e0e0e0;
    }
    .section-header {
        background: linear-gradient(90deg, #43cea2 0%, #185a9d 100%);
        color: white;
        padding: 10px;
        border-radius: 7px;
        margin-bottom: 20px;
        font-size: 20px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)




# --- PDF Graphs Notice & Extraction ---


# --- Use screenshots from the root folder (cross-platform, GitHub-friendly) ---
SCREENSHOTS_DIR = Path(__file__).parent
if not SCREENSHOTS_DIR.exists():
    image_paths = []
else:
    # Filter for image files only (exclude .xlsx and other non-images)
    image_paths = sorted([
        str(p) for p in SCREENSHOTS_DIR.iterdir() 
        if p.is_file() and p.suffix.lower() in [".png", ".jpg", ".jpeg"]
    ])

st.info("All graphs below are loaded from the root folder in this repository. To update, add or replace screenshots in that folder and reload the app. This works on all platforms and on GitHub.")


st.sidebar.title("📊 I-REC Dashboard")
st.sidebar.markdown("### March 2026 Data (Static Graphs)")
st.sidebar.info("Graphs are from the official PDF report. Data is not interactive. Screenshots are in the root folder.")


st.title("⚡ I-REC Market Dashboard (Static PDF Graphs)")
st.markdown("### March 2026 - Official Graphs from PDF Report")


# --- Display all images from the root folder ---
if image_paths:
    for idx, img in enumerate(image_paths, 1):
        st.image(img, caption=f"Graph {idx}", use_column_width=True)
else:
    st.warning("No images found in the root folder. Please add screenshots to display them here.")



# --- End of dashboard ---

# ============================================
# FOOTER
# ============================================
st.markdown("---")
st.markdown("""
**Data Source:** Evident I-REC Registry Monthly Statistics  
**Reporting Period:** January 2014 to March 2026  
**Compiled:** 7th April 2026
""")