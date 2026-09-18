import cv2
from deepface import DeepFace

print("Starting Gender Classification...")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame")
        break

    try:
        result = DeepFace.analyze(
            frame,
            actions=["gender"],
            detector_backend="opencv",
            enforce_detection=False,
            silent=True
        )

        # Handle different DeepFace versions
        if isinstance(result, list):
            gender = result[0]["dominant_gender"]
        else:
            gender = result["dominant_gender"]

        cv2.putText(
            frame,
            f"Gender: {gender}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

    except Exception as e:
        cv2.putText(
            frame,
            "Analyzing...",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )
        print("Error:", e)

    cv2.imshow("Gender Classification", frame)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()