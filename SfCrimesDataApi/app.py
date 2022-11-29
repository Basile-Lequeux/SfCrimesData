from flask import Flask, request
import numpy as np

app = Flask(__name__)


# dayofWeek, district, hour, month, year


@app.route("/predict/<day_of_week>/<district>/<int:hour>/<int:month>/<int:year>", methods=["GET"])
def predict(day_of_week, district, hour, month, year):
    array_day = build_day_of_week(day_of_week)
    array_district = build_district(district)
    props_array = np.append(array_day, array_district)
    date = [hour, month, year]
    res = np.append(props_array, date)
    

    return f'{res}'


def build_day_of_week(day_of_week):
    day_lower = day_of_week.lower()
    if day_lower == "monday":
        return [0, 1, 0, 0, 0, 0, 0]
    if day_lower == "tuesday":
        return [0, 0, 0, 0, 0, 1, 0]
    if day_lower == "wednesday":
        return [0, 0, 0, 0, 0, 0, 1]
    if day_lower == "thursday":
        return [0, 0, 0, 0, 1, 0, 0]
    if day_lower == "friday":
        return [1, 0, 0, 0, 0, 0, 0]
    if day_lower == "saturday":
        return [0, 0, 1, 0, 0, 0, 0]
    if day_lower == "sunday":
        return [0, 0, 0, 1, 0, 0, 0]
    else:
        return [0, 1, 0, 0, 0, 0, 0]


def build_district(district):
    district_lower = district.lower()
    if district_lower == "bayview":
        return [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if district_lower == "central":
        return [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    if district_lower == "ingleside":
        return [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    if district_lower == "mission":
        return [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    if district_lower == "northern":
        return [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    if district_lower == "park":
        return [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    if district_lower == "richmond":
        return [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    if district_lower == "southern":
        return [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    if district_lower == "taraval":
        return [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    if district_lower == "tenderloin":
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    else:
        return [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]


if __name__ == '__main__':
    app.run()
