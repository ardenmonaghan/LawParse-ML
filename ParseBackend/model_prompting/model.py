from langchain_community.llms import Ollama
from embedding_functions.embedding_function import get_embedding_function
from langchain_community.vectorstores import Chroma
from langchain.schema.document import Document


PROMPT_TEMPLATE = '''
You are a helpful assistant that can answer questions and help with tasks.
Answer the question based only on the following context:
{context}

---
Answer the question based on the anove context. {question}
'''


class LlamaModel:
    def __init__(self):
        self.CHROMA_PATH = "chroma_db"

    def query_RAG(self, query_text: str):

        embedding_function = get_embedding_function()
        db = Chroma(persist_directory=self.CHROMA_PATH,
                    embedding_function=embedding_function)

        results = db.similarity_search_with_score(query_text, 3)

        all_scores = []
        result_text_format = ""
        for doc, score in results:
            all_scores.append(score)
            result_text_format += f"\nScore: {score}\n\n ---- \n\n{doc.page_content}"

        return result_text_format, all_scores

    def ollama_Generate_Answer(self, query_text: str):
        model = Ollama(model="llama3")
