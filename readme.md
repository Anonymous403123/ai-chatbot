# 🤖 AI Chatbot with Web Interface

A simple yet powerful AI chatbot built using **Streamlit** and powered by the **OpenRouter API**. This project provides an interactive web-based chat interface with customizable model settings and chat history management.

---

## 🚀 Features

- 💬 Interactive chat interface
- ⚙️ Adjustable model and temperature settings
- 🧠 Supports multiple free AI models via OpenRouter
- 🗑️ Clear chat & 💾 export chat history
- ⏱️ Timestamped messages
- 🔌 Fallback echo bot (no API required)

---

## 🛠️ Setup & Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies
```bash
pip install streamlit requests
```

### 4. Add Your API Key
- Get your API key from: https://openrouter.ai/keys  
- Open the Python file and replace:
```python
API_KEY = "YOUR_OPENROUTER_API_KEY"
```

### 5. Run the App
```bash
streamlit run app.py
```

### 6. Open in Browser
```
http://localhost:8501
```

---

## 🧠 Approach

This chatbot is built using an API-based approach:

- Uses the OpenRouter API to access multiple AI models
- No fine-tuning or RAG — purely live API inference
- Maintains conversation context using session state
- Includes a fallback rule-based echo bot for offline testing

### ✨ What Makes It Unique?

- 🔄 Auto model routing (uses best available free model)
- 🎛️ Real-time temperature control for creativity
- 💡 Beginner-friendly with no heavy ML setup required

---

## ⚠️ Challenges & Solutions

### 1. API Errors & Timeouts
**Challenge:** Handling API failures and delays  
**Solution:** Added error handling for timeouts, connection issues, and API errors

### 2. Managing Chat State
**Challenge:** Maintaining conversation history  
**Solution:** Used Streamlit session_state to persist messages

### 3. Testing Without API Key
**Challenge:** App breaks without API key  
**Solution:** Implemented an echo bot fallback for testing

---

## 📌 Future Improvements

- Add memory (long-term conversation storage)
- Integrate RAG for knowledge-based responses
- Improve UI/UX with themes and animations
- Deploy on cloud (Streamlit Cloud / AWS)

---

## 📄 License

This project is open-source and free to use.
