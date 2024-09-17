from langchain_community.llms import Ollama
from embedding_functions.embedding_function import get_embedding_function
from langchain_community.vectorstores import Chroma
from langchain.schema.document import Document

# Meant for controlling different versions of the pdf files uploaded by the user for a specific claim. This will be a section where
# the user will have multiple options to upload new versions of the pdf file, delete the current version, restore a previous version, etc.

# Main use is to generally specify the differences between the versions and to keep track of the changes.

# How to track changes
# chunks will be different between versions, so we can use the chunk_id to track changes.
# new chunks that are not in the previous version, but in the current version, are new chunks that are added.
# chunks that are in the previous version, but not in the current version, are deleted chunks.
# for chunks that are the same between versions, the chunk_id is the same, and the content can be checked if it is the same,
# if the content is the same, we can keep the same chunk_id and update the metadata, such as the version history.

PROMPT_TEMPLATE = '''
YOU ARE A VERSION CONTROL ASSISTANT. YOU WILL BE GIVEN ALL THE CHUNKS FROM TWO VERSIONS OF A PDF FILE.
YOUR JOB IS TO COMPARE THE CHUNKS AND SUMMARIZE THE CHANGES BETWEEN THE TWO VERSIONS.

Whereever you recognize a change in the content of the document, or the meaning between the two versions, you will summarize the changes in the content
and what page that occurs and how it affects the meaning. Just simply state what you notice for differences.

Go through each page one by oneand summarize the changes. If there are not signifigant changes between the two versions, please respond with "No significant changes between the two versions on Page X."

Please state the changes you find in this format

--------------------------------
Here is the first document
--------------------------------
{context}
--------------------------------
Other Document Will be Displayed Below
--------------------------------

{context_two}

'''


class VersionControlModel:
    def __init__(self):
        pass
        # self.path_one = "chroma_databases/" + full_path_one
        # self.path_two = "chroma_databases/" + full_path_two

        # Accessing specific database versions

    def prompt_version_control(self, chunks_with_ids_one: list, chunks_with_ids_two: list):
        context_doc1 = self.retrieve_text_from_chunks(chunks_with_ids_one)
        context_doc2 = self.retrieve_text_from_chunks(chunks_with_ids_two)

        prompt = PROMPT_TEMPLATE.format(
            context=context_doc1, context_two=context_doc2)

        model = Ollama(model="llama3:instruct")
        response = model.invoke(prompt)
        return response

    def retrieve_text_from_chunks(self, chunks_with_ids: list):
        pages_prompting = ''

        for page in chunks_with_ids:
            page_content = page.page_content
            page_number = page.metadata['page']
            pages_prompting += f"\nPage {page_number}:\n\n {page_content}\n\n"
            pages_prompting += "-----\n\n"

        return pages_prompting
