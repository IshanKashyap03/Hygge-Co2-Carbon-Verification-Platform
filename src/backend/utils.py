from datetime import datetime


def is_float(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


def issue_date_to_datetime(issue_date: str) -> datetime:
    """Converts the issue date to a datetime object"""
    return datetime.strptime(issue_date, "%Y-%m-%dT%H:%M:%S.%f")


def start_end_date_to_datetime(date_str: str) -> datetime:
    """Converts the date string used for the start and end dates to a datetime object"""
    return datetime.strptime(date_str, "%B %d, %Y %H:%M")


def start_end_datetime_to_str(date: datetime) -> str:
    return date.strftime("%B %d, %Y %H:%M")


def main():
    # TODO: Add proper testing framework (Pytest)
    issue_date = "2024-05-28T17:41:58.300626"
    assert issue_date_to_datetime(issue_date) == datetime(
        2024, 5, 28, 17, 41, 58, 300626
    )
    start_date = "May 01, 2024 00:00"
    start_datetime = start_end_date_to_datetime(start_date)
    assert start_datetime == datetime(2024, 5, 1, 0, 0, 0, 0)
    assert start_end_datetime_to_str(start_datetime) == "May 01, 2024 00:00"

    end_date = "May 28, 2024 21:34"
    end_datetime = start_end_date_to_datetime(end_date)
    assert end_datetime == datetime(2024, 5, 28, 21, 34, 0, 0)
    assert start_end_datetime_to_str(end_datetime) == "May 28, 2024 21:34"
    print("All tests passed successfully.")


if __name__ == "__main__":
    main()
