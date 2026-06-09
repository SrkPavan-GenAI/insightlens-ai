import streamlit as st
from PIL import Image

from src.gemini_helper import get_gemini_response
from src.storage import save_history

st.markdown("""
<style>

.token-card {
    background-color: #262730;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 10px;
    border-left: 4px solid #00C8FF;
}

.token-title {
    font-size: 14px;
    color: #FFFFFF;
    font-weight: 600;
}

.token-value {
    font-size: 28px;
    font-weight: bold;
    color: #FFD700;
}
.cost-card {
    background-color: #262730;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 10px;
    border-left: 4px solid #FFD700;
}

.cost-title {
    font-size: 14px;
    color: #FFFFFF;
    font-weight: 600;
}

.cost-value {
    font-size: 28px;
    font-weight: bold;
    color: #FFD700;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------
# Session State
# ----------------------------------

if "questions_count" not in st.session_state:
    st.session_state.questions_count = 0

if "responses_count" not in st.session_state:
    st.session_state.responses_count = 0

if "images_uploaded" not in st.session_state:
    st.session_state.images_uploaded = 0

# ------------------------------
# Token Tracking
# ------------------------------

if "prompt_tokens" not in st.session_state:
    st.session_state.prompt_tokens = 0

if "response_tokens" not in st.session_state:
    st.session_state.response_tokens = 0

if "total_tokens" not in st.session_state:
    st.session_state.total_tokens = 0
    
# ----------------------------------
# Page Header
# ----------------------------------

st.title("🤖 Image Bot")

st.markdown(
    """
    Upload an image and ask questions about it using Gemini Vision.
    """
)

# ----------------------------------
# Sidebar
# ----------------------------------

with st.sidebar:

    st.header("⚙️ Control Center")

    st.success("Gemini Connected")

    st.markdown("---")

    # -----------------------------
    # Controls
    # -----------------------------

    st.subheader("Actions")

    if st.button("🖼 New Image"):
        st.rerun()

    if st.button("🔄 Refresh Session"):
        st.session_state.clear()
        st.rerun()

    st.markdown("---")

    # -----------------------------
    # Statistics
    # -----------------------------

    st.subheader("📊 Session Statistics")

    st.metric(
        "Images Uploaded",
        st.session_state.images_uploaded
    )

    st.metric(
        "Questions Asked",
        st.session_state.questions_count
    )

    st.metric(
        "Responses Generated",
        st.session_state.responses_count
    )

    st.markdown("---")

    st.subheader("🧠 AI Assistant Prompts")
    
    if st.button("Describe this image"):
        st.session_state.selected_prompt = "🖼 Describe Image"
    
    if st.button("What objects are visible?"):
        st.session_state.selected_prompt = "🔎 What objects are visible?"
    
    if st.button("Summarize the image"):
        st.session_state.selected_prompt = "📋 Summarize Content"
    
    if st.button("Create Study Notes"):
        st.session_state.selected_prompt = "📚 Create Study Notes"
    
    if st.button("Extract key insights"):
        st.session_state.selected_prompt = "🔍 Extract Key Insights"

    if st.button("Generate Quiz Questions"):
        st.session_state.selected_prompt = """
    Generate 10 multiple-choice quiz questions
    based on the uploaded image.
    
    Include:
    
    1. Question
    2. Four options
    3. Correct answer
    """
        
    if st.button("📊 Explain Chart"):
        st.session_state.selected_prompt = "📊 Explain Chart"
        
    st.markdown("---")

    st.subheader("📊 Session Statistics")
    st.markdown("---")

    st.subheader("⚙️ AI Settings")
    
    max_tokens = st.slider(
        "Max Output Tokens",
        min_value=100,
        max_value=4096,
        value=1000,
        step=100
    )
    
    st.markdown("---")

    st.subheader("🪙 Token Usage")

    st.markdown(f"""
    <div class="token-card">
    <div class="token-title">Prompt Tokens</div>
    <div class="token-value">{st.session_state.prompt_tokens}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="token-card">
    <div class="token-title">Response Tokens</div>
    <div class="token-value">{st.session_state.response_tokens}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="token-card">
    <div class="token-title">Total Tokens</div>
    <div class="token-value">{st.session_state.total_tokens}</div>
    </div>
    """, unsafe_allow_html=True)
        
    estimated_cost = (
        st.session_state.total_tokens / 1000000
    ) * 0.10
    
    st.markdown(f"""
    <div class="token-card">
    <div class="token-title">💰 Estimated Cost ($)</div>
    <div class="token-value">{estimated_cost:.5f}</div>
    </div>
    """, unsafe_allow_html=True)

    st.caption(
        "Token estimates are approximate and may vary from actual Gemini usage."
    )
    st.markdown("---")
    
    st.info(
        "Powered by Gemini Vision"
    )
    
# ----------------------------------
# Upload Image
# ----------------------------------

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png", "webp"]
)

# ----------------------------------
# If Image Uploaded
# ----------------------------------

if uploaded_file:
    
    if "current_image" not in st.session_state:

        st.session_state.current_image = uploaded_file.name

        st.session_state.images_uploaded += 1

    elif st.session_state.current_image != uploaded_file.name:

        st.session_state.current_image = uploaded_file.name

        st.session_state.images_uploaded += 1

    # EXISTING CODE CONTINUES 👇

    image = Image.open(uploaded_file)

    col1, col2 = st.columns([1, 1])

    with col1:

        st.image(
            image,
            caption="Uploaded Image",
            width=250
        )
        
    st.caption(
        f"{uploaded_file.name} | {image.format}"
    )

    st.markdown("---")

    # ----------------------------------
    # Question Section
    # ----------------------------------

    if "selected_prompt" not in st.session_state:
        st.session_state.selected_prompt = ""

    question = st.text_area(
        "Ask a Question",
        value=st.session_state.selected_prompt,
        placeholder="What is happening in this image?"
    )

    analyze_btn = st.button(
        "Analyze Image"
    )

    # ----------------------------------
    # Analyze
    # ----------------------------------

    if analyze_btn:

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            with st.spinner(
                "Analyzing image..."
            ):

                try:

                    response_text = get_gemini_response(
                        question,
                        image,
                        max_tokens
                    )

                    prompt_tokens = len(question.split()) * 1.3

                    response_tokens = len(response_text.split()) * 1.3
                    
                    total_tokens = int(
                        prompt_tokens + response_tokens
                    )
                    
                    st.session_state.prompt_tokens += int(prompt_tokens)
                    
                    st.session_state.response_tokens += int(response_tokens)
                    
                    st.session_state.total_tokens += total_tokens

                    st.session_state.questions_count += 1
                    st.session_state.responses_count += 1
                    
                    # Save History

                    save_history(
                        {
                            "image": uploaded_file.name,
                            "question": question,
                            "response": response_text
                        }
                    )

                    st.success(
                        "Analysis Completed"
                    )

                    st.markdown(
                        "## AI Response"
                    )

                    st.write(
                        response_text
                    )

                    st.download_button(
                        label="Download Response",
                        data=response_text,
                        file_name="analysis.txt",
                        mime="text/plain"
                    )

                except Exception as e:

                    st.error(
                        f"Error: {str(e)}"
                    )