import os
import fitz  # PyMuPDF
from langchain_community.document_loaders import DirectoryLoader, TextLoader, JSONLoader
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms.ollama import Ollama
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaEmbeddings  # 引入新的 OllamaEmbeddings


# 指定資料夾
data_dir = "data"

if not os.path.exists(data_dir):
    print(f"❌ 資料夾 {data_dir} 不存在，請確認資料夾名稱")
else:
    loader = DirectoryLoader(data_dir, glob="*.*", show_progress=True)

    documents = []

    for filename in os.listdir(data_dir):
        file_path = os.path.join(data_dir, filename)

        if filename.endswith(".json"):
            try:
                json_loader = JSONLoader(file_path=file_path, jq_schema=".[] | {text: .content, metadata: {source: .source}}")
                documents.extend(json_loader.load())
            except Exception as e:
                print(f"❌ JSON 解析失敗 {filename}: {e}")

        elif filename.endswith(".txt") or filename.endswith(".md"):
            try:
                text_loader = TextLoader(file_path)
                documents.extend(text_loader.load())
            except Exception as e:
                print(f"❌ TXT 解析失敗 {filename}: {e}")

        elif filename.endswith(".pdf"):  # **新增 PDF 解析**
            try:
                with fitz.open(file_path) as doc:
                    text = "\n".join([page.get_text("text") for page in doc])
                    documents.append(Document(page_content=text, metadata={"source": file_path}))
            except Exception as e:
                print(f"❌ PDF 解析失敗 {filename}: {e}")

        else:
            print(f"⚠️ 不支援的格式: {filename}")

    print(f"📂 最終成功載入 {len(documents)} 筆文件")

# **1. 拆分文本，提升檢索效果**
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# **2. 建立向量資料庫 - 使用 FAISS**
embedding = OllamaEmbeddings(model="deepseek-r1:1.5b")

# FAISS 向量資料庫
faiss_vectorstore = FAISS.from_documents(docs, embedding)

# **3. 啟動 RAG 問答系統**
retriever = faiss_vectorstore.as_retriever()
llm = Ollama(model="deepseek-r1:1.5b")
qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever)

if __name__ == "__main__":
    # **4. 測試 AI 小助理**
    question = "請解釋 IFRS 16 租賃標準的主要內容"
    response = qa_chain.run(question)
    print(response)
