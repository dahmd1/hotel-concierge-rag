from langchain_text_splitters import RecursiveCharacterTextSplitter
import pandas as pd
def chunk_pages(pages, chunk_size=500, chunk_overlap=100) -> pd.DataFrame:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = pages["text"].tolist()
    metadatas = [{"page_number": pn} for pn in pages["page_number"]]
    documents = text_splitter.create_documents(texts, metadatas=metadatas)
    rows = []
    for chunk_id, doc in enumerate(documents):
        rows.append({
            "chunk_id": chunk_id,
            "page_number": doc.metadata["page_number"],
            "text": doc.page_content,
            "word_count": len(doc.page_content.split()),
        })

    chunks = pd.DataFrame(rows)
    return chunks

def filter_chunks(chunks: pd.DataFrame, min_words: int = 8) -> pd.DataFrame:
    chunks = chunks[chunks["word_count"] >= min_words]
    chunks = chunks.reset_index(drop=True)
    return chunks 