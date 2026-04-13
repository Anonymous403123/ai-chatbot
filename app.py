import streamlit as st
import requests
import json
from datetime import datetime

# ============================================
# CONFIGURATION
# ============================================

# 🔑 Get your API key from https://openrouter.ai/keys
# For testing without API key, you can use a simple echo bot (see alternative below)

API_KEY = "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"  # Replace with your actual API key

# Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ============================================
# INITIALIZE SESSION STATE
# ============================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "model" not in st.session_state:
    st.session_state.model = "openrouter/free"  # Auto-selects working free model

if "temperature" not in st.session_state:
    st.session_state.temperature = 0.7

# ============================================
# SIDEBAR SETTINGS
# ============================================

with st.sidebar:
    st.title("⚙️ Settings")
    
    # Model selection
    st.subheader("Model")
    model_option = st.radio(
        "Choose model type:",
        ["Auto (Recommended)", "Manual Select"],
        index=0
    )
    
    if model_option == "Manual Select":
        st.session_state.model = st.selectbox(
            "Model:",
            [
                "openrouter/free",
                "microsoft/phi-3-mini-128k-instruct:free",
                "meta-llama/llama-3.2-3b-instruct:free",
                "qwen/qwen-2.5-7b-instruct:free"
            ],
            help="Free models have rate limits"
        )
    else:
        st.session_state.model = "openrouter/free"
        st.info("🤖 Using auto-router for best available free model")
    
    # Temperature control
    st.subheader("Creativity")
    st.session_state.temperature = st.slider(
        "Temperature:",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1,
        help="Higher = more creative, Lower = more focused"
    )
    
    st.divider()
    
    # Chat controls
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
    
    with col2:
        if st.button("💾 Export Chat", use_container_width=True):
            chat_text = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages])
            st.download_button(
                label="📥 Download",
                data=chat_text,
                file_name=f"chat_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )
    
    # API Status
    st.divider()
    st.caption("📡 API Status")
    if API_KEY == "YOUR_OPENROUTER_API_KEY":
        st.error("⚠️ Please add your OpenRouter API key")
        st.caption("Get one at [openrouter.ai/keys](https://openrouter.ai/keys)")
    else:
        st.success("✅ API key configured")

# ============================================
# MAIN CHAT INTERFACE
# ============================================

st.title("🤖 AI Chatbot")
st.caption("💡 Ask me anything! I'm powered by OpenRouter's free AI models.")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        # Show timestamp for older messages
        if "timestamp" in message:
            st.caption(f"🕐 {message['timestamp']}")

# ============================================
# CHAT INPUT & RESPONSE HANDLING
# ============================================

def get_bot_response(messages):
    """Get response from OpenRouter API"""
    
    # Prepare messages for API
    api_messages = []
    for msg in messages:
        api_messages.append({
            "role": msg["role"],
            "content": msg["content"]
        })
    
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://localhost:8501",
                "X-Title": "Streamlit Chatbot"
            },
            json={
                "model": st.session_state.model,
                "messages": api_messages,
                "temperature": st.session_state.temperature,
                "max_tokens": 1000,
                "top_p": 0.9,
                "frequency_penalty": 0,
                "presence_penalty": 0
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            error_data = response.json()
            error_msg = error_data.get("error", {}).get("message", "Unknown error")
            return f"❌ API Error: {error_msg}"
            
    except requests.exceptions.Timeout:
        return "⏰ Request timed out. Please try again."
    except requests.exceptions.ConnectionError:
        return "🔌 Connection error. Check your internet connection."
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Alternative: Simple echo bot for testing without API
def echo_bot_response(messages):
    """Simple echo bot - no API needed"""
    last_message = messages[-1]["content"]
    return f"You said: '{last_message}'\n\n(This is an echo response. Add your API key to get real AI responses.)"

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat
    st.session_state.messages.append({
        "role": "user",
        "content": prompt,
        "timestamp": datetime.now().strftime("%H:%M")
    })
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get and display bot response
    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            if API_KEY == "YOUR_OPENROUTER_API_KEY":
                # Use echo bot for testing
                response = echo_bot_response(st.session_state.messages)
            else:
                # Use real API
                response = get_bot_response(st.session_state.messages)
        
        st.markdown(response)
    
    # Add bot response to history
    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "timestamp": datetime.now().strftime("%H:%M")
    })

# ============================================
# FOOTER
# ============================================

st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.caption(f"💬 Messages: {len(st.session_state.messages)}")
with col2:
    st.caption(f"🎛️ Model: {st.session_state.model}")
with col3:
    st.caption(f"🌡️ Temperature: {st.session_state.temperature}")
