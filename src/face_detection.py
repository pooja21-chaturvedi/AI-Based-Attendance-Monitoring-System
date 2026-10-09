"""Face DETECTION using OpenCV Haar cascades.

This finds face-shaped regions only. It does NOT identify who a person is.
Recognition is a separate step to add once the team agrees on enrollment,
consent and the recognition method. Unknown people must never be marked
as known students.
"""
import cv2


def _load_cascade():
    path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(path)
    if cascade.empty():
        raise RuntimeError("Could not load face detection model.")
    return cascade


def detect_faces_in_image(image_path, save_to=None):
    """Detect faces in an image file. Returns (number_of_faces, boxes).

    If save_to is given, writes a copy of the image with green boxes drawn.
    """
    image = cv2.imread(str(image_path))
    if image is None:
        raise FileNotFoundError(f"Could not open image: {image_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = _load_cascade().detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    if save_to:
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imwrite(str(save_to), image)

    return len(faces), faces


def detect_faces_from_webcam(camera_index=0):
    """Open the webcam and show live detections. Press 'q' to quit."""
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise RuntimeError("Camera unavailable. Check permissions or camera index.")

    cascade = _load_cascade()
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                raise RuntimeError("Could not read frame from camera.")
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imshow("Face detection (press q to quit)", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
