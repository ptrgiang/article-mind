import google.generativeai as palm
from newspaper import Article


def extract_text_from_url(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text


def generate_summary(text):
    response = palm.generate_text(prompt=f"Summarize this article: \n{text}")
    return response.result


# Function for chat interaction
def chat_about_article(article_text, chat_input):
    # Create a new conversation
    response = palm.chat(
        messages=f"Here is the article: \n{article_text} \nPlease answer my questions. Wait until my first reply. You should respond 'How can I help you?'"
    )
    response = response.reply(f"{chat_input}")
    return response.last
