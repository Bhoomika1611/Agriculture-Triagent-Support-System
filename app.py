import streamlit as st
from crew_setup import agriculture_crew

st.set_page_config(
    page_title="AI Agriculture Support System",
    page_icon="🌾",
    layout="wide"
)

# -------------------------
# CUSTOM CSS
# -------------------------
st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}

.title{
text-align:center;
font-size:60px;
font-weight:700;
background: linear-gradient(90deg,#00c6ff,#0072ff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subtitle{
text-align:center;
font-size:20px;
color:#d1d1d1;
margin-bottom:40px;
}

.agent-card{
background:#0b0b0b;
padding:25px;
border-radius:15px;
border:1px solid #333;
}

button[kind="primary"]{
background:linear-gradient(90deg,#00c6ff,#0072ff);
border:none;
border-radius:10px;
font-size:18px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------
st.markdown('<h1 class="title">🌾 AI Agriculture Support System</h1>', unsafe_allow_html=True)

st.markdown(
'<p class="subtitle">Multi-Agent AI system that helps farmers with crops, diseases and government schemes</p>',
unsafe_allow_html=True
)

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("⚙️ Agriculture Settings")

crop = st.sidebar.selectbox(
    "Select Crop Type",
    [
        "Wheat",
        "Rice",
        "Maize",
        "Cotton",
        "Vegetables",
        "Other"
    ]
)

region = st.sidebar.selectbox(
    "Farming Region",
    [
        "North India",
        "South India",
        "East India",
        "West India",
        "Central India"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
"""
This AI uses **3 Agriculture Agents**

🌱 Crop Advisor  
🦠 Disease Expert  
🏛 Government Policy Advisor
"""
)

# -------------------------
# USER INPUT
# -------------------------
st.markdown("### 💬 Ask the AI Agriculture Assistant")

user_input = st.text_input(
    "Example: wheat crop yellow leaves solution",
    placeholder="Describe your farming problem..."
)

generate = st.button("🚀 Get AI Farming Advice")

# -------------------------
# WORKFLOW DISPLAY
# -------------------------
st.markdown("### 🤖 Agent Workflow")

st.write("""
Farmer Question  
⬇  
🌱 Crop Advisor  
⬇  
🦠 Disease Expert  
⬇  
🏛 Government Policy Advisor
""")

# -------------------------
# AI RESPONSE
# -------------------------
if generate and user_input:

    with st.spinner("🤖 Agriculture AI agents are analyzing your query..."):

        prompt = f"""
Crop: {crop}
Region: {region}

Farmer Question:
{user_input}

Generate:
1. Crop recommendation and farming advice
2. Possible crop disease and treatment
3. Government agriculture schemes
"""

        crew_result = agriculture_crew.kickoff(
            inputs={"query": prompt}
        )

        outputs = [str(t) for t in crew_result.tasks_output]

        crop_output = outputs[0] if len(outputs) > 0 else ""
        disease_output = outputs[1] if len(outputs) > 1 else ""
        policy_output = outputs[2] if len(outputs) > 2 else ""

    st.markdown("---")
    st.header("📊 AI Agriculture Analysis")

    tab1, tab2, tab3 = st.tabs([
        "🌱 Crop Advisor",
        "🦠 Disease Expert",
        "🏛 Government Schemes"
    ])

    with tab1:
        st.subheader("Crop Recommendation")
        st.markdown(
            f'<div class="agent-card">{crop_output}</div>',
            unsafe_allow_html=True
        )

    with tab2:
        st.subheader("Disease Diagnosis")
        st.markdown(
            f'<div class="agent-card">{disease_output}</div>',
            unsafe_allow_html=True
        )

    with tab3:
        st.subheader("Government Schemes")
        st.markdown(
            f'<div class="agent-card">{policy_output}</div>',
            unsafe_allow_html=True
        )

    # -------------------------
    # DOWNLOAD BUTTON
    # -------------------------
    st.download_button(
        label="📥 Download Farming Advice",
        data=str(policy_output),
        file_name="agriculture_advice.txt",
        mime="text/plain"
    )

# -------------------------
# FOOTER
# -------------------------
st.markdown("---")

st.markdown("""
<center>

⚡ Built with **CrewAI + Groq + RAG + Streamlit**

AI Multi-Agent Agriculture Support System

</center>
""", unsafe_allow_html=True)