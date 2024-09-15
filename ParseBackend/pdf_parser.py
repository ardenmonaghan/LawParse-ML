from langchain_community.document_loaders import PyMuPDFLoader
# from langchain_community.text_splitter import CharacterTextSplitter


class PDFParser:
    def __init__(self):
        self.pdf_path = None

    def load_pdf(self, pdf_path: str):
        self.pdf_path = pdf_path

        loader = PyMuPDFLoader(self.pdf_path)
        pages = loader.load_and_split()
        print(pages[1].page_content)

    def split_text(self, text: str):
        pass


if __name__ == "__main__":
    parser = PDFParser()
    parser.load_pdf("pdfs/ExampleClaim.pdf")
