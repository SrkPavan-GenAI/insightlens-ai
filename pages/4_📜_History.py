import streamlit as st

from src.storage import load_history

st.title("📜 History")

history = load_history()

if not history:

    st.info(
        "No history found."
    )

else:

    for item in history:

        with st.expander(
            f"🖼 {item['image']}"
        ):

            if "timestamp" in item:
                st.write(
                    f"📅 {item['timestamp']}"
                )

            st.markdown(
                "### Question"
            )

            st.write(
                item["question"]
            )

            st.markdown(
                "### Response"
            )

            st.write(
                item["response"]
            )