import pandas as pd

from settings import EXCEL_FILE_PATH


class Sensor:

    def __init__(self):
        self.sensor_flower_gtype = pd.read_excel(EXCEL_FILE_PATH, sheet_name="Sheet1")

    def collect_sensors_in_csv(self):

        sensors = []
        init_sensors = self.sensor_flower_gtype["Sensor"].values.tolist()
        for init_sensor in init_sensors:

            sensor_val = int(init_sensor)
            if sensor_val == 12679:
                continue
            if sensor_val not in sensors:
                sensors.append(sensor_val)

        return sensors

    def collect_gtype_flowering_time(self, sensor_id):

        gtype_flowering = []

        for i in range(1, 4):
            gtype_flowering.append(self.sensor_flower_gtype.loc[
                (self.sensor_flower_gtype["Sensor"] == float(sensor_id)) & (self.sensor_flower_gtype["Genotype"] == i),
                ["Flowering time"]].values.tolist()[0][0])

        return gtype_flowering


if __name__ == '__main__':

    sensor = Sensor()
    # sensor.collect_sensors_in_csv()
    sensor.collect_gtype_flowering_time(sensor_id=1823)
