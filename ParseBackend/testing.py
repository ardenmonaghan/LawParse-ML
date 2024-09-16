from pdf_parser import PDFParser
from vector_database import VectorDatabase


if __name__ == "__main__":
    parser = PDFParser()
    pages = parser.load_pdf("pdfs/ExampleClaim.pdf")

    assert len(pages) > 0
    print("Pages is not empty, loaded successfully")
    print("Number of pages: ", len(pages))

    assert pages[0].page_content is not None
    print("Page has content, as expected")

    # chunks = list[Document]
    chunks = parser.split_text(pages)
    assert len(chunks) > 0
    print("Chunks is not empty, split successfully")
    print("Number of chunks: ", len(chunks))

    example_chunk = chunks[0]
    assert example_chunk.metadata is not None
    print("Chunk has metadata, as expected")
    # rint(example_chunk.metadata)

    assert example_chunk.page_content is not None
    print("Chunk has content, as expected")
    # print(chunks[0].page_content)

    # Chunk ID creation
    chunks = parser.chunk_id_creation(chunks)
    # for chunk in chunks:
    #     print(chunk.metadata)
    print("Chunk ID creation successful, len(chunks): ", len(chunks))

    # Vector Database creation
    vector_db = VectorDatabase()
    vector_db.create_vector_database(chunks)
    print("Vector Database created successfully")
