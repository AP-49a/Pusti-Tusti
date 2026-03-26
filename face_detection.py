import cv2
import mediapipe as mp

# Initialize MediaPipe face detection
mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection()

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    results = face_detection.process(rgb_frame)

    if results.detections:
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box
            h, w, c = frame.shape

            x = int(bbox.xmin * w)
            y = int(bbox.ymin * h)
            width = int(bbox.width * w)
            height = int(bbox.height * h)

            # Draw rectangle
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

    cv2.imshow("Face Detection - PUSTI TUSTI", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()