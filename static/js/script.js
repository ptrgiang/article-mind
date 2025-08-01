import { GoogleGenerativeAI } from "https://esm.run/@google/generative-ai";

document.addEventListener('DOMContentLoaded', () => {
    console.log("DOM fully loaded and parsed.");

    const loadArticleBtn = document.getElementById('load-article-btn');
    const articleUrlInput = document.getElementById('article-url');
    const apiKeyInput = document.getElementById('api-key-input');
    const loadingDiv = document.getElementById('loading');
    const contentWrapper = document.getElementById('content-wrapper');
    const summaryContentDiv = document.getElementById('summary-content');
    const chatHistoryDiv = document.getElementById('chat-history');
    const chatInput = document.getElementById('chat-input');
    const sendChatBtn = document.getElementById('send-chat-btn');

    let genAI;
    let chatSession;
    let articleText = '';

    apiKeyInput.addEventListener('change', () => {
        const apiKey = apiKeyInput.value;
        console.log("API Key entered.");
        if (apiKey) {
            sessionStorage.setItem('gemini-api-key', apiKey);
            try {
                genAI = new GoogleGenerativeAI(apiKey);
                console.log("GoogleGenerativeAI initialized successfully.");
            } catch (e) {
                alert("Invalid API Key provided.");
                console.error("Error initializing GoogleGenerativeAI:", e);
            }
        }
    });

    loadArticleBtn.addEventListener('click', async () => {
        console.log("Load Article button clicked.");
        const articleUrl = articleUrlInput.value;
        const apiKey = sessionStorage.getItem('gemini-api-key');

        if (!apiKey) {
            alert('Please enter your Gemini API Key.');
            console.error("API Key is missing.");
            return;
        }

        if (!articleUrl) {
            alert('Please enter a URL.');
            console.error("Article URL is missing.");
            return;
        }

        console.log(`API Key: ${apiKey ? 'Loaded' : 'Missing'}, URL: ${articleUrl}`);

        loadingDiv.classList.remove('hidden');
        contentWrapper.classList.add('hidden');
        loadArticleBtn.disabled = true;
        articleUrlInput.disabled = true;

        try {
            console.log("Fetching HTML from Google Apps Script...");
            const fetchResponse = await fetch('https://script.google.com/macros/s/AKfycbwfC1QxFQ7GGwoULndpJ9d9xPtA4v18_qjph_9AJPcSYYG-4XC0nBjllha-2TQhezjVJA/exec', {
                redirect: "follow",
                method: 'POST',
                headers: { 'Content-Type': 'text/plain;charset=utf-8' },
                body: JSON.stringify({ url: articleUrl})
            });
            console.log("Fetch response status:", fetchResponse.status);
            if (!fetchResponse.ok) {
                throw new Error(`Failed to fetch article: ${fetchResponse.statusText}`);
            }
            const responseData = await fetchResponse.json();
            if (!responseData.success) {
                throw new Error(responseData.error);
            }
            const htmlText = responseData.html;
            console.log(htmlText);
            console.log("HTML content fetched.");

            const parser = new DOMParser();
            const doc = parser.parseFromString(htmlText, 'text/html');
            doc.querySelectorAll('script, style').forEach(elem => elem.remove());
            articleText = doc.body.textContent || "";
            const lines = articleText.split(/\r?\n/).map(line => line.trim()).filter(line => line.length > 0);
            articleText = lines.join('\n');
            console.log("Article text extracted:", articleText.substring(0, 200) + "...");

            if (!articleText) {
                throw new Error("Could not extract text from the article.");
            }

            console.log("Generating summary...");
            const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash"});
            const summaryPrompt = `Please provide a concise, easy-to-understand summary of the following article. Use markdown to highlight important keywords and phrases with bold formatting.:\n\n--- ARTICLE ---\n\n${articleText}\n\n--- END ARTICLE ---`;
            const summaryResult = await model.generateContent(summaryPrompt);
            const summaryResponse = await summaryResult.response;
            const summaryText = summaryResponse.text();
            console.log("Summary generated.");

            const converter = new showdown.Converter();
            const summaryHtml = converter.makeHtml(summaryText);
            summaryContentDiv.innerHTML = summaryHtml;
            contentWrapper.classList.remove('hidden');

            console.log("Starting chat session...");
            chatSession = model.startChat({ history: [] });
            appendMessage('assistant', 'The summary is ready. You can now ask me anything about the article.');
            console.log("Chat session started.");

        } catch (error) {
            alert(`An error occurred: ${error.message}`);
            console.error("Error during article processing:", error);
        } finally {
            loadingDiv.classList.add('hidden');
            loadArticleBtn.disabled = false;
            articleUrlInput.disabled = false;
            console.log("Processing finished.");
        }
    });

    sendChatBtn.addEventListener('click', handleChat);
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            handleChat();
        }
    });

    async function handleChat() {
        const prompt = chatInput.value;
        if (!prompt || !chatSession) {
            return;
        }

        appendMessage('user', prompt);
        chatInput.value = '';
        appendMessage('assistant', '<div class="loader"></div>');

        try {            const fullContext = `Based on this article:\n${articleText}\n\nAnswer this question:\n${prompt}`;            const result = await chatSession.sendMessage(fullContext);            const response = await result.response;            const text = response.text();            const converter = new showdown.Converter();            const html = converter.makeHtml(text);            const lastMessage = chatHistoryDiv.querySelector('.assistant-message:last-child .message-content');            lastMessage.innerHTML = html;        } catch (error) {
            const lastMessage = chatHistoryDiv.querySelector('.assistant-message:last-child .message-content');
            lastMessage.innerHTML = `<p class="text-red-500">An error occurred. Please try again.</p>`;
            console.error("Chat error:", error);
        }
        chatHistoryDiv.scrollTop = chatHistoryDiv.scrollHeight;
    }

    function appendMessage(role, content) {
        const messageWrapper = document.createElement('div');
        messageWrapper.classList.add('message', `${role}-message`, 'mb-4', 'flex');

        const messageContent = document.createElement('div');
        messageContent.classList.add('message-content', 'p-3', 'rounded-lg', 'max-w-2/3');
        messageContent.innerHTML = content;

        if (role === 'user') {
            messageWrapper.classList.add('justify-end');
            messageContent.classList.add('bg-black', 'text-white');
        } else {
            messageWrapper.classList.add('justify-start');
            messageContent.classList.add('bg-gray-200', 'text-black');
        }
        
        messageWrapper.appendChild(messageContent);
        chatHistoryDiv.appendChild(messageWrapper);
        chatHistoryDiv.scrollTop = chatHistoryDiv.scrollHeight;
    }
});