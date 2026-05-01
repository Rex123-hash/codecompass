import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="CodeCompass 🧭",
    page_icon="🧭",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #0062ff, #00b4d8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .sub-header {
        text-align: center;
        color: #888;
        margin-bottom: 2rem;
    }
    .metric-box {
        background: #1e1e2e;
        border-radius: 10px;
        padding: 1rem;
        border: 1px solid #0062ff;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">🧭 CodeCompass</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Turn any GitHub repository into an instant onboarding experience</p>', unsafe_allow_html=True)

st.divider()

github_url = st.text_input(
    "🔗 Paste a GitHub Repository URL",
    placeholder="https://github.com/owner/repository",
    help="Enter any public GitHub repository URL"
)

col1, col2 = st.columns([1, 4])
with col1:
    analyze_btn = st.button("🚀 Analyze Repo", use_container_width=True, type="primary")

if analyze_btn and github_url:
    with st.spinner("🧭 CodeCompass is mapping your codebase..."):
        try:
            response = requests.post(
                f"{API_URL}/analyze",
                json={"github_url": github_url},
                timeout=120
            )
            data = response.json()

            if "error" in data:
                st.error(f"❌ {data['error']}")
            else:
                st.session_state["repo_data"] = data
                st.session_state["github_url"] = github_url

                st.success(f"✅ Analysis complete for **{data['owner']}/{data['repo']}**")

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("📁 Total Files", data["total_files"])
                with col2:
                    st.metric("🔍 Files Analyzed", min(data["total_files"], 10))

                st.divider()

                st.subheader("🏗️ Architecture Summary")
                st.markdown(data["summary"])

                st.divider()

                st.subheader("📂 File Tree (Top 30)")
                with st.expander("View all files"):
                    for f in data["file_tree"]:
                        st.code(f, language=None)

        except Exception as e:
            st.error(f"❌ Could not connect to backend: {e}")

elif analyze_btn and not github_url:
    st.warning("⚠️ Please enter a GitHub URL first.")

st.divider()

st.subheader("💬 Ask CodeCompass Anything")
st.caption("Ask specific questions about the repository after analyzing it.")

question = st.text_input(
    "Your question",
    placeholder="Where is authentication handled? What does the payment module do?"
)

ask_btn = st.button("💡 Ask", type="secondary")

if ask_btn and question:
    url = st.session_state.get("github_url", github_url)
    if not url:
        st.warning("⚠️ Please analyze a repository first.")
    else:
        with st.spinner("🤔 Thinking..."):
            try:
                response = requests.post(
                    f"{API_URL}/ask",
                    json={"github_url": url, "question": question},
                    timeout=120
                )
                data = response.json()
                st.markdown("### 💡 Answer")
                st.markdown(data.get("answer", "No answer returned."))
            except Exception as e:
                st.error(f"❌ Error: {e}")

st.divider()
st.caption("Built with ❤️ using IBM Bob + watsonx.ai | IBM Bob Dev Day Hackathon 2026")