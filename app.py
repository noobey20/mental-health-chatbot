import streamlit as st

st.set_page_config(page_title="Mental Health Companion Chatbot", page_icon="💛")

st.markdown(
    "<h1 style='text-align: center; color: white;'>💛 Mental Health Companion Chatbot</h1>",
    unsafe_allow_html=True,
)

st.write("")
st.write("A supportive, safe chatbot for student emotional well-being.")

# Emotion detection
def detect_emotion(text):
    text = text.lower()
    if any(word in text for word in ["sad", "upset", "depressed", "cry"]):
        return "sad"
    elif any(word in text for word in ["stress", "stressed", "tired", "pressure"]):
        return "stress"
    elif any(word in text for word in ["angry", "mad", "frustrated"]):
        return "anger"
    elif any(word in text for word in ["happy", "good", "great", "excited"]):
        return "happy"
    else:
        return "neutral"

# Response generation
def generate_response(emotion):
    if emotion == "sad":
        return "I'm really sorry you're feeling this way… you're not alone. I'm here for you. 💛"
    elif emotion == "stress":
        return "It sounds like things are overwhelming… Take a deep breath. You're doing your best. 💛"
    elif emotion == "anger":
        return "It's okay to feel angry. Your feelings matter, and it's safe to express them here. 💛"
    elif emotion == "happy":
        return "That's wonderful! I'm glad you're feeling good today. Keep smiling! 😊"
    else:
        return "I understand… you can share anything with me. I'm here to listen. 💛"

# Chat interface
user_input = st.text_input("How are you feeling today?")

if user_input:
    st.write(f"**You:** {user_input}")

    emotion = detect_emotion(user_input)
    st.write(f"**Emotion Detected:** `{emotion}`")

    reply = generate_response(emotion)
    st.write(f"**Chatbot:** {reply}")