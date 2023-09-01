import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as palm
from module import extract_text_from_url, generate_summary, chat_about_article
from design import apply_design
from feedback_form import save_feedback


def main():
    load_dotenv()

    # palm.configure(api_key=os.getenv("PALM_API_KEY"))  # run_locally
    palm.configure(api_key=st.secrets["PALM_API_KEY"]) # deploy_on_streamlit

    # Set up page configuration
    st.set_page_config(
        page_title="Article Mind: Harnessing AI for Rapid Article Insights",
        page_icon="🚀",
        layout="wide",
    )

    # Introductory section
    st.write(" ")
    st.markdown(
        "<h1 style='text-align: center; color: white; font-size:35px;'>Welcome to Article Mind!</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h3 style='text-align: center; font-size:56px;'<p>📰</p></h3>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h3 style='text-align: center; color: grey; font-size:20px;'>Unleash the power of AI for instant article summaries and chat interactions</h3>",
        unsafe_allow_html=True,
    )
    st.markdown("___")

    # Apply design elements
    custom_css, background_css, sun_icon, moon_icon = apply_design()

    # Sidebar for options
    st.sidebar.title("Options")
    selected_option = st.sidebar.radio("", ["Chat", "Summarize"])

    if selected_option == "Chat":
        st.header("Chat with AI")
        st.write(" ")
        article_url = st.text_input("Enter Article URL for context:")
        chat_input = st.text_input("Ask any question about this article:")
        if st.button("Chat"):
            if article_url and chat_input:
                try:
                    with st.spinner("Loading..."):
                        article_text = extract_text_from_url(article_url)
                        chat_response = chat_about_article(article_text, chat_input)
                    st.write(chat_response, unsafe_allow_html=True)
                except:
                    st.write(
                        "This article is not available to chat.", unsafe_allow_html=True
                    )

    if selected_option == "Summarize":
        st.header("Summarize Article")
        st.write(" ")
        article_url = st.text_input("Enter Article URL:")

        if st.button("Summarize"):
            if article_url:
                try:
                    with st.spinner("Summarizing..."):
                        article_text = extract_text_from_url(article_url)
                        summary = generate_summary(article_text)
                    st.write(summary, unsafe_allow_html=True)
                except:
                    st.write(
                        "This article is not available to summarize.",
                        unsafe_allow_html=True,
                    )

    # Feedback Form
    st.write("---")
    st.write("Feedback Form")
    st.write(" ")

    # Input fields
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    feedback = st.text_area("Your Feedback", max_chars=500)

    # Submit button
    if st.button("Submit"):
        if name and email and feedback:
            save_feedback(name, email, feedback)
            st.success("Thank you for your feedback!")

    # Footer
    st.write("---")
    st.write("Contact Information")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("**Email: work.trgiangpham@gmail.com**", icon="📧")
    with c2:
        st.info(
            "**GitHub: [github.com/ptrgiang](https://github.com/ptrgiang)**",
            icon="🖥️",
        )
    with c3:
        st.info(
            "**LinkedIn: [Truong Giang Pham](https://linkedin.com/in/trgiang-pham)**",
            icon="🔗",
        )

    st.write("---")
    st.write("© 2023 Article Mind. All rights reserved.")

    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
