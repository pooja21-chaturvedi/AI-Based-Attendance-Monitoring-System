"""Command-line runner. Run from the project root, e.g.:

    python main.py mark ST001 "Test Student"
    python main.py report
    python main.py report --date 2026-10-09 --export data/report.csv
    python main.py detect-image student_images/test.jpg
    python main.py webcam
"""
import argparse

from src.attendance import export_report, get_report, mark_attendance
from src.face_detection import detect_faces_from_webcam, detect_faces_in_image


def main():
    parser = argparse.ArgumentParser(description="AI-Based Attendance Monitoring System")
    sub = parser.add_subparsers(dest="command", required=True)

    p_mark = sub.add_parser("mark", help="Mark a student present")
    p_mark.add_argument("student_id")
    p_mark.add_argument("student_name")

    p_report = sub.add_parser("report", help="Show attendance records")
    p_report.add_argument("--date", help="Filter by date, YYYY-MM-DD")
    p_report.add_argument("--student", help="Filter by student ID")
    p_report.add_argument("--export", help="Save the report to this CSV path")

    p_img = sub.add_parser("detect-image", help="Detect faces in an image")
    p_img.add_argument("image_path")
    p_img.add_argument("--save", help="Save annotated image to this path")

    sub.add_parser("webcam", help="Live face detection (press q to quit)")

    args = parser.parse_args()

    if args.command == "mark":
        print(mark_attendance(args.student_id, args.student_name))
    elif args.command == "report":
        df = get_report(date=args.date, student_id=args.student)
        print(df.to_string(index=False) if not df.empty else "No records found.")
        if args.export:
            export_report(args.export, date=args.date, student_id=args.student)
            print(f"Exported to {args.export}")
    elif args.command == "detect-image":
        n, _ = detect_faces_in_image(args.image_path, save_to=args.save)
        print(f"Faces detected: {n}")
    elif args.command == "webcam":
        detect_faces_from_webcam()


if __name__ == "__main__":
    main()
