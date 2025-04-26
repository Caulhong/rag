from retriever import init_vector_store, add_docs_to_store
from rag_pipeline import rag_ask
from utils import load_documents

if __name__ == "__main__":
    # 初始化向量数据库
    vector_store = init_vector_store()

    # 加载文档并插入向量库
    documents = load_documents("./docs")
    add_docs_to_store(documents, vector_store)

    print("RAG 文档问答助手已启动。输入 'exit' 退出。")
    while True:
        query = input("请输入你的问题：")
        if query.lower() == "exit":
            break
        answer = rag_ask(query)
        print("回答：", answer)