import streamlit as st
import time
from config import LLM_MODEL
from llm import generate_response
# from config import LLM_MODEL  # Uncomment if you have this file
# from llm import generate_response # Uncomment if you have this file

# --- MOCK FUNCTIONS FOR DEMO (Delete these if you have real config/llm files) ---
# LLM_MODEL = "PeacePal-v1"
# def generate_response(prompt):
#     time.sleep(1.5) # Simulate thinking
#     return f"I hear you saying: '{prompt}'. That sounds difficult, but I'm here for you. Tell me more."
# # --------------------------------------------------------------------------------

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="PeacePal - Mental Health Companion",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- 2. CUSTOM CSS (The "Look and Feel") ---
# We inject this CSS to override Streamlit's default harsh white/red colors
# with soothing Greens, Teals, and Soft Greys.
# st.markdown("""
#     <style>
#     /* Main Background - Soft White */
#     .stApp {
#         background-color: #F8F9FA;
#     }
    
#     /* Header Styling */
#     h1 {
#         color: #2E5E4E; /* Deep Calming Green */
#         font-family: 'Helvetica Neue', sans-serif;
#     }
#     h3 {
#         color: #5D8A7B; /* Softer Sage */
#         font-weight: 300;
#     }
    
#     /* Chat Message styling */
#     .stChatMessage {
#         background-color: white;
#         border-radius: 15px;
#         padding: 10px;
#         box-shadow: 0 2px 4px rgba(0,0,0,0.05);
#         margin-bottom: 10px;
#     }
    
#     /* User Message specific override (Streamlit uses distinct classes, but we can target the icon) */
#     .stChatMessage[data-testid="stChatMessage"]:nth-child(odd) {
#         background-color: #E8F5E9; /* Very Light Green for User */
#     }
    
#     /* Sidebar Styling */
#     [data-testid="stSidebar"] {
#         background-color: #E0F2F1; /* Mint Cream */
#         border-right: 1px solid #B2DFDB;
#     }
    
#     /* Input Box Styling */
#     .stTextInput > div > div > input {
#         border-radius: 20px;
#         border: 1px solid #B2DFDB;
#     }
    
#     /* Button Styling */
#     .stButton > button {
#         background-color: #2E5E4E;
#         color: white;
#         border-radius: 20px;
#         border: none;
#         padding: 10px 24px;
#         transition: all 0.3s ease;
#     }
#     .stButton > button:hover {
#         background-color: #1B3E32;
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#     }
#     </style>
# """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3048/3048122.png", width=100) # Optional Logo
    st.title("Settings")
    
    st.info(f"**Model Active:** {LLM_MODEL}")
    st.markdown("---")
    st.markdown("**Crisis Resources:**")
    st.caption("📞 911 (USA) / 112 (India)")
    
    st.markdown("---")
    if st.button("🗑️ Clear Conversation", type="primary"):
        st.session_state.messages = []
        st.rerun()

# --- 4. MAIN INTERFACE ---
st.title("🌿 PeacePal")
st.markdown("### A safe space to share your thoughts.")
st.markdown("---")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant", 
        "content": "Hi there. I'm here to listen without judgment. How are you feeling right now?"
    }]

# Display Chat Messages
# We use a container to keep messages distinct from the input
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar="🌿" if message["role"] == "assistant" else "👤"):
            st.markdown(message["content"])

# --- 5. INPUT HANDLING ---
# Uses st.chat_input which is stuck to the bottom (Better than text_input)
if user_input := st.chat_input("Share what's on your mind..."):
    
    # 1. Add User Message to State & Display
    st.session_state.messages.append({"role": "user", "content": user_input})
    with chat_container:
        with st.chat_message("user", avatar="👤"):
            st.markdown(user_input)

    # 2. Generate Response
    with chat_container:
        with st.chat_message("assistant", avatar="🌿"):
            with st.spinner("PeacePal is listening..."):
                response = generate_response(user_input)
                st.markdown(response)
    
    # 3. Add AI Message to State
    st.session_state.messages.append({"role": "assistant", "content": response})

