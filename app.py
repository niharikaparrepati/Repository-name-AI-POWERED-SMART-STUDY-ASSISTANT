import streamlit as st
import requests
import json
import time

# 1. Page Base Properties Setup Architecture
st.set_page_config(
    page_title="Smart Study Assistant Pro",
    page_icon="🎓",
    layout="wide"
)

# Ollama Local Configuration Setup Variables Mapping
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"

def generate_local_response(prompt_text):
    """Local Ollama AI (Llama 3.2) dynamic processing system handler"""
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt_text,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=90)
        if response.status_code == 200:
            return response.json().get("response", "No response received.")
        else:
            return f"❌ Ollama Error: Status code {response.status_code}. Make sure Ollama application is active."
    except requests.exceptions.ConnectionError:
        return "❌ Local Processing Error: Could not connect to Ollama instance. Please check if the Ollama application is running and Llama 3.2 model is pulled locally."

# Initialize Session State Safely to handle page routing actions without duplicate variables errors
if "page_selection" not in st.session_state:
    st.session_state["page_selection"] = "AI Question & Answer"

# 2. Page Header Visual Anchors Banner Panels Layout Showcase
st.title("🎓 AI-Powered Smart Study Assistant Pro")
st.caption("🔒 Secured Enterprise Architecture — Local AI Processing Enabled via Ollama & Llama 3.2")

# 📊 Dashboard Quick Stats Metrics Row Panels Showcase Setup
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric(label="✨ Active AI Node Core", value="Llama 3.2", delta="Local Processing")
with col_m2:
    st.metric(label="📊 Selected Framework Mode", value="All-In-One Pro", delta="Active Panel Loops")
with col_m3:
    st.metric(label="⏱️ Productivity Engine", value="Multi-Tasking Engine", delta="Live Counters")

st.markdown("---")

# 3. 🎨 Clean Visual Anchors Custom Sidebar Buttons Router Panel
with st.sidebar:
    st.header("⚙️ Feature Navigation")
    st.write("Click a separate panel below directly:")
    
    # Custom functional states trigger directly updating structural key dictionary values securely
    if st.button("🤖 AI Question & Answer", use_container_width=True, key="side_nav_qa"):
        st.session_state["page_selection"] = "AI Question & Answer"
        
    if st.button("📚 Topic Explanation", use_container_width=True, key="side_nav_topic"):
        st.session_state["page_selection"] = "Topic Explanation"
        
    if st.button("📝 Study Material Summarization", use_container_width=True, key="side_nav_sum"):
        st.session_state["page_selection"] = "Study Material Summarization"
        
    if st.button("🧠 AI Quiz Generator", use_container_width=True, key="side_nav_quiz"):
        st.session_state["page_selection"] = "AI Quiz Generator"
        
    if st.button("📋 Flashcard Deck Maker", use_container_width=True, key="side_nav_fc"):
        st.session_state["page_selection"] = "Flashcard Deck Maker"
        
    if st.button("🕒 Study Pomodoro Timer", use_container_width=True, key="side_nav_timer"):
        st.session_state["page_selection"] = "Study Pomodoro Timer"
        
    if st.button("📝 Personal Study Notes Manager", use_container_width=True, key="side_nav_notes"):
        st.session_state["page_selection"] = "Personal Study Notes Manager"
    
    st.markdown("---")
    st.header("📖 Learning Level Settings")
    learning_level = st.radio(
        "Student Explanation Framework Level:",
        ["Beginner (Simple words & Analogies)", "Intermediate (Standard)", "Advanced (Deep Technical View)"],
        key="side_learning_radio"
    )
    
    st.markdown("---")
    st.caption("⚡ Developed with Streamlit components and local processing safety protocols.")

# 4. Feature Execution Main Interface Router Blocks Configuration Output System
current_panel = st.session_state["page_selection"]

st.info(f"📍 Active Feature Mode Screen: **{current_panel}**")

if current_panel == "AI Question & Answer":
    st.subheader("🤖 AI Question & Answer Portal")
    st.write("Enter your question below to receive custom detailed breakdowns directly from the AI Node workflow.")
    user_q = st.text_input("Enter your question:", placeholder="Example: What is inheritance in Java?", key="field_user_qa_input")
    
    if st.button("Get AI Answer", key="action_trigger_btn_qa"):
        if user_q:
            prompt = f"System Instruction: Respond according to the student level: {learning_level}.\nQuestion: {user_q}"
            with st.spinner("🧠 Local Llama 3.2 generating response..."):
                ans = generate_local_response(prompt)
                st.success("Generated Response Summary:")
                st.write(ans)
        else:
            st.warning("Please type a question first!")

elif current_panel == "Topic Explanation":
    st.subheader("📚 Complex Topic Explainer System")
    topic = st.text_input("Enter difficult topic:", placeholder="Example: Quantum Computing or Recursion", key="field_topic_explainer_input")
    
    if st.button("Explain Topic", key="action_trigger_btn_topic"):
        if topic:
            prompt = f"Explain the topic '{topic}' in simple language with clean structural examples and breakdown key points. Keep the targeting style tailored for a {learning_level} student level framework."
            with st.spinner("📚 Structuring detailed concept breakdown..."):
                explanation = generate_local_response(prompt)
                st.success("Topic Analysis Framework Details:")
                st.write(explanation)
        else:
            st.warning("Please enter a topic name!")

elif current_panel == "Study Material Summarization":
    st.subheader("📝 Text Summarizer Profile System")
    text_to_sum = st.text_area("Paste long study notes/text files below:", height=250, placeholder="Paste details here...", key="field_summarizer_textarea")
    
    if st.button("Generate Smart Summary", key="action_trigger_btn_sum"):
        if text_to_sum:
            prompt = f"Analyze the following study material and generate an objective, concise summary listing all critical points. Tailor the formatting style for a {learning_level} mindset:\n\n{text_to_sum}"
            with st.spinner("⚡ Extracting key notes context..."):
                summary = generate_local_response(prompt)
                st.success("Summary Content Breakdown:")
                st.write(summary)
        else:
            st.warning("Please paste some content first!")

elif current_panel == "AI Quiz Generator":
    st.subheader("🧠 Custom Quiz Generator Module Panel")
    quiz_topic = st.text_input("Enter target topic for Quiz:", placeholder="Example: Photosynthesis, Data Structures", key="field_quiz_topic_input")
    
    if st.button("Generate Multiple Choice Quiz", key="action_trigger_btn_quiz"):
        if quiz_topic:
            prompt = f"Generate 4 multiple-choice questions (MCQs) for the topic '{quiz_topic}'. Keep the complexity standard aligned for a {learning_level} level user profile. Clearly provide the option parameters and separate the list of correct answers at the absolute bottom endpoint cleanly."
            with st.spinner("🧠 Processing custom test suite items..."):
                quiz_output = generate_local_response(prompt)
                st.success("Generated Test Paper Structure Parameters:")
                st.write(quiz_output)
        else:
            st.warning("Please name a specific topic parameters area!")

elif current_panel == "Flashcard Deck Maker":
    st.subheader("📋 Flashcard Deck Maker Engine")
    st.write("Convert complex conceptual parameters data fields into easy-to-read retention flashcard systems.")
    fc_topic = st.text_input("Enter Flashcard Core Topic area:", placeholder="Example: Git commands or Chemistry Periodic elements", key="field_flashcard_topic_input")
    
    if st.button("Build Revision Flashcards", key="action_trigger_btn_fc"):
        if fc_topic:
            prompt = f"Generate 5 quick study revision flashcards for the topic '{fc_topic}' matching student level format '{learning_level}'. For each flashcard, format strictly as:\n- **Front (Concept/Question)**: ...\n- **Back (Answer/Explanation)**: ..."
            with st.spinner("📋 Local Llama engine drafting flashcard points..."):
                fc_output = generate_local_response(prompt)
                st.success("Revision Cards Configuration Output:")
                st.markdown(fc_output)
        else:
            st.warning("Please mention a topic to generate cards!")

elif current_panel == "Study Pomodoro Timer":
    st.subheader("🕒 Study Pomodoro Focus Timer")
    st.write("Time track productivity workspace panels helper setup tracking loops.")
    
    timer_duration = st.number_input("Set Focus Time Duration Length (Minutes):", min_value=1, max_value=60, value=25, key="field_pomodoro_duration_counter")
    
    if st.button("Start Focus Session Counter", key="action_trigger_btn_timer"):
        st.info(f"🚀 Session active! Focus your target assignments continuously for {timer_duration} minutes.")
        progress_bar = st.progress(0)
        
        total_seconds = timer_duration * 60
        for i in range(100):
            time.sleep(total_seconds / 100)
            progress_bar.progress(i + 1)
            
        st.success("🎉 Focus block completed successfully! Great job! Take a short break now.")

elif current_panel == "Personal Study Notes Manager":
    st.subheader("📝 Personal Study Notes Manager Workspace")
    st.write("Manage your lecture documentation items, structural reference points, and local dynamic downloads from this system dashboard panel.")
    
    notes_title = st.text_input("Notes Subject/Topic Title:", placeholder="Example: Java Lecture 1 Notes", key="field_notes_title_textbox")
