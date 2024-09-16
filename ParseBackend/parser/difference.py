import PyPDF2
import difflib


class VersionControlParser:
    def __init__(self):
        pass

    def extract_text_from_pdf(self, pdf_path: str):
        pdf_reader = PyPDF2.PdfReader(pdf_path)
        text = ''
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text

    def compare_texts(self, text1, text2):
        text1_lines = text1.splitlines()
        text2_lines = text2.splitlines()
        diff = difflib.unified_diff(
            text1_lines, text2_lines, fromfile='file1.pdf', tofile='file2.pdf', lineterm='')
        return '\n'.join(diff)


if __name__ == "__main__":
    parser = VersionControlParser()
    pdf1_text = parser.extract_text_from_pdf(
        "../pdf_version_control/doc1.pdf")
    pdf2_text = parser.extract_text_from_pdf(
        "../pdf_version_control/doc2.pdf")

    diff_result = parser.compare_texts(pdf1_text, pdf2_text)
    print(diff_result)
