from dotenv import load_dotenv
import os
import ollama
import json
import streamlit as st
# from langchain_groq import ChatGroq
load_dotenv()

prompt1= """
you are an experienced in DSA concepts.You can answer the the questions in seconds.
if the question is an greeting ,then you shoud greet him politely and ask for dsa question.
If the question is non DSA question.Then you need to give the response "I am a DSA related chatbot,Ask those questions"
question ={ques}
"""


prompt1="""
Role:
You are a senior lecturer with highly knowledgable in Data Structures and Algorithms where you will be teaching students with Data Structures and Algorithms (DSA).
---
Task:
Your job is to analyze the input Query and answer the query which is related to DSA.
----
Instructions:
- Only answer to the questions related to Data structures and algorithms.
- If input Query is NON DSA query then stricly give the statement As follows:"IM DSA Chatbot I can help out you only DSA Concepts".
- For each explaination have an example and python snippets.
- Ensure that the concept explanation should understand to people who are technical and non technical.
- The explanation should be consise and clear.
- Ensure that the response key-value pairs should be strings.
- Ensure that ALL values in the JSON are strings (no null, no None).
---
<INPUT>
__QUESTION__
<INPUT>
---
Output format:
You MUST respond with ONLY a valid JSON object. No markdown, no backticks, no extra text.
Your response MUST contain only the JSON object.
```json
{
  'Question':<INPUT>,
  'Description':<DESCRIPTION>,
  'Explanation':<EXPLANTION>,
  'Examples':<EXAMPLES>
}

```
---
"""

def get_ollama_response(inp:str):
    # model = os.getenv("OLLAMA_MODEL")
    model = "llama3.2"
    response = ollama.chat(model=model, messages=[
    {
        'role': 'user',
        'content': inp,
    },
])
   
    response = response.message.content
    if "{" not in response and "}" not in response:
          return response
    print(response,type(response))
    response=response.replace("```","")
    response=response.strip("```")
    start = response.find("{")
    end = response.rfind("}") + 1

    if start == -1 or end == -1:
        raise ValueError("Could not find JSON object in model response")

    json_str = response[start:end]
    # print("JSON STRING::", json_str)
    response_dict = json.loads(json_str)
    return response_dict
  
if "messages" not in st.session_state:
  st.session_state["messages"]=[]

for msg in st.session_state["messages"]:
      role = "You" if msg["role"]=="user" else "Bot"
      st.write(f"**{role}:**{msg['content']}")


st.set_page_config(page_title="AI DSA Chatbot")
st.header("DSA Chatbot")
# st.title("DSA Chatbot")
input_text = st.text_area("Query", key= "input")

if input_text:
      st.session_state["messages"].append({"role":"user","content":input_text})


submit = st.button("send")
if submit:
    # inp_str = input("YOU::")
    # if inp_str.lower()=="exit":
    #     break
    
    formatted_prompt = prompt1.replace("__QUESTION__",input_text)
    response = get_ollama_response(formatted_prompt)
    st.session_state["messages"].append({"role":"bot","content":response})
    
    st.write(response)
    print(f"BOT::{response}")
    
    
     


