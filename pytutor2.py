import os
import fitz  # PyMuPDF
from langchain_community.document_loaders import TextLoader  # 已修正
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_community.llms.ollama import Ollama
from langchain.chains import RetrievalQA
from langchain.schema import Document

# 資料夾路徑 (使用絕對路徑，請替換為你的實際路徑)
data_dir = r"data"  # r 前綴表示 raw string
faiss_index_dir = "faiss_index"

# 載入資料
documents = []
print(f"開始載入資料，資料夾: {data_dir}")
for filename in os.listdir(data_dir):
    if filename.endswith(".pdf"):
        try:
            filepath = os.path.join(data_dir, filename)
            print(f"嘗試載入檔案: {filepath}")
            # 使用 PyMuPDF 讀取 PDF 內容
            with fitz.open(filepath) as doc:
                text = ""
                for page in doc:
                    text += page.get_text()
            # 建立 Langchain Document 物件
            documents.append(Document(page_content=text, metadata={"source": filename}))
            print(f"成功載入 {filename}")
        except Exception as e:
            print(f"❌ 載入檔案 {filename} 失敗: {e}")

print(f"總共載入的文件數量: {len(documents)}")

if not documents:
    print("❌ 沒有載入任何文件，請檢查資料夾和檔案格式")
    exit()

# 切割文本
text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)  # 調整 chunk_size 和 chunk_overlap
documents = text_splitter.split_documents(documents)

print(f"分割後的文件數量: {len(documents)}")

if not documents:
    print("❌ 分割後沒有任何文件，請檢查文件內容和切割設定")
    exit()


# 建立向量資料庫
print("開始建立向量資料庫")
embeddings = OllamaEmbeddings(model="deepseek-r1:1.5b")

# 測試 OllamaEmbeddings
try:
    test_embedding = embeddings.embed_query("This is a test.")
    print(f"嵌入向量長度: {len(test_embedding)}")
except Exception as e:
    print(f"OllamaEmbeddings 錯誤: {e}")
    exit()

try:
    db = FAISS.from_documents(documents, embeddings)
    print("成功建立向量資料庫")
except Exception as e:
    print(f"❌ 建立向量資料庫失敗: {e}")
    exit()

# 測試 Retriever
query = "What is cash?"
print(f"測試 Retriever，問題: {query}")
retriever = db.as_retriever()
relevant_docs = retriever.get_relevant_documents(query)

print(f"Retriever 找到 {len(relevant_docs)} 筆相關文件")
for i, doc in enumerate(relevant_docs):
    print(f"--- 文件 {i+1} ---")
    print(doc.page_content)
    print(doc.metadata)

# 建立 QA Chain
print("建立 QA Chain")
llm = Ollama(model="deepseek-r1:1.5b")
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

# 問題
query = "What is the heavily tested areas in AICPA FAR？"
print(f"問題: {query}")

# 執行 QA
try:
    response = qa.run(query)
    print(f"回答: {response}")
except Exception as e:
    print(f"❌ 執行 QA 失敗: {e}")

print("程式執行完畢")
