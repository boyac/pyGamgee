# pyTutor

📂 AI_CPA_Tutor/
│── 📂 data/                    # 存放 CPA FAR 課本、筆記、題庫
│     ├── Becker_FAR.pdf
│     ├── Gleim_Notes.docx
│     ├── FAR_Exam_MCQs.csv
│     ├── 自己整理的筆記.txt
│
│── 📂 models/                  # 存放 DeepSeek 模型
│     ├── deepseek-mistral-7b/
│
│── 📂 embeddings/              # 向量索引（儲存已解析的知識）
│     ├── index.json
│
│── app.py                       # 主程式（啟動 AI Tutor）
│── ingest.py                    # 讀取 & 處理 CPA FAR 資料
│── query.py                     # 問答引擎（查詢 AI 知識庫）
│── requirements.txt             # 需要安裝的 Python 套件
│── README.md                    # 介紹如何使用 AI CPA Tutor
