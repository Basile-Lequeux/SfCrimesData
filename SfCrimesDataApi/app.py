from flask import Flask, request
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pickle

app = Flask(__name__)
labels = ['WARRANTS', 'OTHER OFFENSES', 'LARCENY/THEFT', 'VEHICLE THEFT',
       'VANDALISM', 'NON-CRIMINAL', 'ROBBERY', 'ASSAULT', 'WEAPON LAWS',
       'BURGLARY', 'SUSPICIOUS OCC', 'DRUNKENNESS', 'FORGERY/COUNTERFEITING',
       'DRUG/NARCOTIC', 'STOLEN PROPERTY', 'SECONDARY CODES', 'TRESPASS',
       'MISSING PERSON', 'FRAUD', 'KIDNAPPING', 'RUNAWAY',
       'DRIVING UNDER THE INFLUENCE', 'SEX OFFENSES FORCIBLE', 'PROSTITUTION',
       'DISORDERLY CONDUCT', 'ARSON', 'FAMILY OFFENSES', 'LIQUOR LAWS',
       'BRIBERY', 'EMBEZZLEMENT', 'SUICIDE', 'LOITERING',
       'SEX OFFENSES NON FORCIBLE', 'EXTORTION', 'GAMBLING', 'BAD CHECKS',
       'TREA', 'RECOVERED VEHICLE', 'PORNOGRAPHY/OBSCENE MAT']

loaded_model = pickle.load(open("../finalized_model.sav", 'rb'))

# dayofWeek, district, hour, month, year


@app.route("/predict/<day_of_week>/<district>/<int:hour>/<int:month>/<int:year>", methods=["GET"])
def predict(day_of_week, district, hour, month, year):
    array_day = build_day_of_week(day_of_week)
    array_district = build_district(district)
    date = [hour, month, year]
    res = array_day +  array_district + date
    predict = loaded_model.predict([res])
    print(predict)
    return f"{labels[predict[0]]}"


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
