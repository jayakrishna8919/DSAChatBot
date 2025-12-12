DSA Chatbot – README
Overview
--------
This project is a DSA (Data Structures & Algorithms) Chatbot built using:

Streamlit (UI)

Ollama + Llama model (LLM backend)

Python

JSON-structured responses

The chatbot answers only DSA-related questions.
If a user asks a non-DSA question, it replies with:

"IM DSA Chatbot I can help out you only DSA Concepts"

Features
----------
Understands and answers DSA questions clearly.

Gives examples and Python snippets for each concept.

Returns responses in clean JSON format.

Maintains chat history using Streamlit session state.

Filters non-DSA questions.

Greets users for greeting queries.

Project Structure
app.py               # Main Streamlit chatbot code
.env                 # Environment variables (Optional)

Technologies Used
---------------
Python
Streamlit
Ollama (local LLM engine)
Llama3.2 model
dotenv
JSON

How It Works
------------
1. Prompt Design

A detailed system prompt defines the chatbot’s behavior:

Act as a senior DSA lecturer

Only answer DSA topics

Output strictly in JSON format

Provide examples + Python code

2. User Query Flow

User enters a question.

The prompt inserts the question (__QUESTION__).

Model generates a JSON response.

Code extracts and cleans the JSON.

Streamlit displays the chatbot’s reply.

JSON Output Format
-------------------

The model must return a response like:

{
  "Question": "...",
  "Description": "...",
  "Explanation": "...",
  "Examples": "..."
}


All values are strings.

Run the App
------------
1. Install dependencies
pip install streamlit python-dotenv ollama

2. Start Ollama model
ollama pull llama3.2

3. Run Streamlit app
streamlit run app.py

🧩 Key Functionality
✔ Processing model output

The function:

get_ollama_response(inp)


Sends prompt to Llama model

Extracts pure JSON from model output

Returns Python dictionary

✔ Chat memory
st.session_state["messages"]


Stores user and bot messages.

✔ UI

Text area for input

"Send" button

Display chat history
