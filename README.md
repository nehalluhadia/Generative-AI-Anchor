# 🎥 AI News Anchor  

An interactive **Generative AI News Anchor** built with **Streamlit**, which fetches the latest news articles, summarizes them, and generates a talking video anchor using the **D-ID API** with text-to-speech voices.  

---

## 🚀 Features  
- Fetches real-time news using **NewsAPI**.  
- Converts news summaries into a script for an AI anchor.  
- Generates a **talking video avatar** with D-ID API.  
- User can customize:  
  - Anchor image (URL input).  
  - News query keyword(s).  
  - Number of news items (1–5).  
  - AI voice (multiple voice options).  

---

## ⚙️ Setup Instructions  

### 1️⃣ Clone Repository  

git clone <your-repo-url>
cd ai-news-anchor

### 2️⃣ Create Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate   # Mac/Linux

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Setup Environment Variables

Create a .env file in the project root with the following:

NEWS_API_KEY=your_newsapi_key_here
BEARER_TOKEN=your_did_api_key_here


- Get NEWS_API_KEY from NewsAPI
- Get D-ID BEARER_TOKEN from D-ID API

### ▶️ Run the App
streamlit run streamlit_app.py

## 🛠️ How It Works

1. User Input

   - An image URL (anchor face).
   - Query keywords (e.g., "AI", "Sports", "Politics").
   - Number of news items.
   - Voice option.

2. Processing
   - Fetches trending articles via news_api.py.
   - Extracts summaries & creates a short news script.
   - Passes script + image + voice into news_video.py.

3. Output
   - The D-ID API returns a video URL with your AI anchor speaking.

## 📌 Example

- Input:
   - Image URL: https://i.ibb.co/sample-anchor.png
   - Query: Artificial Intelligence
   - Number of News: 3
   - Voice: en-US-JennyNeural

- Output:
   - A video of the AI anchor summarizing the top AI news in real time.

## 🧰 Tech Stack

- Python (Streamlit, Requests, dotenv)
- NewsAPI (fetch latest news)
- D-ID API (AI video generation)
- Microsoft Neural Voices (text-to-speech)

## ⚠️ Troubleshooting

- Error: Video generation failed

   - Check if your D-ID plan allows video generation.
   - Reduce number of news items (too much text may cause timeout).

- News not loading
  - Ensure NEWS_API_KEY is correct & valid.

## 📜 License

This project is for educational & demo purposes. Check individual APIs for their respective terms of use.

