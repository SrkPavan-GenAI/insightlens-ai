import streamlit as st

def show_footer():

    st.markdown("---")

    st.markdown(
        """
        <div style='text-align:center;
                    font-size:14px;
                    color:#808080;
                    padding:15px;'>

            🔍 InsightLens AI<br>

            Built by <b>Srk Pavan Kumar</b><br>

            Powered by Gemini Vision + Streamlit

        </div>
        """,
        unsafe_allow_html=True
    )