from langchain_community.llms import Ollama


class LlamaModel:
    def __init__(self):
        reponse = ollama.chat(model='llama3.1', messages=[
            {
                'role': 'user',
                'content': "Hello"
            }
        ])
