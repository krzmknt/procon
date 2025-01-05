import pytest
from datetime import datetime, timedelta
from .main import round_time_down, round_time_up

# ---------------------------
# round_time_down, round_time_up


def test_round_time_normal():
    assert round_time_down(datetime(2023, 9, 25, 10, 3), timedelta(minutes=5)) == datetime(
        2023, 9, 25, 10, 0
    )

    assert round_time_up(datetime(2023, 9, 25, 10, 3), timedelta(minutes=5)) == datetime(
        2023, 9, 25, 10, 5
    )

    assert round_time_down(datetime(2023, 9, 25, 10, 23), timedelta(minutes=15)) == datetime(
        2023, 9, 25, 10, 15
    )

    assert round_time_up(datetime(2023, 9, 25, 10, 23), timedelta(minutes=15)) == datetime(
        2023, 9, 25, 10, 30
    )

    assert round_time_down(datetime(2023, 9, 25, 10, 23), timedelta(minutes=60)) == datetime(
        2023, 9, 25, 10, 0
    )

    assert round_time_up(datetime(2023, 9, 25, 10, 23), timedelta(minutes=60)) == datetime(
        2023, 9, 25, 11, 0
    )


def test_round_time_rare_interval():
    assert round_time_down(datetime(2023, 9, 25, 10, 11), timedelta(minutes=3)) == datetime(
        2023, 9, 25, 10, 9
    )

    assert round_time_up(datetime(2023, 9, 25, 10, 11), timedelta(minutes=3)) == datetime(
        2023, 9, 25, 10, 12
    )


def test_round_time_edge():
    # POSIX time starts at 1970-01-01 00:00:00 UTC
    assert round_time_down(datetime(1970, 1, 1, 0, 0), timedelta(minutes=5)) == datetime(
        1970, 1, 1, 0, 0
    )

    assert round_time_up(datetime(1970, 1, 1, 0, 0), timedelta(minutes=5)) == datetime(
        1970, 1, 1, 0, 0
    )

    assert round_time_down(datetime(2023, 12, 31, 23, 59), timedelta(minutes=5)) == datetime(
        2023, 12, 31, 23, 55
    )

    assert round_time_up(datetime(2023, 12, 31, 23, 59), timedelta(minutes=5)) == datetime(
        2024, 1, 1, 0, 0
    )
