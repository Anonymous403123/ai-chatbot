# 🤖 AI Chatbot

> A smart conversational AI chatbot built with Python and Streamlit that combines rule-based responses with generative AI capabilities.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![OpenRouter](https://img.shields.io/badge/OpenRouter-API-orange?style=for-the-badge)](https://openrouter.ai)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)

## 📌 Overview

This is a **simple yet powerful chatbot** that demonstrates two approaches to conversational AI:
- **Rule-based responses** for common interactions
- **AI-powered generation** for dynamic conversations

The chatbot features a clean, modern web interface built with Streamlit and can run both with and without an API key.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎯 **Dual Mode** | Rule-based + AI-powered responses |
| 💬 **Chat History** | Maintains conversation context |
| 🎨 **Modern UI** | Clean, responsive Streamlit interface |
| 🔄 **Clear Chat** | One-click conversation reset |
| ⚡ **Fast Response** | Optimized for quick replies |
| 🆓 **Free Tier** | Works with OpenRouter free models |

## 🛠️ Tech Stack

<details>
<summary>Click to expand</summary>

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **Streamlit** | Web interface framework |
| **OpenRouter API** | AI model provider (free tier) |
| **Requests** | API communication |
| **Session State** | Chat history management |

</details>

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) OpenRouter API key

### Step-by-Step Guide

```bash
# 1. Clone the repository
git clone https://github.com/Anonymous403123/ai-chatbot.git
cd ai-chatbot

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
streamlit run app.py