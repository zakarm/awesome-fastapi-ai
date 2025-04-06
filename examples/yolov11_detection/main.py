from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
import numpy as np
import cv2
import shutil
import os

app = FastAPI(title="YOLOv8 Detection API")

model = YOLO("yolov11n.pt")

@app.post("/detect")
async def detect_objects(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    results = model(image)
    boxes = results[0].boxes.xyxy.cpu().numpy().tolist()
    return {"boxes": boxes}
