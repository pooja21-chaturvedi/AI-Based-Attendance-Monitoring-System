import pytest

from src.attendance import export_report, get_report, init_file, mark_attendance


def test_new_student_saved(tmp_path):
    f = tmp_path / "att.csv"
    assert mark_attendance("ST001", "Test", file=f) == "Attendance marked successfully."
    report = get_report(file=f)
    assert len(report) == 1
    assert report.loc[0, "student_id"] == "ST001"
    assert report.loc[0, "status"] == "Present"


def test_duplicate_rejected(tmp_path):
    f = tmp_path / "att.csv"
    mark_attendance("ST001", "Test", file=f)
    assert mark_attendance("ST001", "Test", file=f) == "Attendance already marked for today."
    assert len(get_report(file=f)) == 1


def test_different_student_allowed(tmp_path):
    f = tmp_path / "att.csv"
    mark_attendance("ST001", "A", file=f)
    mark_attendance("ST002", "B", file=f)
    assert len(get_report(file=f)) == 2


def test_empty_file_report(tmp_path):
    f = tmp_path / "att.csv"
    init_file(f)
    assert get_report(file=f).empty


def test_invalid_input(tmp_path):
    with pytest.raises(ValueError):
        mark_attendance("", "", file=tmp_path / "att.csv")


def test_filter_by_student_and_date(tmp_path):
    f = tmp_path / "att.csv"
    mark_attendance("ST001", "A", file=f)
    mark_attendance("ST002", "B", file=f)
    assert len(get_report(student_id="ST002", file=f)) == 1
    assert len(get_report(date="1999-01-01", file=f)) == 0


def test_export_report(tmp_path):
    f = tmp_path / "att.csv"
    out = tmp_path / "out.csv"
    mark_attendance("ST001", "A", file=f)
    export_report(out, file=f)
    assert out.exists()
    assert "ST001" in out.read_text()


def test_name_with_comma_is_kept(tmp_path):
    f = tmp_path / "att.csv"
    mark_attendance("ST001", "Doe, John", file=f)
    assert get_report(file=f).loc[0, "student_name"] == "Doe, John"
