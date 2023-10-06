# Welcome to rocinante-icebreaker
Simple repository demoing how to use OpenAI LLM LangChain agents to execute simple chains to "break the ice" with your
friends, family, and colleagues.

## Getting Started

A pre-requisite for this project is to have Python 3.11 installed on your machine, and to have some basic familiarity
with the language. You can find the installation instructions for Python [here](https://www.python.org/downloads/).

1. Clone this repository.
2. Install dependencies.

    ```bash
    pip install -r requirements.txt
    ```

3. Create an account on [OpenAI](https://platform.openai.com/).
4. Copy your OpenAI API key from the OpenAI console.
5. Create an environment variable with the key `OPENAI_API_KEY` and the value of the copied API key.
6. Create an account on [ProxyCurl](https://proxycurl.com/).
7. Copy your ProxyCurl API key from the ProxyCurl console.
8. Create an environment variable with the key `PROXYCURL_API_KEY` and the value of the copied API key.
9. Create an account on [SerpApi](https://serpapi.com/).
10. Copy your SerpApi API key from the SerpApi console.
11. Create an environment variable with the key `SERPAPI_API_KEY` and the value of the copied API key.
12. Create an account on [X](https://twitter.com/).
13. Copy your X API Bearer Token from the X developer console to gain access to the X API v2.
14. Create an environment variable with the key `TWITTER_BEARER_TOKEN` and the value of the copied API key.
15. Run the script.

    ```bash
    python app.py
    ```

16. Go to `http://localhost:5001/` to see the results in your browser of choice. Submit a name to see if it will return
results.

To modify the kind of query you want to run on the document, change the `query` variable in `main.py`. This is intended 
to give a general idea on how you can simply use Pinecone and OpenAI to build a simple search engine for text documents.
