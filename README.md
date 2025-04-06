# 🚀 Awesome FastAPI Tools for AI Projects

A curated collection of tools, patterns, and extensions to build **FastAPI** backends for **AI/ML projects**. Whether you're serving deep learning models or building real-time inference APIs, this repo is for you.

## 📂 Categories

### 🔥 Model Serving
- [Triton Inference Server integration](tools/model-serving/triton)
- [TorchServe with FastAPI](tools/model-serving/torchserve)
- HuggingFace Transformers with FastAPI

### 🧹 Data Preprocessing
- Streaming data preprocessing
- Async file handling with FastAPI

### 📡 WebSocket & Real-Time Inference
- Multi-client WebSocket inference (YOLO, etc.)
- Thread-safe camera streaming APIs

### 🔐 Auth & Security
- JWT with role-based access
- Secure API keys for ML endpoints

### 📈 Monitoring & Logging
- Prometheus + Grafana
- Custom logs for inference requests

### 🧪 Examples
- YOLOv8 real-time inference app
- Chatbot API with LangChain
- Embedding API with Faiss + FastAPI

## 🛠 Setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
