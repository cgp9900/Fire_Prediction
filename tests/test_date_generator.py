import datetime

import pandas as pd

from fire import date_generator


def test_random_date_one_return():
    pd_input_dates = pd.DataFrame(
        data={
            "date": [
                datetime.datetime(2023, 7, 9, 0, 0),
                datetime.datetime(2023, 7, 11, 0, 0),
            ]
        }
    )
    returned_dates = date_generator.rand_date(pd_input_dates, 1)
    returned_dates = returned_dates[0]

    assert returned_dates == datetime.datetime(2023, 7, 10, 0, 0)


def test_random_date_excluded():
    pd_input_dates_consecutive = pd.DataFrame(
        data={
            "date": [
                datetime.datetime(2023, 7, 8, 0, 0),
                datetime.datetime(2023, 7, 9, 0, 0),
                datetime.datetime(2023, 7, 10, 0, 0),
                datetime.datetime(2023, 7, 11, 0, 0),
            ]
        }
    )

    assert "No differing dates found"
