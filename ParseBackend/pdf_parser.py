from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document


class PDFParser:
    def __init__(self):
        self.pdf_path = None

    def load_pdf(self, pdf_path: str) -> list[Document]:
        '''loads the pdf document and returns a list with all the pages as documents'''
        self.pdf_path = pdf_path

        loader = PyMuPDFLoader(self.pdf_path)
        pages = loader.load()
        # page content, text content -metadata (page number and source)
        return pages

    def split_text(self, documents: list[Document]) -> list[Document]:
        '''splits the documents into more chunks of text for better processing'''

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800, chunk_overlap=80, length_function=len, is_separator_regex=False)

        return text_splitter.split_documents(documents)

    # sourcepath, page number, chunk number
    # ex) pdfs/ExampleClaim.pdf, 1, 1

    def chunk_id_creation(self, chunks: list[Document]) -> list[Document]:
        current_page_number = 1
        current_chunk_index = 0

        for chunk in chunks:
            source = chunk.metadata['source']
            page = chunk.metadata['page']
            if current_page_number == page:
                current_chunk_index += 1
            else:
                current_chunk_index = 0
                current_page_number = page

            chunk_id = f"{source}-{page}:{current_chunk_index}"
            chunk.metadata['chunk_id'] = chunk_id

        return chunks


if __name__ == "__main__":
    parser = PDFParser()
    pages = parser.load_pdf("pdfs/ExampleClaim.pdf")
    print(pages[1])
    print("--------------------------------")

    chunks = parser.split_text(pages)
    print(chunks[4])
