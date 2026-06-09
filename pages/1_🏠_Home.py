import streamlit as st

st.title(
    "🏠 Home"
)

st.markdown(
    """
    ## 🔍 InsightLens AI

    Multimodal Visual Intelligence Assistant
    
    Upload images, analyze content,
    generate insights, create study notes,
    and interact with Gemini Vision.

    ### Tech Stack

    - Python
    - Streamlit
    - Gemini Vision
    - Pillow

    ### Use Cases

    - Education
    - Research
    - Document Analysis
    - Visual Intelligence

    """

)

st.markdown("""
## Use Cases

- Education
- Research
- Document Analysis
- Visual Intelligence
""")

st.subheader("📊 Project Statistics")

col1, col2 = st.columns(2)

with col1:
    st.success("✓ Gemini Vision")
    st.success("✓ Streamlit")
    st.success("✓ History Tracking")

with col2:
    st.success("✓ Token Monitoring")
    st.success("✓ Download Responses")
    st.success("✓ Enterprise Architecture")

st.markdown("---")

st.markdown(
    """
    <div style="
        text-align:center;
        padding:25px;
        color:#6B7280;
        font-size:15px;
    ">

        🔍 InsightLens AI
        
        🚀 Built by Srk Pavan Kumar
        
        ⚡ Powered by Gemini Vision + Streamlit

    </div>
    """,
    unsafe_allow_html=True
)