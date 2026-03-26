import cv2
import mediapipe as mp
from ultralytics import YOLO
import qrcode
from datetime import datetime

# Load YOLO model
model = YOLO("yolov8n.pt")

# MediaPipe face detection
mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection()

# Food classes
food_items = ["banana","apple","orange","sandwich","pizza","hot dog","cake"]

# Start camera
cap = cv2.VideoCapture(0)

print("PUSTI TUSTI system started")

qr_generated = False

while True:

    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Face detection
    face_results = face_detection.process(rgb)
    face_detected = False

    if face_results.detections:
        face_detected = True
        cv2.putText(frame,"Face Detected",(20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    # Food detection
    results = model(frame)

    detected_food = None

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            if label in food_items:
                detected_food = label

                x1,y1,x2,y2 = map(int,box.xyxy[0])

                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

                cv2.putText(frame,label,(x1,y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.9,(0,255,0),2)

    # Generate QR automatically
    if face_detected and detected_food and not qr_generated:

        time = datetime.now().strftime("%H:%M:%S")

        data = f"""
PUSTI TUSTI
Face: Detected
Food: {detected_food}
Time: {time}
"""

        qr = qrcode.make(data)
        qr.save("pusti_record.png")

        print("QR Code Generated!")

        qr_generated = True

    cv2.imshow("PUSTI TUSTI System",frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()