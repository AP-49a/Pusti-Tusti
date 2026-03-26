from ultralytics import YOLO
import cv2
import csv
import os
from datetime import datetime

# Load YOLO model
model = YOLO("yolov8n.pt")

# Create CSV file if it doesn't exist
if not os.path.exists("food_log.csv"):
    with open("food_log.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Food", "Time"])

# Food classes
food_items = ["banana","apple","orange","sandwich","pizza","hot dog","cake"]

# Start camera
cap = cv2.VideoCapture(0)

print("Food Detection Started...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    detected_food = None

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            if label in food_items:
                detected_food = label

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)

                cv2.putText(frame, label, (x1,y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.9, (0,255,0), 2)

    cv2.imshow("PUSTI TUSTI Food Detection", frame)

    # Press S to save food
    if cv2.waitKey(1) & 0xFF == ord('s'):
        if detected_food:
            time = datetime.now().strftime("%H:%M:%S")

            with open("food_log.csv","a",newline="") as f:
                writer = csv.writer(f)
                writer.writerow([detected_food,time])

            print("Saved:", detected_food, time)

    # ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()