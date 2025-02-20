# RAG-Based Question Answering System with Ollama and FAISS

## Description

This project implements a Retrieval-Augmented Generation (RAG) based question answering system using the following technologies:

*   **Langchain:**  A framework for building applications powered by large language models (LLMs).
*   **Ollama:** A tool for running large language models locally.
*   **FAISS (Facebook AI Similarity Search):** A library for efficient similarity search and clustering of dense vectors.
*   **PyMuPDF (fitz):** A Python binding for MuPDF, used for reading and extracting text from PDF documents.

The system ingests data from a specified directory, creates embeddings using Ollama, stores the embeddings in a FAISS index, and then uses this index to retrieve relevant information when answering questions. This allows you to ask questions about your documents and receive answers based on the content within those documents.

## Key Features

*   **Local LLM:** Leverages Ollama to run a large language model locally, eliminating the need for cloud-based APIs.
*   **PDF Support:**  Extracts text from PDF documents using PyMuPDF.
*   **FAISS Indexing:**  Uses FAISS for fast and efficient similarity search, enabling quick retrieval of relevant document chunks.
*   **RAG Implementation:**  Combines retrieval and generation to provide context-aware and informative answers.
*   **Customizable:** Easily adaptable to different data sources and LLMs.

## Requirements

Before running this project, you need to have the following installed:

*   **Python 3.7+**
*   **Ollama:** Follow the installation instructions on the [Ollama website](https://ollama.com/). Make sure Ollama is running and the desired model is downloaded.
*   **pip:** Python package installer.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [YOUR_REPOSITORY_URL]
    cd [YOUR_REPOSITORY_NAME]
    ```

2.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

    *(Create a `requirements.txt` file with the following dependencies, or adapt to your project's actual requirements)*

    ```
    langchain
    langchain-community
    langchain-ollama
    faiss-cpu  # or faiss-gpu if you have a CUDA-enabled GPU
    pymupdf
    tqdm
    ```

## Usage

1.  **Prepare your data:** Place the documents you want to use for question answering (e.g., PDF files) in a directory named `data`.

2.  **Configure the script:**

    *   Modify the `data_dir` variable in the script to point to the correct directory containing your data files.
    *   Ensure that Ollama is running with the desired model loaded. The default model is specified in the script (e.g., `deepseek-r1:1.5b`). You can change this to any model available in Ollama.

3.  **Run the script:**

    ```bash
    python your_script_name.py
    ```

    Replace `your_script_name.py` with the actual name of your Python script.

4.  **Ask questions:**  The script will load the data, create the FAISS index, and then prompt you to ask a question.  The system will then provide an answer based on the retrieved information.

## Code Overview

*   **`tutor2.py`:**  The main script that handles data loading, embedding generation, FAISS indexing, and question answering.  (Adjust this to your actual script name)
*   **`data/`:** (example) Directory where your data files (e.g., PDF documents) are stored.
*   **`faiss_index/`:** Directory where the FAISS index is saved (created automatically).

## Contributing

Contributions are welcome! If you find a bug or have an idea for a new feature, please open an issue or submit a pull request.

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Submit a pull request.

## License

[Choose a License - e.g., MIT License]

(Optional:  Include license details here or link to a LICENSE file)****
