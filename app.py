import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time
from utils import generate_simulated_data, get_chart_data, calculate_market_share, ATTRIBUTES

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Netflix Conjoint Analysis",
    page_icon="▶️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLING ---
st.markdown("""
<style>
    .stApp {
        background-color: #141414;
        color: white;
    }
    .stMetric {
        background-color: #262626;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #404040;
    }
    /* Customize Sidebar */
    [data-testid="stSidebar"] {
        background-color: #000000;
        border-right: 1px solid #333;
    }
    h1, h2, h3 {
        color: white !important;
    }
    p, label {
        color: #b3b3b3 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- STATE MANAGEMENT ---
if 'data' not in st.session_state:
    with st.spinner('Running Hierarchical Bayes Model...'):
        time.sleep(1.5) # Simulate delay
        st.session_state.data = generate_simulated_data()

if 'sim_options' not in st.session_state:
    st.session_state.sim_options = [
        {'id': 1, 'name': "Current Basic", 'price': 11.99, 'ads': 'None', 'quality': '720p', 'screens': 1},
        {'id': 2, 'name': "New Concept", 'price': 15.49, 'ads': 'Limited', 'quality': '4K+HDR', 'screens': 4}
    ]

# --- SIDEBAR ---
with st.sidebar:
    st.title("▶️ NETFLIX")
    st.markdown("---")
    
    selected_tab = st.radio(
        "Navigation",
        ["Overview", "Utility Analysis", "Market Simulator", "Demographics"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.caption("STATUS")
    st.markdown("🟢 **Model Converged**")

# --- MAIN CONTENT ---
st.title("Netflix Consumer Choice Analysis")
st.caption("Project #10: Data-Driven Growth Strategy")

chart_data = get_chart_data()

# --- OVERVIEW TAB ---
if selected_tab == "Overview":
    col1, col2, col3 = st.columns(3)
    col1.metric("Sample Size", "200", "Total Respondents")
    col2.metric("Choice Tasks", "1,600", "Observed Data Points")
    col3.metric("Model Accuracy", "94.2%", "Hit-Rate Prediction")
    
    st.markdown("---")
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("Attribute Importance")
        st.caption("Which features drive the most value in the subscription decision?")
        fig = px.bar(
            chart_data['importance'], 
            x='value', 
            y='name', 
            orientation='h',
            text='value',
            color_discrete_sequence=['#E50914']
        )
        fig.update_layout(
            plot_bgcolor='#141414',
            paper_bgcolor='#141414',
            font_color='white',
            xaxis={'visible': False},
            yaxis={'title': ''}
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with c2:
        st.subheader("Key Strategic Insight")
        st.info("💡 Price sensitivity is non-linear; significant utility drop-off occurs above $15.49.")
        st.info("💡 Users perceive 'Limited Ads' almost as favorably as 'No Ads' if offset by a 30% price reduction.")
        st.info("💡 4K Quality is a niche motivator, primarily driving retention in premium tiers rather than mass-market acquisition.")
        
        st.error("Recommendation: Implement a 'Goldilocks' tier with Limited Ads and 1080p quality priced at $11.99 to maximize capture of budget-conscious households.")

# --- UTILITIES TAB ---
elif selected_tab == "Utility Analysis":
    st.subheader("Part-Worth Utilities")
    
    cols = st.columns(2)
    
    charts = [
        ('price', cols[0]),
        ('ads', cols[1]),
        ('quality', cols[0]),
        ('screens', cols[1])
    ]
    
    for attr, col in charts:
        with col:
            d = chart_data[attr]
            fig = px.line(
                d['data'], 
                x='name', 
                y='value', 
                title=d['title'],
                markers=True,
                color_discrete_sequence=['#E50914']
            )
            fig.update_layout(
                plot_bgcolor='#262626',
                paper_bgcolor='#262626',
                font_color='white'
            )
            st.plotly_chart(fig, use_container_width=True)

# --- SIMULATOR TAB ---
elif selected_tab == "Market Simulator":
    st.subheader("Market Share Prediction Tool")
    
    col_config, col_result = st.columns([1, 1])
    
    with col_config:
        st.markdown("### Configuration")
        
        # Scenario 1 (Baseline)
        st.markdown("#### Scenario 1 (Baseline)")
        with st.expander("Edit Scenario 1", expanded=True):
            opt1 = st.session_state.sim_options[0]
            opt1['name'] = st.text_input("Name", opt1['name'], key="s1_name")
            opt1['price'] = st.selectbox("Price", ATTRIBUTES['price'], index=ATTRIBUTES['price'].index(opt1['price']), key="s1_price")
            opt1['ads'] = st.selectbox("Ads", ATTRIBUTES['ads'], index=ATTRIBUTES['ads'].index(opt1['ads']), key="s1_ads")
            opt1['quality'] = st.selectbox("Quality", ATTRIBUTES['quality'], index=ATTRIBUTES['quality'].index(opt1['quality']), key="s1_quality")
            opt1['screens'] = st.selectbox("Screens", ATTRIBUTES['screens'], index=ATTRIBUTES['screens'].index(opt1['screens']), key="s1_screens")
            
        # Scenario 2 (Comparison)
        st.markdown("#### Scenario 2 (Comparison)")
        with st.expander("Edit Scenario 2", expanded=True):
            opt2 = st.session_state.sim_options[1]
            opt2['name'] = st.text_input("Name", opt2['name'], key="s2_name")
            opt2['price'] = st.selectbox("Price", ATTRIBUTES['price'], index=ATTRIBUTES['price'].index(opt2['price']), key="s2_price")
            opt2['ads'] = st.selectbox("Ads", ATTRIBUTES['ads'], index=ATTRIBUTES['ads'].index(opt2['ads']), key="s2_ads")
            opt2['quality'] = st.selectbox("Quality", ATTRIBUTES['quality'], index=ATTRIBUTES['quality'].index(opt2['quality']), key="s2_quality")
            opt2['screens'] = st.selectbox("Screens", ATTRIBUTES['screens'], index=ATTRIBUTES['screens'].index(opt2['screens']), key="s2_screens")
            
    with col_result:
        st.markdown("### Predicted Market Share")
        
        share_df = calculate_market_share(st.session_state.sim_options)
        
        fig = px.pie(
            share_df, 
            names='name', 
            values='value', 
            color='name',
            color_discrete_sequence=['#444444', '#E50914'],
            hole=0.5
        )
        fig.update_layout(
             plot_bgcolor='#141414',
             paper_bgcolor='#141414',
             font_color='white',
             legend=dict(orientation="h", y=-0.1)
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Big Numbers
        c1, c2 = st.columns(2)
        c1.metric(share_df.iloc[0]['name'], f"{share_df.iloc[0]['value']}%")
        c2.metric(share_df.iloc[1]['name'], f"{share_df.iloc[1]['value']}%")

# --- DEMOGRAPHICS TAB ---
elif selected_tab == "Demographics":
    st.container()
    st.markdown("""
        <div style="text-align: center; padding: 50px; background-color: #262626; border-radius: 15px;">
            <h3>👥 Segmented Utility Analysis</h3>
            <p style="max-width: 500px; margin: 0 auto; padding-top: 10px;">
                Unlock regional and demographic cuts (Gen Z vs. Boomers) by connecting this project to your actual Customer CRM data.
            </p>
            <br/>
            <button style="
                background-color: transparent; 
                border: 1px solid #666; 
                color: white; 
                padding: 10px 20px; 
                border-radius: 5px; 
                cursor: pointer;">
                Upgrade to Multi-Segment View
            </button>
        </div>
    """, unsafe_allow_html=True)
