import streamlit as st
from llm import generate_response

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="PeacePal - Mental Health Companion",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- 2. SIDEBAR ---
with st.sidebar:
    st.title("About PeacePal 🌿")
    st.markdown("""
    **PeacePal** is a safe, AI-driven mental health companion. 
    
    Designed specifically for students facing stress and anxiety, it provides a judgment-free space to share your feelings. PeacePal listens to your thoughts and offers empathetic, motivational support and relaxation tips to help manage your well-being.
    """)
    
    st.markdown("---")
    if st.button("🗑️ Clear Conversation", type="primary"):
        st.session_state.messages = []
        st.rerun()

# --- 3. MAIN INTERFACE ---
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
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar="🌿" if message["role"] == "assistant" else "👤"):
            st.markdown(message["content"])

# --- 4. INPUT HANDLING ---
if user_input := st.chat_input("Share what's on your mind..."):
    
    # Add User Message to State & Display
    st.session_state.messages.append({"role": "user", "content": user_input})
    with chat_container:
        with st.chat_message("user", avatar="👤"):
            st.markdown(user_input)

    # Generate Response
    with chat_container:
        with st.chat_message("assistant", avatar="🌿"):
            with st.spinner("PeacePal is listening..."):
                response = generate_response(user_input)
                st.markdown(response)
    
    # Add AI Message to State
    st.session_state.messages.append({"role": "assistant", "content": response})