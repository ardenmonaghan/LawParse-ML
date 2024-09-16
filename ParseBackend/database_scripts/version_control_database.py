# Meant for controlling different versions of the pdf files uploaded by the user for a specific claim. This will be a section where
# the user will have multiple options to upload new versions of the pdf file, delete the current version, restore a previous version, etc.

# Main use is to generally specify the differences between the versions and to keep track of the changes.

class VersionControlDatabase:
    def __init__(self):
        self.CHROMA_PATH = "version_control_chroma_db"

    def create_version_control_database(self, chunks_with_ids: list[Document]):
        '''for databases that require version control, and multiple databases to be created and handle differences between files'''
        pass
