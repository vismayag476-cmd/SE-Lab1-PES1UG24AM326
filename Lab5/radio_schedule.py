
"""Manage a simple radio station schedule."""

import sqlite3


def create_database():
    """Create and return an in-memory database for radio shows."""
    database = sqlite3.connect(":memory:")
    database.execute(
        """
        CREATE TABLE slots (
            id INTEGER PRIMARY KEY,
            show TEXT NOT NULL,
            host TEXT NOT NULL,
            start_hour INTEGER NOT NULL,
            minutes INTEGER NOT NULL
        )
        """
    )
    return database


def add_slot(database, show, host, start_hour, minutes):
    """Add a radio show to the schedule."""
    database.execute(
        """
        INSERT INTO slots (show, host, start_hour, minutes)
        VALUES (?, ?, ?, ?)
        """,
        (show, host, start_hour, minutes),
    )


def slot_label(show, host):
    """Return a formatted radio show label."""
    return f"{show} hosted by {host}"


def overlap_free(first_end_hour, second_start_hour):
    """Check whether two shows do not overlap."""
    return first_end_hour <= second_start_hour


def morning_shows(database):
    """Return all shows scheduled before noon."""
    return [
        row[0]
        for row in database.execute(
            "SELECT show FROM slots WHERE start_hour < 12"
        )
    ]


def remove_slot(database, slot_id):
    """Remove a radio show using its ID."""
    database.execute("DELETE FROM slots WHERE id = ?", (slot_id,))


def main():
    """Run a sample radio scheduling session."""
    database = create_database()

    add_slot(database, "Sunrise Beats", "Vik", 7, 60)
    add_slot(database, "Midday Talk", "Anu", 13, 45)

    print(slot_label("Sunrise Beats", "Vik"))
    print(overlap_free(8, 13), morning_shows(database))

    remove_slot(database, 2)
    database.close()


if __name__ == "__main__":
    main()
