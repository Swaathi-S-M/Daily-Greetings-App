import streamlit as st
import random
from datetime import datetime

# Page Config
st.set_page_config(
    page_title="Daily Cute Greetings",
    page_icon="🐱",
    layout="centered"
)

# Updated Cute Gradient Background + Styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(to bottom right, #FFF0F5, #E6F7FF);
    }
    .main {
        background: linear-gradient(to bottom right, #FFF0F5, #E6F7FF);
    }
    .cute-box {
        background-color: #FFD6E8;
        padding: 25px;
        border-radius: 25px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        box-shadow: 4px 4px 15px rgba(0,0,0,0.15);
        animation: fadeIn 1s ease-in;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

# Updated Title
st.markdown(
    "<h1 style='text-align: center; color:#FF69B4;'>🌸 Magical Daily Blessings 🌸</h1>",
    unsafe_allow_html=True
)

# Cute doodle images (local paths)
doodles = [
    r"C:\Users\Student\Downloads\k1.avif",
    r"C:\Users\Student\Downloads\k6.jpg",
    r"C:\Users\Student\Downloads\k5.png",
    r"C:\Users\Student\Downloads\k4.jpg",
    r"C:\Users\Student\Downloads\k3.jpg",
    r"C:\Users\Student\Downloads\k2.jpg"
]

# Positive quotes
quotes = [
    "🌸 You are doing better than you think!",
    "🐱 Stay pawsitive today!",
    "🌈 Small steps still count!",
    "💖 You are enough, just as you are.",
    "✨ Shine softly, the world needs your light.",
    "🌷 Progress > Perfection.",
    "🧸 Be kind to yourself today.",
    "🚀 Keep growing, keep glowing!"
]

# Greeting based on time
hour = datetime.now().hour
if hour < 12:
    greeting = "☀️ Good Morning!"
elif hour < 17:
    greeting = "🌤️ Good Afternoon!"
else:
    greeting = "🌙 Good Evening!"

st.markdown(
    f"<h3 style='text-align:center;'>{greeting}</h3>",
    unsafe_allow_html=True
)

# Divider Line (New UI element)
st.markdown("<hr style='border:2px solid #FFB6C1;'>", unsafe_allow_html=True)

# Button interaction
if st.button("🌸 Give Me Today's Cute Message 🌸"):
    quote = random.choice(quotes)
    doodle = random.choice(doodles)

    st.image(doodle, width=220)
    st.markdown(
        f"<div class='cute-box'>{quote}</div>",
        unsafe_allow_html=True
    )

# Updated Footer for CI/CD Test
st.markdown(
    "<br><center>🌈 Auto Build Test Successful! 🌈<br>Made with 💕 and CI/CD magic ✨</center>",
    unsafe_allow_html=True
)
