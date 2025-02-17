# pyTutor

# 📂 AICPA_Tutor/
根據你的需求，這是專案的檔案結構：

## 📂 data/                    
存放 CPA FAR 課本、筆記、題庫等資料。
- 📄 Becker_FAR.pdf  
- 📄 Gleim_Notes.docx  
- 📄 FAR_Exam_MCQs.csv  
- 📄 自己整理的筆記.txt  

## 📂 models/                  
存放 DeepSeek 模型或其他用於推理的模型。
- 📂 deepseek-mistral-7b/  

## 📂 embeddings/              
儲存已解析的知識並創建向量索引，用於快速查詢。
- 📄 index.json  

## 🖥️ app.py                       
主程式，用來啟動 AI Tutor，提供用戶介面與功能。

## 📝 ingest.py                    
讀取並處理 CPA FAR 資料，將其轉換成適合進行索引和查詢的格式。

## 🔎 query.py                     
問答引擎，提供查詢功能，讓使用者可以向 AI Tutor 發問。

## 📜 requirements.txt             
列出所有需要安裝的 Python 套件，以便於安裝與環境配置。

## 📑 README.md                    
專案介紹文件，包含如何使用 AI CPA Tutor 的說明。
