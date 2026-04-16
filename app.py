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