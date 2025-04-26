import faiss
import os
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

index_path = "./vector_store"

def init_vector_store():
    if os.path.exists(index_path):
        return FAISS.load_local(index_path, embedding_model,  allow_dangerous_deserialization=True)
    else:
        sample_docs = [
            Document(page_content="This is a sample document about AI and machine learning."),
        ]
        
        return FAISS.from_documents(sample_docs, embedding_model, allow_dangerous_deserialization=True)

def add_docs_to_store(docs, store):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(docs)
    store.add_documents(chunks)
    store.save_local(index_path)

def get_relevant_docs(query):
    store = FAISS.load_local(index_path, embedding_model, allow_dangerous_deserialization=True)
    return store.similarity_search(query, k=4)