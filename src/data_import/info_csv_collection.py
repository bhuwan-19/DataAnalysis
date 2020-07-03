import pandas as pd
import os

from settings import CSV_FILE_PATH, LOCAL, CUR_DIR


class ParTemp:

    def __init__(self):

        self.date_remote_par_temp = pd.read_csv(CSV_FILE_PATH, index_col=False)

    def extract_info_by_sensor(self, remote_id):

        remote_df = self.date_remote_par_temp.loc[self.date_remote_par_temp["remote_id"] == remote_id, ["date", "par",
                                                                                                        "temp"]]
        if LOCAL:
            tmp_file_path = os.path.join(CUR_DIR, "temp", "temp_{}.csv".format(remote_id))
            remote_df.to_csv(tmp_file_path, index=False, header=True)

        return remote_df


if __name__ == '__main__':

    par_temp = ParTemp()
    par_temp.extract_info_by_sensor(remote_id=62102)
