# Meant for controlling different versions of the pdf files uploaded by the user for a specific claim. This will be a section where
# the user will have multiple options to upload new versions of the pdf file, delete the current version, restore a previous version, etc.

# Main use is to generally specify the differences between the versions and to keep track of the changes.

# How to track changes
# chunks will be different between versions, so we can use the chunk_id to track changes.
# new chunks that are not in the previous version, but in the current version, are new chunks that are added.
# chunks that are in the previous version, but not in the current version, are deleted chunks.
# for chunks that are the same between versions, the chunk_id is the same, and the content can be checked if it is the same,
# if the content is the same, we can keep the same chunk_id and update the metadata, such as the version history.

from embedding_functions.embedding_function import get_embedding_function
from langchain_community.vectorstores import Chroma
from langchain.schema.document import Document


class VersionControlDatabase:
    def __init__(self):
        self.CHROMA_PATH = "versions/version_control_chroma_db"

    def create_version_control_database(self, chunks_with_ids: list[Document]):
        '''for databases that require version control, and multiple databases to be created and handle differences between files'''
        pass
