
# 1. Authenticate
from huggingface_hub import login
import os

# safer: store in env var first (Windows PowerShell):
# setx HUGGINGFACE_TOKEN "hf_xxx"
login(token=os.environ["HUGGINGFACE_TOKEN"])


# 2. Quick inference (load a model → generate text)
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "mistralai/Mistral-7B-Instruct-v0.2"  # pick any compatible model

tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"  # dispatch across CPU/GPU automatically
)

# Low-RAM tip (if you hit memory limits / error 1455 on Windows):
prompt = "Write a haiku about the sea."
inputs = tok(prompt, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=80, do_sample=True, temperature=0.7)
print(tok.decode(out[0], skip_special_tokens=True))

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    load_in_8bit=True,   # needs bitsandbytes
    # or load_in_4bit=True
)

# 3. Pipelines (one-liner tasks)
from transformers import pipeline

pipe = pipeline("text-generation", model=model_id, device_map="auto")
print(pipe("Explain transformers in 1 sentence.", max_new_tokens=50)[0]["generated_text"])


# 4. Datasets: load, split, map
from datasets import load_dataset

ds = load_dataset("imdb")             # or local files with load_dataset("json", data_files=...)
train = ds["train"].shuffle(seed=42).select(range(2000))
test  = ds["test"].shuffle(seed=42).select(range(1000))


# 5. Tokenize + Trainer fine-tuning (text classification example)
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
import numpy as np
from evaluate import load as load_metric

model_id = "distilbert-base-uncased"
tok = AutoTokenizer.from_pretrained(model_id)
def tokenize(batch): return tok(batch["text"], truncation=True, padding="max_length", max_length=256)

train_t = train.map(tokenize, batched=True)
test_t  = test.map(tokenize, batched=True)

model = AutoModelForSequenceClassification.from_pretrained(model_id, num_labels=2)

metric = load_metric("accuracy")
def compute_metrics(p):
    preds = np.argmax(p.predictions, axis=1)
    return metric.compute(predictions=preds, references=p.label_ids)

args = TrainingArguments(
    output_dir="out-imdb",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=32,
    num_train_epochs=2,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    logging_steps=50,
    push_to_hub=True,               # <- push results to your repo
    hub_model_id="your-username/imdb-distilbert",  # optional custom name
)

trainer = Trainer(model=model, args=args, train_dataset=train_t, eval_dataset=test_t, compute_metrics=compute_metrics)
trainer.train()
trainer.push_to_hub()               # push model + logs to the Hub


# 6. Push/pull any files or models
from huggingface_hub import HfApi, create_repo, upload_file

api = HfApi()
create_repo(name="my-awesome-model", repo_type="model", exist_ok=True)
upload_file(
    path_or_fileobj="README.md",
    path_in_repo="README.md",
    repo_id="your-username/my-awesome-model",
    repo_type="model"
)

# 7. Web app hosting with Gradio + Spaces
import gradio as gr
from transformers import pipeline

pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.2", device_map="auto")

def chat(prompt):
    return pipe(prompt, max_new_tokens=128, do_sample=True, temperature=0.7)[0]["generated_text"]

demo = gr.Interface(fn=chat, inputs="text", outputs="text", title="Mini Chatbot")
demo.launch()


# 8) Good practices
# Use Read tokens for inference; Write tokens only for training/pushing.
# Keep tokens in env vars or CI secrets (never hard-code).
# For big models: set Windows pagefile larger, use device_map="auto" and/or load_in_8bit=True.
# Use accelerate config to set a proper device map / multi-GPU offload when needed.