import pandas as pd
import os
import numpy as np

from random import *
from datetime import timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
from matplotlib import ticker as mticker
from src.data_import.info_excel_collection import Sensor
from src.data_import.info_csv_collection import ParTemp
from src.data_process.daily_data import split_df_by_date, calculate_daily_info
from settings import START_DATE, END_DATE, PLOT_DIR_PATH


def analyze_relationship_by_plot():
    sensor_data = Sensor()
    par_temp_data = ParTemp()
    print("Sensor data input...")
    sensors = sensor_data.collect_sensors_in_csv()

    x_dates = pd.date_range(START_DATE, END_DATE)

    par_plot_info = {}
    temp_plot_info = {}
    temp_max_min_plot_info = {}
    flowering_info = {}

    for sensor in sensors:

        print("Calculate Integral of Light and Temperature, Max and Min Temperature value...")
        flowering_time = sensor_data.collect_gtype_flowering_time(sensor_id=sensor)
        flowering_date = []
        for flowering in flowering_time:
            flowering_dt = START_DATE + timedelta(days=flowering)
            flowering_date.append(flowering_dt)

        flowering_info[str(sensor)] = flowering_date
        sensor_df = par_temp_data.extract_info_by_sensor(remote_id=sensor)
        sensor_daily_df = split_df_by_date(d_frame=sensor_df)

        pars = []
        temps = []
        max_temps = []
        min_temps = []

        for date_ in sensor_daily_df:

            par_integral, temp_integral, max_temp, min_temp = calculate_daily_info(day_df=sensor_daily_df[date_])
            if not pars:
                pars.append(par_integral)
            else:
                pars.append(par_integral + pars[-1])
            if not temps:
                temps.append(temp_integral)
            else:
                temps.append(temp_integral + temps[-1])
            max_temps.append(max_temp)
            min_temps.append(min_temp)

        par_plot_info[str(sensor)] = pars
        temp_plot_info[str(sensor)] = temps
        temp_max_min_plot_info[str(sensor) + "_max"] = max_temps
        temp_max_min_plot_info[str(sensor) + "_min"] = min_temps

    print("Plot graph...")

    plot_analysis_graph(x=x_dates, y_dict=par_plot_info, y_label="Light Integral (mol/m2)", title="Light_Integral_day",
                        flower_date=flowering_info, margin_left=1, margin_right=4)
    plot_analysis_graph(x=x_dates, y_dict=temp_plot_info, y_label="Temperature Integral ($^\circ$C d)",
                        title="Temperature_Integral_day", flower_date=flowering_info, margin_left=1, margin_right=4)
    plot_analysis_graph(x=x_dates, y_dict=temp_max_min_plot_info, y_label="Max Min Temperature ($^\circ$C)",
                        title="Max_Min_Temperature", flower_date=None, margin_left=0, margin_right=2)


def plot_analysis_graph(x, y_dict, y_label, title, flower_date, margin_left, margin_right):
    plot_file_path = os.path.join(PLOT_DIR_PATH, "{}.png".format(title))

    months = mdates.MonthLocator()  # every month
    days = mdates.DayLocator()
    years__month_fmt = mdates.DateFormatter('%Y-%m')

    plt.gca().xaxis.set_major_locator(months)
    plt.gca().xaxis.set_major_formatter(years__month_fmt)
    plt.gca().xaxis.set_minor_locator(days)
    plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d '))
    for i, y in enumerate(y_dict):
        colors = (random(), random(), random())
        if flower_date is not None:
            if i == 0:
                plt.plot(flower_date[y][0], y_dict[y][-1], 'b*--', label="Gtype1")
                plt.plot(flower_date[y][1], y_dict[y][-1], 'g*--', label="Gtype2")
                plt.plot(flower_date[y][2], y_dict[y][-1], 'r*--', label="Gtype3")
            else:
                plt.plot(flower_date[y][0], y_dict[y][-1], 'b*--')
                plt.plot(flower_date[y][1], y_dict[y][-1], 'g*--')
                plt.plot(flower_date[y][2], y_dict[y][-1], 'r*--')

            max_date = max(flower_date[y])
            xx = pd.date_range(END_DATE, max_date)
            plt.plot(xx, [y_dict[y][-1]] * len(xx), "--", color=colors)

        plt.plot(x, y_dict[y], color=colors, label=y)

    date_min = np.datetime64(START_DATE, 'M') - np.timedelta64(margin_left, 'M')
    date_max = np.datetime64(END_DATE, 'M') + np.timedelta64(margin_right, 'M')
    plt.gca().set_xlim(date_min, date_max)

    plt.gcf().autofmt_xdate()

    plt.xlabel("Date")
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.savefig(plot_file_path)
    plt.show()


if __name__ == '__main__':
    analyze_relationship_by_plot()
