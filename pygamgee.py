*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2025-02-20 08:18:18
# @Last Modified by:   boyac
# @Last Modified time: 2025-02-20 08:18:18

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

# Folder path (use absolute path, replace with your actual path)
data_dir = r"data"
faiss_index_dir = "faiss_index"
mymodel = "deepseek-r1:1.5b"

# Check the initial size
initial_size = 0
if os.path.exists(os.path.join(faiss_index_dir, "index.faiss")):
    initial_size = os.path.getsize(os.path.join(faiss_index_dir, "index.faiss"))
print(f"Initial FAISS index size: {initial_size} bytes")

# Load documents
documents = []
print(f"Loading documents, folder: {data_dir}")
for filename in os.listdir(data_dir):
    if filename.endswith(".pdf"):
        try:
            filepath = os.path.join(data_dir, filename)
            print(f"Attempting to load file: {filepath}")
            # Use PyMuPDF to read PDF content
            with fitz.open(filepath) as doc:
                text = ""
                for page in doc:
                    text += page.get_text()
            # Create Langchain Document object
            documents.append(Document(page_content=text, metadata={"source": filename}))
            print(f"Successfully loaded {filename}")
        except Exception as e:
            print(f"❌ Failed to load file {filename}: {e}")

print(f"Total number of documents loaded: {len(documents)}")

if not documents:
    print("❌ No documents loaded, please check folder and file format")
    exit()

# Split text
text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)  # Adjust chunk_size and chunk_overlap
documents = text_splitter.split_documents(documents)

print(f"Number of split documents: {len(documents)}")

if not documents:
    print("❌ No documents after splitting, please check document content and splitting settings")
    exit()

# Create vector database (Load if exists, otherwise create and save)
print("Creating vector database")
embeddings = OllamaEmbeddings(model=mymodel)

if os.path.exists(faiss_index_dir):
    print("Loading FAISS index from disk...")
    try:
        db = FAISS.load_local(faiss_index_dir, embeddings, allow_dangerous_deserialization=True)
        print("FAISS index loaded successfully.")
    except Exception as e:
        print(f"❌ Failed to load FAISS index: {e}")
        exit()
else:
    try:
        db = FAISS.from_documents(documents, embeddings)
        print("Successfully created vector database")
        # Save the FAISS index to disk
        os.makedirs(faiss_index_dir, exist_ok=True)  # Ensure the directory exists
        db.save_local(faiss_index_dir)
        print(f"FAISS index saved to: {faiss_index_dir}")
    except Exception as e:
        print(f"❌ Failed to create vector database: {e}")
        exit()

# Create QA Chain
print("Creating QA Chain")
llm = OllamaLLM(model=mymodel)

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
	# Question
	prompt = """
	What is the best why to understand business consolidation?

	"""

	query = prompt  # Simplified question
	print(f"Question: {query}")

	try:
	    result = qa_chain.invoke({"query": query})

	    print(f"Answer: {result['result']}")

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
	    print(f"❌ QA execution failed: {e}")

	print("Program execution finished")
	# Check the size
	final_size = 0
	if os.path.exists(os.path.join(faiss_index_dir, "index.faiss")):
	    final_size = os.path.getsize(os.path.join(faiss_index_dir, "index.faiss"))
	print(f"Final FAISS index size: {final_size} bytes")
