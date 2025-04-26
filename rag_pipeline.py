from retriever import get_relevant_docs
from llm_wrapper import ask_llm

def rag_ask(query):
    docs = get_relevant_docs(query)
    context = "\n".join([doc.page_content for doc in docs])
    print(context)
    prompt = f"基于以下内容回答问题：\n{context}\n\n问题：{query}"
    return ask_llm(prompt)