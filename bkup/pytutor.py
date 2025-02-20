import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model
from datasets import load_dataset
from torch.optim import AdamW
from torch.utils.data import DataLoader

# 檢查 GPU 或 M1/M2 Metal 支援
device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

# 載入模型和 Tokenizer
model_name = "deepseek-ai/deepseek-llm-7b-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    device_map="auto",   # 自動選擇設備
    torch_dtype=torch.float16 if device != "cpu" else torch.float32
).to(device)

# 配置 LoRA
lora_config = LoraConfig(r=8, lora_alpha=32, lora_dropout=0.1, task_type="CAUSAL_LM")
model = get_peft_model(model, lora_config)
model.train()

# 讀取訓練資料
dataset = load_dataset("json", data_files="my_data.json")
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True, return_tensors="pt")

# 資料前處理
tokenized_dataset = dataset.map(tokenize_function, batched=True)
train_dataloader = DataLoader(tokenized_dataset['train'], batch_size=4, shuffle=True)

# 定義 Optimizer
optimizer = AdamW(model.parameters(), lr=5e-5)

# 開始訓練
num_epochs = 3
for epoch in range(num_epochs):
    for batch in train_dataloader:
        # 將資料移至 GPU 或 MPS 裝置
        input_ids = batch['input_ids'].squeeze(1).to(device)
        attention_mask = batch['attention_mask'].squeeze(1).to(device)
        
        # 前向傳播與計算 Loss
        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=input_ids)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        print(f"Epoch {epoch+1}, Loss: {loss.item()}")

# 儲存模型和 Tokenizer
model.save_pretrained("my_expert_model")
tokenizer.save_pretrained("my_expert_model")

print("模型已儲存！")
