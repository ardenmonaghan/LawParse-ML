from parser.pdf_parser import PDFParser
from database_scripts.vector_database import VectorDatabase
from model_prompting.model import LlamaModel

if __name__ == "__main__":
    parser = PDFParser()
    pages = parser.load_pdf("pdfs/ExampleClaim.pdf")

    assert len(pages) > 0
    print("Pages is not empty, loaded successfully")
    print("Number of pages: ", len(pages))
    print('--------------------------------')

    assert pages[0].page_content is not None, "Page has no content"
    print("Page has content, as expected")
    print('--------------------------------')

    # chunks = list[Document]
    chunks = parser.split_text(pages)
    assert len(chunks) > 0, "Chunks is empty"
    print("Chunks is not empty, split successfully")
    print("Number of chunks: ", len(chunks))
    print('--------------------------------')

    example_chunk = chunks[0]
    assert example_chunk.metadata is not None, "Chunk has no metadata"
    print("Chunk has metadata, as expected")
    print(example_chunk.metadata)
    print('--------------------------------')

    assert example_chunk.page_content is not None, "Chunk has no content"
    print("Chunk has content, as expected")
    # print(chunks[0].page_content)
    print('--------------------------------')

    # Chunk ID creation
    chunks = parser.chunk_id_creation(chunks)
    assert len(chunks) > 0, "Chunks is empty"
    print("Chunk ID creation successful, len(chunks): ", len(chunks))
    print('--------------------------------')

    # Vector Database creation
    vector_db = VectorDatabase()
    vector_db.create_vector_database(chunks)
    print("Vector Database created successfully")
    print('--------------------------------')

    # Prompting the model with a query
    model = LlamaModel()
    result_text, all_scores = model.query_RAG(
        "Can you tell me about what did the bank do to the plantiff")
    assert result_text is not None, "Result text is empty"
    assert all_scores is not None, "All scores is empty"
    print('--------------------------------')

    result_text = model.ollama_Generate_Answer(
        "Can you tell me when this incident occured ")
    print(result_text)
    print('--------------------------------')

    print("ALL CASES PASSED")
