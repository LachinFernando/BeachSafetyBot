import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Beach Safety Hazards Chatbot",
    page_icon="🏖️",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f1f5f9;
    }
    .stMarkdown {
        color: #f1f5f9;
    }
    h1, h2, h3 {
        color: #f1f5f9 !important;
    }
</style>
""", unsafe_allow_html=True)

# Header with emoji
st.title("🏖️ Beach Safety Hazards Chatbot")

# Add some spacing
st.markdown("<br>", unsafe_allow_html=True)

# Display beach image (using a placeholder URL - you can replace with your own image)
st.image(
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200&h=400&fit=crop",
    use_container_width=True,
    caption="Stay Safe at the Beach"
)

# Add spacing
st.markdown("<br>", unsafe_allow_html=True)

# About section
st.header("🌊 What is this about?")

st.markdown("""
Welcome to the **Beach Safety Hazards Chatbot** - your intelligent companion for beach safety information!

This chatbot is designed to help you:

- 🚨 **Identify potential beach hazards** and understand the risks
- 💡 **Get instant answers** to your beach safety questions
- 🏊 **Learn about water safety**, rip currents, and swimming conditions
- 🐚 **Understand marine life hazards** like jellyfish, stingrays, and more
- ☀️ **Receive sun protection tips** and weather-related safety advice
- 🆘 **Know what to do in emergencies** at the beach

Simply ask any question about beach safety, and our AI-powered chatbot will provide you with 
accurate, helpful information to ensure you have a safe and enjoyable beach experience!
""")

# Call to action
st.markdown("<br>", unsafe_allow_html=True)
st.info("👈 Navigate to the **Chatbot** page from the sidebar to start asking questions!")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Stay safe, stay informed, enjoy the beach! 🌴</p>",
    unsafe_allow_html=True
)
