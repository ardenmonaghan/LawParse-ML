from langchain.schema.document import Document
from langchain_community.vectorstores import Chroma
import shutil
import os
from embedding_functions.embedding_function import get_embedding_function


class VectorDatabase:
    def __init__(self, define_path: str):
        # self.CHROMA_PATH = "chroma_db"
        self.CHROMA_PATH = "chroma_databases/" + define_path

     # for each chunk create its embedding and store it in a database'
    def create_vector_database(self, chunks_with_ids: list[Document]):
        '''for databases that require a database to be updated over time'''

        db = Chroma(persist_directory=self.CHROMA_PATH,
                    embedding_function=get_embedding_function())

        existing_items = db.get(include=[])  # IDs are included by default
        existing_ids = set(existing_items['ids'])

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

    def delete_database(self):
        if os.path.exists(self.CHROMA_PATH):
            shutil.rmtree(self.CHROMA_PATH)
