from datetime import datetime, timedelta


def round_time_down(time: datetime, interval: timedelta) -> datetime:
    """
    Round down the given time based on the given interval.

    Parameters:
    The original datetime object.
    interval: The interval to round down to.

    Returns:
    The rounded-down time based on the given interval.

    Examples:
    >>> rounde_time_down(datetime(2021, 1, 1, 0, 0), timedelta(minutes=5))
    datetime.datetime(2021, 1, 1, 0, 0)
    """

    return datetime.fromtimestamp(
        time.timestamp() // interval.total_seconds() * interval.total_seconds()
    )


def round_time_up(time: datetime, interval: timedelta) -> datetime:
    """
    Round up the given time based on the given interval.

    Parameters:
    time: The original datetime object.
    interval: The interval to round up to.

    Returns:
    The rounded-up time based on the given interval.

    """

    base_time = round_time_down(time, interval)
    if base_time < time:
        return base_time + interval
    return base_time
