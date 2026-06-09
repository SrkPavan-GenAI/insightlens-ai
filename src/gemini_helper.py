import google.generativeai as genai

from src.config import (
    GOOGLE_API_KEY,
    MODEL_NAME
)

genai.configure(
    api_key=GOOGLE_API_KEY
)


def get_gemini_response(
    question,
    image,
    max_tokens
):
    model = genai.GenerativeModel(
        MODEL_NAME
    )

    response = model.generate_content(
        [question, image]
    )

    try:
    
        return response.text
    
    except:
    
        return "Gemini did not return a text response."