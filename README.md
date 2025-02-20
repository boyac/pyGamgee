# RAG-Based Learning Assistant with Ollama and FAISS

[![GitHub Sponsors](https://img.shields.io/github/sponsors/YOUR_GITHUB_USERNAME?style=for-the-badge)](https://github.com/sponsors/YOUR_GITHUB_USERNAME)
[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/YOUR_KOFI_USERNAME)

Support this project by becoming a GitHub Sponsor or buying me a coffee!

## Description

This project implements a Retrieval-Augmented Generation (RAG) based question answering system designed to help students learn and prepare for the AICPA FAR (Financial Accounting & Reporting) exam. It leverages the following technologies:

*   **Langchain:** A powerful framework for building applications powered by large language models (LLMs).
*   **Ollama:** Enables running large language models locally, ensuring privacy and offline access.
*   **FAISS (Facebook AI Similarity Search):** Provides efficient similarity search for quick retrieval of relevant information from study materials.
*   **PyMuPDF (fitz):** Used for extracting text from PDF study notes and textbooks.
*   **Gradio:** Creates an interactive chat interface for easy learning.

The system ingests PDF study notes, creates embeddings using Ollama, stores them in a FAISS index, and then uses this index to answer your questions about the material. This allows for a more interactive and personalized learning experience.

## Key Features

*   **Localized Knowledge:** Runs entirely on your local machine, keeping your study data private and accessible offline.
*   **Interactive Chat Interface:** Uses Gradio to provide a user-friendly way to ask questions and receive answers.
*   **PDF Study Material Support:** Extracts text from PDF study notes, making it easy to learn from existing resources.
*   **Efficient Retrieval:** FAISS indexing enables quick retrieval of relevant information from your study materials.
*   **Personalized Learning:** By asking questions, you can explore the material in a way that suits your learning style.

## Requirements

Before running this project, ensure you have the following installed:

*   **Python 3.8+** (Recommended for best compatibility)
*   **Ollama:** Follow the installation instructions on the [Ollama website](https://ollama.com/). Make sure Ollama is running and your chosen model (e.g., `deepseek-r1:1.5b`) is downloaded. Use `ollama pull deepseek-r1:1.5b` to download the model.
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

    *(Create a `requirements.txt` file with the following dependencies, or adapt to your project's actual requirements. It is highly recommended to use a virtual environment.)*

    ```
    langchain==0.1.11  # Or later, test for compatibility
    langchain-community==0.0.29 # Or later, test for compatibility
    langchain-ollama==0.0.8   # Or later, test for compatibility
    faiss-cpu==1.7.4       # Or faiss-gpu if you have a CUDA-enabled GPU
    pymupdf==1.23.18
    gradio==4.22.1 # Add Gradio
    tqdm==4.66.2
    ```

## Usage

1.  **Prepare your study materials:** Place your AICPA FAR study notes (in PDF format) in a directory named `data`.

2.  **Configure the script:**

    *   Modify the `data_dir` variable in the `tutor2.py` script (or your main script file) to point to the correct directory containing your study notes.  Use an absolute path for reliability. Example: `data_dir = r"C:\Users\YourName\Documents\AICPA_FAR_Study"`
    *   Ensure Ollama is running with your desired model loaded (e.g., `deepseek-r1:1.5b`).
    *   *Optional:* Adjust the `chunk_size` and `chunk_overlap` parameters in the `CharacterTextSplitter` to optimize retrieval performance for your specific study materials.

3.  **Run the script:**

    ```bash
    python tutor2.py
    ```

    Replace `tutor2.py` with the actual name of your Python script.

4.  **Start Learning:** A Gradio interface will open in your web browser. Ask questions about AICPA FAR and receive answers based on your study notes!

## Code Overview

*   **`tutor2.py`:** The main script that handles data loading, embedding generation, FAISS indexing, question answering, and the Gradio interface.
*   **`data/`:** Directory where your AICPA FAR study notes (PDF documents) are stored. **Example file:** `far2024.pdf`
*   **`faiss_index/`:** Directory where the FAISS index is saved (created automatically during the first run).  This allows for faster loading on subsequent runs.

## Troubleshooting

*   **Slow Response Times:** This may occur for large local language models. Ensure you have enough free RAM available and consider using a smaller Ollama model.
*   **Gradio Interface Not Loading:**  Make sure Gradio is installed correctly and that your web browser supports JavaScript.
*   **Errors related to FAISS:** Ensure that `faiss-cpu` (or `faiss-gpu`) is correctly installed.
*   **Ollama Related Issues:** Make sure `ollama serve` is always running in the background.

## Contributing

Contributions are welcome! If you find a bug, have an idea for a new feature, or want to improve the documentation, please open an issue or submit a pull request.

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Submit a pull request.

Please see `CONTRIBUTING.md` for guidelines.

## Support

This project is made possible by the generous support of its users. If you find this project helpful, please consider:

[![GitHub Sponsors](https://img.shields.io/github/sponsors/YOUR_GITHUB_USERNAME?style=for-the-badge)](https://github.com/sponsors/YOUR_GITHUB_USERNAME)
[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/YOUR_KOFI_USERNAME)

*   Becoming a GitHub Sponsor
*   Buying me a coffee on Ko-fi

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
