# Article Mind

Welcome to the Article Mind! This project uses Large Language Models (LLMs) to summarize articles and answer questions based on the provided article URL.

## Features

- **Summarize Articles:** Provide the URL of an article, and AI model will generate a concise summary.
- **Question Answering:** Ask questions related to the article content, and AI model will provide answers.

## Usage

1. **Clone this repository:**

```bash
git clone https://github.com/yourusername/article-mind.git
cd article-mind
```
2. **Obtain your API Key:**

- Join the PaLM API and MakerSuite waitlist at [https://makersuite.google.com/waitlist](https://makersuite.google.com/waitlist).
- Upon acceptance, you can create an API key.

3. **Configure your API Key:**

- Create a `.env` file in the root directory of the project.
- Add a new variable named PALM_API_KEY in the .env file and assign your received API key to it. Your .env file should look like this:

```bash
PALM_API_KEY=your_api_key_here
```

4. **Run the Application with Streamlit:**

```bash
streamlit run app.py
```
  
