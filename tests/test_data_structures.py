from datetime import datetime, timezone

import pytest


from bomapi import data_structures


@pytest.mark.parametrize(
    "date_string, expected",
    (
        (None, None),
        ("", None),
        (
            "2022-05-13T15:05:48Z",
            datetime(2022, 5, 13, 15, 5, 48, tzinfo=timezone.utc),
        ),
    ),
)
def test_parse_date(date_string, expected):
    actual = data_structures._parse_date(date_string)

    assert actual == expected
