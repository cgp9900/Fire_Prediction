from datetime import datetime
from datetime import timedelta
import numpy as np
import pandas as pd

def rand_date(input_df, record_length=2000):
    minimum_date = input_df[
        "date"
    ].min()  # Initializing range of dates associated with df
    maximum_date = input_df["date"].max()

    listed_date = []  # Initializing list of dates
    new_dates = []

    minimum_date += timedelta(days=1)
    while minimum_date != maximum_date:  # All dates not associated with fires
        if minimum_date in input_df["date"].values:
            minimum_date += timedelta(days=1)
        else:
            listed_date.append(minimum_date)
            minimum_date += timedelta(days=1)
    if len(listed_date) > 0:
        for i in range(
            record_length
        ):  # Random generation of dates not associated with fire
            rand_num = np.random.randint(0, len(listed_date))
            curr_date = listed_date[rand_num]
            new_dates.append(curr_date)
            return pd.Series(new_dates)
    else:
        return "No differing dates found"
