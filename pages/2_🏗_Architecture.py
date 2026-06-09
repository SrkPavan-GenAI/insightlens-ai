import streamlit as st

st.set_page_config(
    page_title="Architecture",
    page_icon="🏗",
    layout="wide"
)

st.title("🏗 Architecture")

st.markdown("""
This section illustrates the architecture,
implementation workflow, enterprise scalability,
and future roadmap of InsightLens AI.

""")

# ROW 1

col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 User Flow")
    st.image(
        "architecture/user_flow.png",
        use_container_width=True
    )

with col2:
    st.subheader("⚙️ Developer Flow")
    st.image(
        "architecture/developer_flow.png",
        use_container_width=True
    )

# ROW 2

col3, col4 = st.columns(2)

with col3:
    st.subheader("🏢 Enterprise Flow")
    st.image(
        "architecture/enterprise_flow.png",
        use_container_width=True
    )

with col4:
    st.subheader("🚀 Enterprise Roadmap")
    st.image(
        "architecture/enterprise_structure.png",
        use_container_width=True
    )
