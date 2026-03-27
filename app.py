# import streamlit as st
# from crew_setup import agriculture_crew

# st.set_page_config(
#     page_title="AI Agriculture Support System",
#     page_icon="🌾",
#     layout="wide"
# )

# # -------------------------
# # CUSTOM CSS
# # -------------------------
# st.markdown("""
# <style>

# /* App Background */
# .stApp{
# background: linear-gradient(135deg,#e8f5e9,#c8e6c9,#a5d6a7);
# color:#1b1b1b;
# font-family: 'Segoe UI', sans-serif;
# }

# /* Title */
# .title{
# text-align:center;
# font-size:60px;
# font-weight:800;
# background: linear-gradient(90deg,#2e7d32,#66bb6a);
# -webkit-background-clip:text;
# -webkit-text-fill-color:transparent;
# }

# /* Subtitle */
# .subtitle{
# text-align:center;
# font-size:20px;
# color:#333;
# margin-bottom:40px;
# }

# /* Agent Output Cards */
# .agent-card{
# background:white;
# padding:25px;
# border-radius:15px;
# border:1px solid #e0e0e0;
# box-shadow:0px 10px 25px rgba(0,0,0,0.1);
# color:#222;
# }

# /* Sidebar Styling */
# section[data-testid="stSidebar"]{
# background: linear-gradient(180deg,#2e7d32,#388e3c);
# color:white;
# }

# section[data-testid="stSidebar"] *{
# color:white !important;
# }

# /* Buttons */
# button[kind="primary"]{
# background:linear-gradient(90deg,#43a047,#2e7d32);
# border:none;
# border-radius:12px;
# font-size:18px;
# font-weight:600;
# color:white;
# padding:10px 20px;
# }

# /* Button Hover */
# button[kind="primary"]:hover{
# background:linear-gradient(90deg,#2e7d32,#1b5e20);
# }

# /* Input Field */
# .stTextInput input{
# border-radius:10px;
# border:1px solid #a5d6a7;
# padding:10px;
# }

# /* Tabs */
# .stTabs [data-baseweb="tab"]{
# font-size:16px;
# font-weight:600;
# }

# /* Footer hide */
# footer{
# visibility:hidden;
# }

# </style>
# """, unsafe_allow_html=True)

# # -------------------------
# # HEADER
# # -------------------------
# st.markdown('<h1 class="title">🌾 AI Agriculture Support System</h1>', unsafe_allow_html=True)

# st.markdown(
# '<p class="subtitle">Multi-Agent AI system that helps farmers with crops, diseases and government schemes</p>',
# unsafe_allow_html=True
# )

# # -------------------------
# # SIDEBAR
# # -------------------------
# st.sidebar.title("⚙️ Agriculture Settings")

# crop = st.sidebar.selectbox(
#     "Select Crop Type",
#     [
#         "Wheat",
#         "Rice",
#         "Maize",
#         "Cotton",
#         "Vegetables",
#         "Other"
#     ]
# )

# region = st.sidebar.selectbox(
#     "Farming Region",
#     [
#         "North India",
#         "South India",
#         "East India",
#         "West India",
#         "Central India"
#     ]
# )

# st.sidebar.markdown("---")

# st.sidebar.info(
# """
# This AI uses **3 Agriculture Agents**

# 🌱 Crop Advisor  
# 🦠 Disease Expert  
# 🏛 Government Policy Advisor
# """
# )

# # -------------------------
# # USER INPUT
# # -------------------------
# st.markdown("### 💬 Ask the AI Agriculture Assistant")

# user_input = st.text_input(
#     "Example: wheat crop yellow leaves solution",
#     placeholder="Describe your farming problem..."
# )

# generate = st.button("🚀 Get AI Farming Advice")

# # -------------------------
# # WORKFLOW DISPLAY
# # -------------------------
# st.markdown("### 🤖 Agent Workflow")

# st.write("""
# Farmer Question  
# ⬇  
# 🌱 Crop Advisor  
# ⬇  
# 🦠 Disease Expert  
# ⬇  
# 🏛 Government Policy Advisor
# """)

# # -------------------------
# # AI RESPONSE
# # -------------------------
# if generate and user_input:

#     with st.spinner("🤖 Agriculture AI agents are analyzing your query..."):

#         prompt = f"""
# Crop: {crop}
# Region: {region}

# Farmer Question:
# {user_input}

# Generate:
# 1. Crop recommendation and farming advice
# 2. Possible crop disease and treatment
# 3. Government agriculture schemes
# """

#         crew_result = agriculture_crew.kickoff(
#             inputs={"query": prompt}
#         )

#         outputs = [str(t) for t in crew_result.tasks_output]

#         crop_output = outputs[0] if len(outputs) > 0 else ""
#         disease_output = outputs[1] if len(outputs) > 1 else ""
#         policy_output = outputs[2] if len(outputs) > 2 else ""

#     st.markdown("---")
#     st.header("📊 AI Agriculture Analysis")

#     tab1, tab2, tab3 = st.tabs([
#         "🌱 Crop Advisor",
#         "🦠 Disease Expert",
#         "🏛 Government Schemes"
#     ])

#     with tab1:
#         st.subheader("Crop Recommendation")
#         st.markdown(
#             f'<div class="agent-card">{crop_output}</div>',
#             unsafe_allow_html=True
#         )

#     with tab2:
#         st.subheader("Disease Diagnosis")
#         st.markdown(
#             f'<div class="agent-card">{disease_output}</div>',
#             unsafe_allow_html=True
#         )

#     with tab3:
#         st.subheader("Government Schemes")
#         st.markdown(
#             f'<div class="agent-card">{policy_output}</div>',
#             unsafe_allow_html=True
#         )

#     # -------------------------
#     # DOWNLOAD BUTTON
#     # -------------------------
#     st.download_button(
#         label="📥 Download Farming Advice",
#         data=str(policy_output),
#         file_name="agriculture_advice.txt",
#         mime="text/plain"
#     )

# # -------------------------
# # FOOTER
# # -------------------------
# st.markdown("---")

# st.markdown("""
# <center>

# ⚡ Built with **CrewAI + Groq + RAG + Streamlit**

# AI Multi-Agent Agriculture Support System

# </center>
# """, unsafe_allow_html=True)



import streamlit as st
from crew_setup import agriculture_crew

st.set_page_config(
    page_title="🌾 Smart Agriculture AI",
    page_icon="🌱",
    layout="wide"
)

# -------------------------
# 🌿 MODERN UI CSS
# -------------------------
st.markdown("""
<style>

/* Background */
.stApp{
background: linear-gradient(135deg,#e8f5e9,#a5d6a7);
font-family: 'Segoe UI', sans-serif;
}

/* Title */
.title{
text-align:center;
font-size:55px;
font-weight:800;
color:#1b5e20;
}

/* Card */
.card{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 8px 20px rgba(0,0,0,0.1);
margin-bottom:20px;
}

/* Button */
button[kind="primary"]{
background:#2e7d32;
color:white;
border-radius:10px;
font-size:16px;
}

button[kind="primary"]:hover{
background:#1b5e20;
}

/* Sidebar */
section[data-testid="stSidebar"]{
background:#1b5e20;
color:white;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# 🌾 HEADER
# -------------------------
st.markdown('<h1 class="title">🌾 Smart Agriculture AI Assistant</h1>', unsafe_allow_html=True)
st.write("AI-powered farming assistant with Crop, Disease & Policy Intelligence")

# -------------------------
# ⚙️ SIDEBAR SETTINGS
# -------------------------
st.sidebar.header("⚙️ Settings")

crop = st.sidebar.selectbox("🌱 Crop", [
    "Wheat", "Rice", "Maize", "Cotton", "Vegetables", "Other"
])

region = st.sidebar.selectbox("📍 Region", [
    "North India", "South India", "East India", "West India", "Central India"
])

# 🔥 NEW FEATURE
priority = st.sidebar.radio(
    "🚨 Select Priority",
    ["Urgent (Disease)", "Normal", "Planning"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 Priority helps AI focus better")

# -------------------------
# 💬 INPUT
# -------------------------
st.subheader("💬 Ask Your Farming Question")

user_input = st.text_area(
    "Example: Leaves turning yellow in wheat crop",
    height=120
)

generate = st.button("🚀 Generate Smart Advice")

# -------------------------
# 🤖 RESPONSE
# -------------------------
# if generate and user_input:

#     with st.spinner("🤖 AI is analyzing your farm..."):

#         # 🔥 Dynamic Prompt Based on Priority
#         if "Urgent" in priority:
#             focus = "Focus more on disease detection and immediate treatment."
#         elif "Planning" in priority:
#             focus = "Focus more on crop planning and government schemes."
#         else:
#             focus = "Provide balanced advice."

#         prompt = f"""
# Crop: {crop}
# Region: {region}
# Priority: {priority}

# Farmer Question:
# {user_input}

# Instructions:
# {focus}

# Provide:
# 1. Crop Advice
# 2. Disease Solution
# 3. Government Schemes
# """

#         result = agriculture_crew.kickoff(
#             inputs={"query": prompt}
#         )

#         outputs = [str(t) for t in result.tasks_output]

#         crop_output = outputs[0] if len(outputs) > 0 else ""
#         disease_output = outputs[1] if len(outputs) > 1 else ""
#         policy_output = outputs[2] if len(outputs) > 2 else ""

#     st.markdown("---")
#     st.header("📊 AI Analysis Report")

#     col1, col2, col3 = st.columns(3)

#     with col1:
#         st.markdown("### 🌱 Crop Advice")
#         st.markdown(f'<div class="card">{crop_output}</div>', unsafe_allow_html=True)

#     with col2:
#         st.markdown("### 🦠 Disease Solution")
#         st.markdown(f'<div class="card">{disease_output}</div>', unsafe_allow_html=True)

#     with col3:
#         st.markdown("### 🏛 Schemes")
#         st.markdown(f'<div class="card">{policy_output}</div>', unsafe_allow_html=True)


if generate and user_input:

    with st.spinner("🤖 AI analyzing your query..."):

        result = agriculture_crew.kickoff(
            inputs={"query": user_input}
        )

        outputs = [str(t) for t in result.tasks_output]

        detected_priority = outputs[0]
        crop_output = outputs[1]
        disease_output = outputs[2]
        policy_output = outputs[3]

    st.success(f"🎯 Detected Priority: {detected_priority}")

    st.markdown("---")
    st.header("📊 AI Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🌱 Crop Advice")
        st.markdown(f'<div class="card">{crop_output}</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("### 🦠 Disease Solution")
        st.markdown(f'<div class="card">{disease_output}</div>', unsafe_allow_html=True)

    with col3:
        st.markdown("### 🏛 Schemes")
        st.markdown(f'<div class="card">{policy_output}</div>', unsafe_allow_html=True)
    # 📥 Download FULL report
    full_report = f"""
AGRICULTURE AI REPORT

Crop: {crop}
Region: {region}
Priority: {priority}

--- Crop Advice ---
{crop_output}

--- Disease Solution ---
{disease_output}

--- Government Schemes ---
{policy_output}
"""

    st.download_button(
        "📥 Download Full Report",
        full_report,
        file_name="farm_report.txt"
    )

# -------------------------
# FOOTER
# -------------------------
st.markdown("---")
st.markdown("⚡ Built with CrewAI + RAG + Groq")