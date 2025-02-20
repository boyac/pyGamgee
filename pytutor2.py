import os
import fitz  # PyMuPDF
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
from langchain.schema import Document
from langchain.memory import ConversationBufferMemory  # ADD THIS IMPORT

# 資料夾路徑 (使用絕對路徑，請替換為你的實際路徑)
data_dir = r"data"
faiss_index_dir = "faiss_index"

# Check the initial size
initial_size = 0
if os.path.exists(os.path.join(faiss_index_dir, "index.faiss")):
    initial_size = os.path.getsize(os.path.join(faiss_index_dir, "index.faiss"))
print(f"Initial FAISS index size: {initial_size} bytes")

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

# 建立向量資料庫 (Load if exists, otherwise create and save)
print("開始建立向量資料庫")
embeddings = OllamaEmbeddings(model="deepseek-r1:1.5b")

if os.path.exists(faiss_index_dir):
    print("Loading FAISS index from disk...")
    try:
        db = FAISS.load_local(faiss_index_dir, embeddings, allow_dangerous_deserialization=True)
        print("FAISS index loaded successfully.")
    except Exception as e:
        print(f"❌ 載入 FAISS 索引失敗: {e}")
        exit()
else:
    try:
        db = FAISS.from_documents(documents, embeddings)
        print("成功建立向量資料庫")
        # Save the FAISS index to disk
        os.makedirs(faiss_index_dir, exist_ok=True)  # Ensure the directory exists
        db.save_local(faiss_index_dir)
        print(f"FAISS index saved to: {faiss_index_dir}")
    except Exception as e:
        print(f"❌ 建立向量資料庫失敗: {e}")
        exit()

#建立 QA Chain
print("建立 QA Chain")
llm = OllamaLLM(model="deepseek-r1:1.5b")

# ADD THIS SECTION:
use_memory = True  # Set to True to use memory, False to disable it

memory = None  # Initialize memory to None
if use_memory:
    memory = ConversationBufferMemory(
        llm=llm,
        memory_key="chat_history",
        return_messages=True,
        output_key='result'  # Specify the output key
    )

qa_chain = RetrievalQA.from_chain_type(
    llm,
    chain_type="stuff",
    retriever=db.as_retriever(),
    memory=memory if use_memory else None,  # Pass memory conditionally
    return_source_documents=True
)

def pretty_print_docs(documents):
    print(f"\n{'-' * 100}\n".join(f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(documents)))


if __name__ == "__main__":
	# 問題
	prompt = """
	500 words summary for FAR.

	"""

	query = prompt  # Simplified question
	print(f"問題: {query}")

	try:
	    result = qa_chain.invoke({"query": query})

	    print(f"回答: {result['result']}")

	    if 'source_documents' in result:
	        print("\nSource Documents:")
	        pretty_print_docs(result['source_documents'])
	    else:
	        print("\nNo source documents found.")

	    if use_memory:
	        # **ADD THIS SECTION TO PRINT THE MEMORY**
	        print("\n--- Conversation History ---")
	        # Print the memory ONLY if it exists (use_memory is True)
	        print(memory.load_memory_variables({}))  # Check the memory here

	except Exception as e:
	    print(f"❌ 執行 QA 失敗: {e}")

	print("程式執行完畢")
	# Check the size
	final_size = 0
	if os.path.exists(os.path.join(faiss_index_dir, "index.faiss")):
	    final_size = os.path.getsize(os.path.join(faiss_index_dir, "index.faiss"))
	print(f"Final FAISS index size: {final_size} bytes")
