import streamlit as st
import random
from datetime import datetime

# Page Config
st.set_page_config(page_title="Daily Cute Greetings", page_icon="🐱", layout="centered")

# Cute pastel background
st.markdown("""
    <style>
    body {
        background-color: #FFF5F7;
    }
    .main {
        background-color: #FFF5F7;
    }
    .cute-box {
        background-color: #FFE4EC;
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        font-size: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>🌷 Enchanted Beginning! 🌷</h1>", unsafe_allow_html=True)

# Cute doodle images (free kawaii style images)
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
    "🧸 Be kind to yourself today."
]

# Greeting based on time
hour = datetime.now().hour
if hour < 12:
    greeting = "☀️ Good Morning!"
elif hour < 17:
    greeting = "🌤️ Good Afternoon!"
else:
    greeting = "🌙 Good Evening!"

st.markdown(f"<h3 style='text-align:center;'>{greeting}</h3>", unsafe_allow_html=True)

if st.button("🌸 Give Me Today's Cute Message 🌸"):
    quote = random.choice(quotes)
    doodle = random.choice(doodles)

    st.image(doodle, width=200)

    st.markdown(f"<div class='cute-box'>{quote}</div>", unsafe_allow_html=True)

st.markdown("<br><center>Made with 💕 and positive vibes ✨</center>", unsafe_allow_html=True)
