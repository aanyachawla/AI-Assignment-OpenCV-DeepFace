
import cv2

from deepface import DeepFace


# Open Webcam

cap = cv2.VideoCapture(0)
while True:

    ret, frame = cap.read()


    if not ret:

        break


    try:

        # Analyze Emotion

        result = DeepFace.analyze(

            frame,

            actions=["emotion"],

            detector_backend="opencv",      # Faster and simpler

            enforce_detection=False,

            silent=True

        )


        emotion = result[0]["dominant_emotion"]


        # Display Emotion

        cv2.putText(

            frame,

            f"Emotion: {emotion}",

            (20, 40),

            cv2.FONT_HERSHEY_SIMPLEX,

            1,

            (0, 255, 0),

            2

        )


    except Exception as e:

        print(e)


    cv2.imshow("Live Emotion Detection", frame)


    # Press ESC to Exit

    if cv2.waitKey(1) & 0xFF == 27:

        break
    
cap.release()

cv2.destroyAllWindows()