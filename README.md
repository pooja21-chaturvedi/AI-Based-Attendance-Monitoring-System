# 🤖 AI-Based Attendance Monitoring System

## 📌 Project Overview

The **AI-Based Attendance Monitoring System** is a Software Engineering project focused on designing a smart and efficient approach to attendance management.

Traditional attendance systems often involve manual processes that can be time-consuming and prone to errors. This project explores an AI-based solution to improve the accuracy, efficiency, and management of attendance records.

This repository contains the **documentation and requirement analysis** of the project, plus a **Python developer prototype** (attendance recording and face detection).

---

## 🎯 Project Objectives

- Analyze the feasibility of the proposed system.
- Identify functional and non-functional requirements.
- Understand the needs of different stakeholders.
- Establish a clear foundation for future system development.
- Improve the efficiency and reliability of attendance management.
- Explore the use of AI for smarter attendance monitoring.

---

## 📂 Documentation

### 📄 Feasibility Report
Evaluates whether the proposed system is practical: technical, economic, operational and schedule feasibility.

### 📝 Requirement Gathering Report
Stakeholder identification, requirement elicitation, functional and non-functional requirements, and user expectations.

Detailed information is available in the documents included in this repository.

---

## 👥 Stakeholder Perspectives

- **Developer** – System design, technologies, implementation, scalability, maintainability.
- **Tester** – Testing, requirement validation, reliability, error identification.
- **Expert** – Technical knowledge, recommendations, guidance.
- **Adviser** – Project planning, progress review, overall guidance.
- **Users** – Usability, accuracy, accessibility, efficient attendance management.

---

## ⚙️ Key Requirements

- User authentication and access management.
- Attendance monitoring and recording.
- Management of attendance records.
- Viewing attendance information.
- Report generation and data management.

Quality attributes: **usability, reliability, security, performance, scalability, maintainability**.

---

## 👥 Project Team

| Team Member          | Role      |
| -------------------- | --------- |
| **Pooja Chaturvedi** | Developer |
| **Parul Goel**       | Expert    |
| **Prabal Pratap**    | Adviser   |
| **Prakhar**          | Tester    |

---

## 💻 Developer Prototype (Python)

### What is implemented
- CSV attendance recording with **one record per student per date** (duplicates rejected)
- Reports filtered by date / student, and CSV export
- OpenCV face **detection** from an image or webcam
- Automated tests (pytest) and a Jupyter notebook demo

### Project structure
```
AI-Based-Attendance-Monitoring-System/
├── data/                 # attendance.csv is created here (git-ignored)
├── student_images/       # your test photos (git-ignored, keep private)
├── notebooks/
│   └── prototype.ipynb   # step-by-step demo
├── src/
│   ├── attendance.py     # mark_attendance, get_report, export_report
│   └── face_detection.py # detect_faces_in_image, detect_faces_from_webcam
├── tests/                # pytest tests
├── main.py               # command-line runner
├── requirements.txt
└── README.md
```

### Setup
```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run
```bash
python -m pytest -v                                   # run tests
python main.py mark ST001 "Test Student"              # mark attendance
python main.py report                                 # view records
python main.py report --date 2026-10-09 --export data/report.csv
python main.py detect-image student_images/test.jpg --save student_images/out.jpg
python main.py webcam                                 # press q to quit
```
Or open `notebooks/prototype.ipynb` in VS Code and choose the `venv` kernel.

### Limitations
- Face **detection** only — it does not identify people. Recognition is not implemented yet.
- CSV storage; database integration is a later task.
- Duplicate rule: one record per student per date.
- Student photos and attendance data are git-ignored and must not be published.

---

## 🚀 Future Scope
- AI-based attendance identification (face recognition, after consent/enrollment rules are agreed)
- Database integration (SQLite or the team's chosen DB)
- User interface and authentication
- Real-time monitoring, reports and analytics

---

## 📌 Project Status

**Current Status:** 🟢 Python prototype (attendance logic + face detection) added; recognition, database and UI pending.
