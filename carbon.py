from joblib import load
import numpy as np



filename = 'carbons.joblib'
model = load(filename)


def prediction(electriccity, gas, transportation, food, organic_waste, inorganic_waste, food_type):
    try:
        data = [
            ("Daging Sapi", 2),
            ("Daging Ayam", 1),
            ("Ikan", 3),
            ("Susu", 6),
            ("Telur", 7),
            ("Sayuran", 5),
            ("Buah", 0),
            ("Kacang", 4)
        ]
        for item in data:
            if food_type == item[0]:
                food_type =  item[1]
                input_data = np.array([[electriccity, gas, transportation, food, organic_waste, inorganic_waste, food_type]], dtype='object')
                prediction = model.predict(input_data)
                return prediction[0]
    except Exception as e:
        print(e)




