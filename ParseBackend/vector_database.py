from langchain.schema.document import Document
from langchain_community.vectorstores import Chroma
import shutil
import os
from langchain_community.embeddings.ollama import OllamaEmbeddings


class VectorDatabase:
    def __init__(self):
        self.CHROMA_PATH = "chroma_db"
    # for each chunk create its embedding and store it in a database'

    def get_embedding_function(self):
        return OllamaEmbeddings(model="llama3")

    def create_vector_database(self, chunks_with_ids: list[Document]):
        '''for databases that require a database to be updated over time'''

        db = Chroma(persist_directory=self.CHROMA_PATH, embedding_function=self.get_embedding_function(
        ))

        existing_items = db.get(include=[])  # IDs are included by default

        if 'chunk_ids' in existing_items:
            existing_ids = set(existing_items['chunk_ids'])
        else:
            existing_ids = set()

        print(f"Number of existing items: {len(existing_ids)}")

        new_chunks = []
        for chunk in chunks_with_ids:
            if chunk.metadata['chunk_id'] not in existing_ids:
                new_chunks.append(chunk)

        print(f"Number of new chunks: {len(new_chunks)}")

        if len(new_chunks) > 0:
            print("Adding new chunks to the database", {len(new_chunks)})
            new_chunk_ids = [chunk.metadata['chunk_id']
                             for chunk in new_chunks]

            db.add_documents(new_chunks, ids=new_chunk_ids)
            db.persist()

        else:
            print("No new chunks to add")

        def version_control_database(self):
            '''for databases that require version control, and multiple databases to be created and handle differences between files'''
            pass

    def delete_database(self):
        if os.path.exists(self.CHROMA_PATH):
            shutil.rmtree(self.CHROMA_PATH)
