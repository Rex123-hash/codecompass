import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="CodeCompass | IBM watsonx.ai",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Exact CSS from reference design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: #0a0e14;
        font-family: 'IBM Plex Sans', sans-serif;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .main .block-container {
        padding: 1rem 2rem;
        max-width: 1600px;
    }
    
    /* Hero Section - Light with illustrations */
    .hero-section {
        background: linear-gradient(135deg, #e8edf5 0%, #dce4ec 100%);
        border-radius: 20px;
        padding: 3rem;
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: relative;
        overflow: hidden;
    }
    
    .hero-left {
        flex: 1;
    }
    
    .hero-logo-row {
        display: flex;
        align-items: center;
        gap: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .hero-logo {
        width: 70px;
        height: 70px;
        background: #0f62fe;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 2rem;
        font-weight: 600;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 600;
        color: #161616;
        margin: 0;
        line-height: 1;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        color: #525252;
        margin: 1rem 0 1.5rem 0;
        font-weight: 400;
    }
    
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: white;
        padding: 0.5rem 1.2rem;
        border-radius: 25px;
        font-size: 0.95rem;
        color: #0f62fe;
        font-weight: 500;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    }
    
    .hero-badge strong {
        color: #0f62fe;
    }
    
    .hero-right {
        flex: 0 0 500px;
        height: 250px;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 250"><rect x="50" y="30" width="150" height="120" rx="10" fill="%232d3748" opacity="0.8"/><rect x="220" y="50" width="200" height="140" rx="10" fill="%233d4a5f" opacity="0.9"/><rect x="100" y="100" width="80" height="80" rx="12" fill="%2342be65" opacity="0.7"/><circle cx="380" cy="80" r="30" fill="%230f62fe"/><rect x="250" y="80" width="120" height="8" rx="4" fill="%230f62fe" opacity="0.6"/><rect x="250" y="100" width="90" height="8" rx="4" fill="%236f6f6f" opacity="0.4"/><rect x="250" y="120" width="100" height="8" rx="4" fill="%236f6f6f" opacity="0.4"/></svg>') center/contain no-repeat;
    }
    
    /* Section Container */
    .section-container {
        background: #161b26;
        border-radius: 20px;
        padding: 2.5rem;
        margin: 2rem 0;
        border: 1px solid rgba(255,255,255,0.05);
        display: flex;
        gap: 2rem;
    }
    
    .section-left {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1.5rem;
        flex: 0 0 140px;
    }
    
    .section-number {
        width: 55px;
        height: 55px;
        background: #0f62fe;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.4rem;
        font-weight: 700;
        color: white;
    }
    
    .section-icon-box {
        width: 100px;
        height: 100px;
        background: linear-gradient(135deg, #0f62fe 0%, #0043ce 100%);
        border-radius: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 3rem;
        box-shadow: 0 8px 24px rgba(15,98,254,0.3);
    }
    
    .section-right {
        flex: 1;
    }
    
    .section-header-row {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1rem;
    }
    
    .section-title {
        font-size: 2rem;
        font-weight: 600;
        color: white;
        margin: 0;
    }
    
    .section-badge {
        background: rgba(15,98,254,0.15);
        color: #78a9ff;
        padding: 0.3rem 0.9rem;
        border-radius: 15px;
        font-size: 0.85rem;
        font-weight: 500;
    }
    
    .section-description {
        font-size: 1.05rem;
        color: #a8a8a8;
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        background: #1e2530;
        border: 2px solid rgba(255,255,255,0.08);
        border-radius: 10px;
        color: white;
        font-size: 1rem;
        padding: 1rem 1.2rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #0f62fe;
        box-shadow: 0 0 0 3px rgba(15,98,254,0.15);
        background: #252d3a;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #6f6f6f;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #0f62fe 0%, #0043ce 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 1rem 2.5rem;
        font-weight: 600;
        font-size: 1.05rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 16px rgba(15,98,254,0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 24px rgba(15,98,254,0.6);
    }
    
    /* Tag pills */
    .tag-container {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
        margin-top: 1.5rem;
    }
    
    .tag {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        padding: 0.6rem 1.2rem;
        border-radius: 25px;
        font-size: 0.9rem;
        color: #b8b8b8;
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }
    
    .tag-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
    }
    
    .tag-dot.blue { background: #78a9ff; }
    .tag-dot.green { background: #42be65; }
    .tag-dot.purple { background: #be95ff; }
    .tag-dot.cyan { background: #33b1ff; }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: 700;
        color: #0f62fe;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 0.85rem;
        font-weight: 500;
        color: #a0a0a0;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Messages */
    .stSuccess {
        background: rgba(36,161,72,0.12);
        border-left: 4px solid #24a148;
        border-radius: 8px;
        padding: 1rem;
        color: #42be65;
    }
    
    .stError {
        background: rgba(218,30,40,0.12);
        border-left: 4px solid #da1e28;
        border-radius: 8px;
        padding: 1rem;
        color: #ff8389;
    }
    
    .stWarning {
        background: rgba(255,199,0,0.12);
        border-left: 4px solid #ffc700;
        border-radius: 8px;
        padding: 1rem;
        color: #ffd666;
    }
    
    /* Info card */
    .info-card {
        background: rgba(255,255,255,0.02);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 12px;
        padding: 2rem;
        margin: 1.5rem 0;
        color: #e0e0e0;
        line-height: 1.8;
    }
    
    /* Footer */
    .footer-section {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 2.5rem 0;
        margin-top: 3rem;
        border-top: 1px solid rgba(255,255,255,0.06);
    }
    
    .footer-left {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        color: #a0a0a0;
        font-size: 1rem;
    }
    
    .footer-right {
        color: #78a9ff;
        font-size: 1rem;
        display: flex;
        align-items: center;
        gap: 0.8rem;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 8px;
        color: white;
        font-weight: 500;
    }
    
    .stCodeBlock {
        background: rgba(0,0,0,0.3);
        border-left: 3px solid #0f62fe;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <div class="hero-left">
        <div class="hero-logo-row">
            <div class="hero-logo"></></div>
            <h1 class="hero-title">CodeCompass</h1>
        </div>
        <p class="hero-subtitle">AI-Powered Repository Intelligence & Onboarding</p>
        <div class="hero-badge">
            ⚡ Powered by <strong>IBM watsonx.ai</strong>
        </div>
    </div>
    <div class="hero-right"></div>
</div>
""", unsafe_allow_html=True)

# Section 01: Repository Analysis
st.markdown("""
<div class="section-container">
    <div class="section-left">
        <div class="section-number">01</div>
        <div class="section-icon-box">🔍</div>
    </div>
    <div class="section-right">
        <div class="section-header-row">
            <h2 class="section-title">Repository Analysis</h2>
            <span class="section-badge">Instant Insights</span>
        </div>
        <p class="section-description">Enter any GitHub repository URL to get instant architecture insights and understand the big picture.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Input Row
col1, col2 = st.columns([5, 1])
with col1:
    github_url = st.text_input(
        "repo",
        placeholder="🔗 https://github.com/owner/repository",
        label_visibility="collapsed"
    )
with col2:
    analyze_btn = st.button("📊 Analyze", use_container_width=True, type="primary")

# Tags
st.markdown("""
<div class="tag-container">
    <div class="tag"><span class="tag-dot blue"></span>Architecture Overview</div>
    <div class="tag"><span class="tag-dot green"></span>Technology Stack</div>
    <div class="tag"><span class="tag-dot purple"></span>Key Components</div>
    <div class="tag"><span class="tag-dot cyan"></span>Dependencies</div>
</div>
""", unsafe_allow_html=True)

# Analysis Logic
if analyze_btn and github_url:
    with st.spinner("🧭 Analyzing repository..."):
        try:
            response = requests.post(f"{API_URL}/analyze", json={"github_url": github_url}, timeout=120)
            data = response.json()

            if "error" in data:
                st.error(f"❌ {data['error']}")
            else:
                st.session_state["repo_data"] = data
                st.session_state["github_url"] = github_url
                st.success(f"✅ Analysis complete for **{data['owner']}/{data['repo']}**")

                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("📁 Files", f"{data['total_files']:,}")
                with col2:
                    st.metric("🔍 Analyzed", 15)
                with col3:
                    st.metric("✅ Status", "Complete")
                with col4:
                    st.metric("⚡ Engine", "watsonx")

                st.markdown(f'<div class="info-card">{data["summary"]}</div>', unsafe_allow_html=True)

                with st.expander("📋 File Tree (Top 30)", expanded=False):
                    for idx, f in enumerate(data["file_tree"], 1):
                        st.code(f"{idx}. {f}", language=None)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

elif analyze_btn:
    st.warning("⚠️ Please enter a GitHub URL")

# Section 02: Ask Questions
st.markdown("""
<div class="section-container">
    <div class="section-left">
        <div class="section-number">02</div>
        <div class="section-icon-box">💬</div>
    </div>
    <div class="section-right">
        <div class="section-header-row">
            <h2 class="section-title">Ask Questions</h2>
            <span class="section-badge">Get Answers</span>
        </div>
        <p class="section-description">Get instant answers about the repository's architecture, implementation, and how things work.</p>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([5, 1])
with col1:
    question = st.text_input(
        "question",
        placeholder="💡 Where is authentication handled? What does the payment module do? How is data stored?",
        label_visibility="collapsed"
    )
with col2:
    ask_btn = st.button("🚀 Ask", type="primary", use_container_width=True)

st.markdown("""
<div class="tag-container">
    <div class="tag"><span class="tag-dot blue"></span>Authentication Flow</div>
    <div class="tag"><span class="tag-dot green"></span>Database Schema</div>
    <div class="tag"><span class="tag-dot purple"></span>API Endpoints</div>
    <div class="tag"><span class="tag-dot cyan"></span>Payment Module</div>
</div>
""", unsafe_allow_html=True)

if ask_btn and question:
    url = st.session_state.get("github_url", github_url)
    if not url:
        st.warning("⚠️ Analyze a repository first")
    else:
        with st.spinner("🤔 Processing..."):
            try:
                response = requests.post(f"{API_URL}/ask", json={"github_url": url, "question": question}, timeout=120)
                data = response.json()
                st.markdown(f'<div class="info-card">{data.get("answer", "No answer")}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Footer
st.markdown("""
<div class="footer-section">
    <div class="footer-left">
        🛡️ Secure. Private. Powered by AI.
    </div>
    <div class="footer-right">
        🚀 Start exploring your codebase smarter.
    </div>
</div>
""", unsafe_allow_html=True)

# Made with Bob
