import pandas as pd
import os
import numpy as np

from datetime import timedelta
from settings import START_DATE, END_DATE, LOCAL, CUR_DIR, NORMALIZE_INDEX


def split_df_by_date(d_frame):

    daily_df = {}
    d_frame["date"] = d_frame["date"].astype('datetime64[ns]')

    delta = timedelta(days=1)
    for single_date in pd.date_range(START_DATE, END_DATE):
        day_str = single_date.strftime("%Y-%m-%d")
        daily_df[day_str] = d_frame.loc[(d_frame["date"] >= single_date) & (d_frame["date"] < single_date + delta)]

        if LOCAL:
            tmp_sub_df_path = os.path.join(CUR_DIR, 'temp', "temp_{}.csv".format(day_str))
            daily_df[day_str].to_csv(tmp_sub_df_path, index=False, header=True)

    return daily_df


def calculate_daily_info(day_df):

    day_df = day_df.reset_index(drop=True)

    time_series = []
    par_series = []
    temp_series = []

    day_df["date"] = day_df["date"].astype('datetime64[ns]')
    for i in range(len(day_df)):
        diff_time = (day_df["date"][i] - day_df["date"][0]).total_seconds()
        time_series.append(diff_time)
        par_series.append(day_df["par"][i])
        temp_series.append(day_df["temp"][i])

    par_integral = np.trapz(par_series, time_series) / NORMALIZE_INDEX
    temp_integral = np.trapz(temp_series, time_series) / NORMALIZE_INDEX
    if temp_series:
        max_temp = max(temp_series)
        min_temp = min(temp_series)
    else:
        max_temp = 0
        min_temp = 0

    return par_integral, temp_integral, max_temp, min_temp


if __name__ == '__main__':

    df = pd.read_csv("")
    # split_df_by_date(d_frame=df)
    calculate_daily_info(day_df=df)
