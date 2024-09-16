from langchain_community.llms import Ollama
from embedding_functions.embedding_function import get_embedding_function
from langchain_community.vectorstores import Chroma
from langchain.schema.document import Document


class VersionControlModel:
    def __init__(self):
        self.CHROMA_PATH = "versions/version_control_chroma_db"

        # Accessing specific database versions

    def create_version_control_database(self, chunks_with_ids: list[Document]):
        pass
