import streamlit as st
import requests
import openai
from news_api import NewsAPI
from news_video import VideoGenerator
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# API keys
news_api_key = os.getenv("NEWS_API_KEY")
video_api_key = os.getenv("BEARER_TOKEN")

# Instances of helper classes
news_client = NewsAPI(api_key=news_api_key)
video_generator = VideoGenerator(video_api_key)

# Streamlit page settings
st.set_page_config(
    page_title="AI News Anchor",
    layout="wide"
)

# Title and styles
st.title("AI News Anchor")
st.markdown('<style>h1{color: orange; text-align: center;}</style>', unsafe_allow_html=True)
st.markdown('<style>h3{color: pink; text-align: center;}</style>', unsafe_allow_html=True)

# Inputs
image_url = st.text_input("Enter Image URL", "")
query = st.text_input("Enter Query Keywords", "")
num_news = st.slider("Number of News", min_value=1, max_value=5, value=3)

# Dropdown for selecting voice
voice_options = [
    "en-US-JennyNeural",
    "en-US-GuyNeural",
    "en-GB-RyanNeural",
    "en-GB-SoniaNeural",
    "en-AU-NatashaNeural"
]
selected_voice = st.selectbox("Choose a Voice", voice_options, index=0)

# Button: Generate
if st.button("Generate"):
    if image_url.strip() and query.strip() and num_news > 0:
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            st.info("Your AI News Anchor: Sophie")
            st.image(image_url, caption="Anchor Image", use_container_width=True)

        with col2:
            desc_list = news_client.get_news_descriptions(query, num_news=num_news)
            st.success("Your Fetched News")
            st.write(desc_list)

            numbered_paragraphs = "\n".join(
                [f"{i+1}. {paragraph}" for i, paragraph in enumerate(desc_list)]
            )
            st.write(numbered_paragraphs)

        with col3:
            # ✅ Limit text length to avoid API timeout
            short_news = " ".join(desc_list[:2])  # first 2 news items only
            if len(short_news) > 350:
                short_news = short_news[:350] + "..."

            final_text = (
                f"Hello, I'm Sophie, your AI News Anchor. "
                f"Here are the latest updates on {query}: {short_news}. "
                "That's all for today. Stay tuned for more updates, thank you!"
            )

            try:
                video_url = video_generator.generate_video(
                    final_text, image_url, voice_id=selected_voice
                )
                st.warning("AI News Anchor Video")
                st.video(video_url)
            except Exception as e:
                st.error(f"⚠️ Video generation failed: {e}")
                st.info("Tip: Try reducing the number of news items or upgrading your D-ID plan.")
    else:
        st.error("⚠️ Failed to fetch news data. Please check your query and API key.")


