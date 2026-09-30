from modules import database


def test_required_tables_exist():
    tables = {
        row[0]
        for row in database.cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()
    }

    assert "events" in tables
    assert "students" in tables
    assert "registrations" in tables
