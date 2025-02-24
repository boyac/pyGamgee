# -*- coding: utf-8 -*-
# @Author: boyac
# @Date: 2025-02-20 08:18:18
# @Last Modified by: boyac
# @Last Modified time: 2025-02-20 08:18:18

import unittest
import os
import fitz  # PyMuPDF
from langchain.schema import Document

# Import the functions from pygamgee.py (adjust the import method as needed)
# Assuming the functions in pygamgee.py are defined in the pygamgee module
import pygamgee
from pygamgee import load_data  # Assuming load_data function exists in pygamgee.py

# Note: Modify data_dir to the path of the test environment
TEST_DATA_DIR = "test_data"
TEST_FAISS_INDEX_DIR = "test_faiss_index"

class TestPyGamgee(unittest.TestCase):

    # Executed before each test method, used to set up the test environment
    def setUp(self):
        # Create test data folder and file
        os.makedirs(TEST_DATA_DIR, exist_ok=True)
        # Create test faiss folder
        os.makedirs(TEST_FAISS_INDEX_DIR, exist_ok=True)

        # Create a test PDF file
        test_pdf_file = os.path.join(TEST_DATA_DIR, "test_file.pdf")
        with fitz.open() as pdf:
            page = pdf.new_page(width=612, height=792)
            page.insert_text((50, 50), "This is a test PDF file.")
            pdf.save(test_pdf_file)

    # Executed after each test method, used to clean up the test environment
    def tearDown(self):
        # Delete the test data folder and file
        import shutil
        shutil.rmtree(TEST_DATA_DIR, ignore_errors=True)
        shutil.rmtree(TEST_FAISS_INDEX_DIR, ignore_errors=True)

    def test_load_data(self):
        # Call the load_data function
        documents = load_data(TEST_DATA_DIR)

        # Assert that the data is loaded correctly
        self.assertIsNotNone(documents)
        self.assertEqual(len(documents), 1)
        self.assertIsInstance(documents[0], Document)
        self.assertEqual(documents[0].page_content, "This is a test PDF file.")

    def test_load_data_no_file(self):
        # Test the case where data_dir is empty
        empty_dir = "empty_data"
        os.makedirs(empty_dir, exist_ok=True)
        documents = load_data(empty_dir)
        self.assertEqual(len(documents), 0)
        shutil.rmtree(empty_dir, ignore_errors=True)


    # You can add more test functions, such as testing text splitting, vector database, QA chain, etc.

if __name__ == '__main__':
    unittest.main()
