# Ai_Trip_Planner

# 🧠 AI Trip Planner

An intelligent travel planning web app built with **Python**, **Streamlit**, and **Google Gemini API**.  
It helps users create personalized travel itineraries based on their preferences — destinations, budget, duration, and interests.

---

## 🚀 Features

- 🗺️ **AI-Powered Recommendations** — Uses Google Gemini to suggest destinations, activities, and hotels.
- 📅 **Smart Itinerary Generation** — Creates a full travel plan with day-wise scheduling.
- 💰 **Budget Optimization** — Suggests affordable or luxury options based on your budget range.
- 🌤️ **Weather Insights** — Provides climate information for your travel dates.
- 🧳 **Custom Filters** — Choose interests like adventure, relaxation, culture, food, etc.
- ⚡ **Instant Results** — Built with Streamlit for a fast and interactive experience.

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend/UI** | Streamlit |
| **Backend** | Python |
| **AI Model** | Google Gemini API |
| **Environment Management** | Virtualenv / Conda |
| **Deployment** | Streamlit Cloud / Netlify / Render |

---

## 🏗️ Project Structure

ai-trip-planner/
│
├── app.py # Main Streamlit app
├── requirements.txt # Dependencies
├── .env # Environment variables (API keys)
├── utils/
│ ├── gemini_api.py # Functions to call Gemini API
│ ├── itinerary_builder.py# Logic to generate trip plans
│ └── helpers.py # Additional utilities
├── assets/
│ └── images/ # Optional images and icons
└── README.md # Project documentation


---

## 🔑 Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/ai-trip-planner.git
cd ai-trip-planner

2️⃣ Create a virtual environment
python -m venv my_env
my_env\Scripts\activate      # (Windows)
source my_env/bin/activate   # (Mac/Linux)

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add your API keys

Create a .env file in the project root and add:

GEMINI_API_KEY=your_gemini_api_key

5️⃣ Run the app
streamlit run app.py

💡 Example Usage

1-Enter your destination, budget, and number of days.

2-Select your travel interests (adventure, nature, history, etc.).

3-Click “Generate Trip Plan” — The AI will generate a detailed itinerary!

4-View recommendations for places, hotels, and activities.

🧠 Powered By

Streamlit

Google Gemini API

Python 3.10+

📸 Demo Screenshot

Add a screenshot of your running app here
<img width="770" height="929" alt="Screenshot 2025-11-08 190534" src="https://github.com/user-attachments/assets/9737418c-4f89-415b-abee-389147760dee" />

![App Screenshot]<img width="770" height="929" alt="Screenshot 2025-11-08 190534" src="https://github.com/user-attachments/assets/ce5c5692-d09c-4184-9d3a-2f6289a0701f" />
