import cv2
import numpy as np
import pytest

from src.face_detection import detect_faces_in_image


def test_invalid_path_raises_clear_error(tmp_path):
    with pytest.raises(FileNotFoundError):
        detect_faces_in_image(tmp_path / "does_not_exist.jpg")


def test_image_without_face_returns_zero(tmp_path):
    blank = np.full((200, 200, 3), 255, dtype=np.uint8)
    path = tmp_path / "blank.jpg"
    cv2.imwrite(str(path), blank)
    count, boxes = detect_faces_in_image(path)
    assert count == 0
    assert len(boxes) == 0
