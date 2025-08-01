# Article Mind

Welcome to Article Mind! This project uses Large Language Models (LLMs) to summarize articles and answer questions based on a provided article URL. This is a fully client-side application that runs in your browser.

## Features

- **Summarize Articles:** Provide the URL of an article, and the AI model will generate a concise summary.
- **Question Answering:** Ask questions related to the article content, and the AI model will provide answers.

## How It Works

Article Mind is a client-side application, meaning all the processing happens in your browser. Here's a breakdown of the technology:

- **Frontend:** The user interface is built with HTML, CSS, and JavaScript.
- **AI Model:** It uses a large language model for summarization and question answering.
- **Article Fetching:** A Google Apps Script is used as a proxy to fetch the article content from the provided URL to bypass CORS restrictions.

## Usage

1. **Run a local web server:** You need to serve the files using a local web server. A simple way to do this is with Python:
   ```bash
   python -m http.server
   ```
   This will start a server on port 8000.
2. **Open in browser:** Open your web browser and navigate to `http://localhost:8000/`.
3. **Enter API Key:** Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey) and enter it into the API key field at the top of the page.
4. **Load Article:** Paste the URL of an article and click "Load".

That's it! The application will fetch the article, summarize it, and allow you to chat about it, all within your browser.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
