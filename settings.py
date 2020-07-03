import os
import datetime

from utils.folder_file_manager import make_directory_if_not_exists

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE_PATH = os.path.join(CUR_DIR, 'utils', 'Rudolf_2019_season.csv')
EXCEL_FILE_PATH = os.path.join(CUR_DIR, 'utils', 'Rudolf_2019_remote_id_to_floweringdays.xlsx')
PLOT_DIR_PATH = make_directory_if_not_exists(os.path.join(CUR_DIR, 'plot'))

START_DATE = datetime.datetime(2019, 3, 14)
END_DATE = datetime.datetime(2019, 5, 20)
NORMALIZE_INDEX = 1000000
LOCAL = False
