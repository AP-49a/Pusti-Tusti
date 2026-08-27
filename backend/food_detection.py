from ultralytics import YOLO

model = YOLO("yolov8n.pt")

# Only allow food-related classes
allowed_foods = [
    "apple",
    "banana",
    "orange",
    "pizza",
    "sandwich",
    "cake",
    "donut",
    "broccoli",
    "carrot"
]

def detect_food(image_path):

    results = model(image_path, conf=0.1)

    detected_foods = []

    for r in results:

        for box in r.boxes:

            cls = int(box.cls[0])

            label = model.names[cls]

            # Filter only food items
            if label in allowed_foods:

                detected_foods.append(label)

    return list(set(detected_foods))