# RAG-Based Learning Assistant with Ollama and FAISS

[![GitHub Sponsors](https://img.shields.io/github/sponsors/boyac?style=for-the-badge)](https://github.com/sponsors/boyac)
[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/boyac)

Support this project by becoming a GitHub Sponsor or buying me a coffee!

![PyGamgee Logo](assets/logo.png)

# PyGamgee: A RAG-Based Learning Assistant

## About  
This project aims to enhance how we interact with information and make learning more efficient by leveraging **open-source language models**. While the current model is small, it’s effective for retrieving relevant information for **studying**, **decision-making**, and **analysis**. The system operates **locally**, ensuring **privacy** and **offline access** without relying on cloud services.

Initially designed for **personal use**, I believe the project can support a wide range of users, from **professionals** staying updated on industry trends to **hobbyists** exploring new topics. Moving forward, I plan to improve the system with more advanced features and welcome **contributions** from others.

Named *PyGamgee* in homage to **Samwise Gamgee** from *The Lord of the Rings*, the project may seem humble, but its goal is to **assist** and **empower** users in their journey to master knowledge and make informed decisions.

Ultimately, this project reflects my belief in accessible technology that streamlines knowledge acquisition and supports users in applying information that drives growth and learning. By making it **open-source**, I hope others will contribute to improving and adapting it to their needs.


## Description

This project implements a Retrieval-Augmented Generation (RAG) based question answering system designed to help students, analyst learn and prepare for their studies, exams and analysis. It leverages the following technologies:

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

## Hardware Upgrade Recommendations

While the current model (`deepseek-r1:1.5b`) works well for basic learning and analysis, if you require higher accuracy or need to run larger models, we recommend upgrading your hardware to support models that require 80GB+ of GPU memory. This will significantly improve the accuracy and performance of your system.

### Recommended Actions:
- **Upgrade your GPU:** For larger models such as `deepseek-r1:70b`, your GPU must have at least 80GB of VRAM. Additionally, multiple GPUs will be needed for parallel processing to achieve optimal performance.
- **Choose a higher precision model:** If you're aiming for more advanced, accurate results, upgrading to models like `deepseek-r1:70b` will provide much better outputs, but they require more powerful hardware to run effectively.

### How to Upgrade:
- **Use the Ollama command to pull larger models:**
   ```bash
   ollama pull deepseek-r1:70b
   ```

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/boyac/pyGamgee.git
    cd pyGamgee
    ```

2.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

   *It is highly recommended to use a virtual environment.*


## Usage

1.  **Prepare your study materials:** Place your data source (in PDF format) in a directory named `data`.

2.  **Configure the script:**

    *   Modify the `data_dir` variable in the `pygamgee.py` script (or your main script file) to point to the correct directory containing your study notes.  Use an absolute path for reliability. Example: `data_dir = r"data"`
    *   Ensure Ollama is running with your desired model loaded (e.g., `deepseek-r1:1.5b`).
    *   *Optional:* Adjust the `chunk_size` and `chunk_overlap` parameters in the `CharacterTextSplitter` to optimize retrieval performance for your specific study materials.

3.  **Run the script:**

    ```bash
    python pygamgee.py
    ```

4.  **Start Learning:** A Gradio interface will open in your web browser. Ask questions about the materials and receive answers based on your data!

## Code Overview

*   **`pygamgee.py`:** The main script that handles data loading, embedding generation, FAISS indexing, question answering, and the Gradio interface.
*   **`data/`:** Directory where your data source (PDF documents) are stored. **Example file:** `far2024.pdf`
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

## Future Directions and Potential Features

I have several ideas for future enhancements to this project, but limited time to implement them myself. I'd love to hear your feedback and welcome contributions!

*   **Incremental Indexing:** Implement incremental updates to the FAISS index, allowing for faster updates when new data is added.
*   **Support for More File Types:** Add support for other document and media formats, such as DOCX, TXT, CSV, JPG, MP3, and MP4.
*   **Improved UI/UX:** Enhance the Gradio interface with features like:
    *   A loading indicator during long-running operations.
    *   A more visually appealing design.
    *   Options for customizing the LLM and other settings.
*   **More Advanced Memory Management:** Explore different memory types in Langchain to optimize performance.
*   **Personalized learning paths:**  The system could track the student's strengths and weaknesses and recommend specific topics to study.
*   **Adaptive questioning:** The system could adjust the difficulty of the questions based on the student's performance.
*   **Feedback and encouragement:** The system could provide feedback on the student's answers and offer encouragement to keep them motivated.
*   **API Endpoint:** Expose a way to call this chatbot, rather than just running it as a GUI.

These are just a few ideas, and I'm open to suggestions and contributions from the community!
## Support

This project is made possible by the generous support of its users. If you find this project helpful, please consider:

[![GitHub Sponsors](https://img.shields.io/github/sponsors/boyac?style=for-the-badge)](https://github.com/sponsors/boyac)
[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/boyac)
![Downloads](https://img.shields.io/github/downloads/boyac/pyGamgee/total)
*   Becoming a GitHub Sponsor
*   Buying me a coffee on Ko-fi

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
