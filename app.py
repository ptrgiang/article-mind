import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as palm
from module import extract_text_from_url, generate_summary, chat_about_article
from design import apply_design


def main():
    load_dotenv()

    palm.configure(api_key=os.getenv("PALM_API_KEY"))

    # Set up page configuration
    st.set_page_config(
        page_title="Article Mind: Harnessing AI for Rapid Article Insights",
        layout="wide",
    )

    # Introductory section
    st.title("Welcome to Article Mind")
    st.write(
        "Unleash the power of AI for instant article summaries and chat interactions."
    )

    # Apply design elements
    custom_css, background_css, sun_icon, moon_icon = apply_design()

    # Sidebar for options
    st.sidebar.title("Options")
    selected_option = st.sidebar.radio("", ["Chat", "Summarize"])

    if selected_option == "Chat":
        st.header("Chat with AI")
        article_url = st.text_input("Enter Article URL for context:")
        chat_input = st.text_input("Ask any question about this article:")
        if st.button("Chat"):
            if article_url and chat_input:
                try:
                    article_text = extract_text_from_url(article_url)
                    chat_response = chat_about_article(article_text, chat_input)
                    st.write(chat_response, unsafe_allow_html=True)
                except:
                    st.write(
                        "This article is not available to chat.", unsafe_allow_html=True
                    )

    if selected_option == "Summarize":
        st.header("Summarize Article and PDF file")
        article_url = st.text_input("Enter Article URL:")

        if st.button("Summarize"):
            if article_url:
                try:
                    article_text = extract_text_from_url(article_url)
                    summary = generate_summary(article_text)
                    st.subheader("Generated Summary:")
                    st.write(summary, unsafe_allow_html=True)
                except:
                    st.write(
                        "This article is not available to summarize.",
                        unsafe_allow_html=True,
                    )

    # Footer
    st.write("---")
    st.write("Contact Information:")
    st.write("📧 Email: work.trgiangpham@gmail.com")
    st.write("🌐 GitHub: [https://github.com/ptrgiang](https://github.com/ptrgiang)")
    st.write(
        "🔗 LinkedIn: [linkedin.com/in/trgiang-pham](https://linkedin.com/in/trgiang-pham)"
    )
    st.write("© 2023 ArticleMind. All rights reserved.")


if __name__ == "__main__":
    main()
