from ultralytics import YOLO
import cv2
import cvzone
import math

model = YOLO('../Yolo-Weights/yolov8m.pt')
results = model("Images/img_cars.jpg", show=True)
cv2.waitKey(0)
