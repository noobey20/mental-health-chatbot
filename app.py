import streamlit as st

st.set_page_config(page_title="Mental Health Companion", page_icon="💛")

st.title("💛 Mental Health Companion Chatbot")
st.write("A supportive, safe chatbot for student emotional well-being.")

if "chat" not in st.session_state:
    st.session_state.chat = []

def detect_emotion(text):
    t = text.lower()
    if any(w in t for w in ["sad", "hurt", "lonely", "upset"]):
        return "sad"
    if any(w in t for w in ["stressed", "anxious", "tense"]):
        return "stressed"
    if any(w in t for w in ["happy", "good", "great"]):
        return "happy"
    return "neutral"

def reply(emotion):
    if emotion == "happy":
        return "That's nice to hear. Keep going 😊"
    if emotion == "sad":
        return "I'm here with you. You can share what's on your mind."
    if emotion == "stressed":
        return "Take a slow breath. Things will settle. I'm here for you."
    return "I understand. Tell me more."

for m in st.session_state.chat:
    st.chat_message(m["role"]).markdown(m["text"])

user = st.chat_input("How are you feeling today?")

if user:
    st.session_state.chat.append({"role": "user", "text": user})
    st.chat_message("user").markdown(user)

    mood = detect_emotion(user)
    bot = f"Emotion Detected: {mood}\n\n" + reply(mood)

    st.chat_message("assistant").markdown(bot)
    st.session_state.chat.append({"role": "assistant", "text": bot})