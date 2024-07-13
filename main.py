from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
# import cv2
import os

from carbon import prediction
from sampah import pre_pre

app = Flask(__name__)
CORS(app)

@app.route('/sampah', methods=['POST'])
def sampah():
#     img_param = request.args.get('img')
    img_param = request.form['img']
    res = pre_pre(img_param)
    print("Typenya adalah ", type(img_param))
    try:
        data = {
            'code': 200,
            'message': 'Berhasil memprediksi!',
            'prediksi': res
        }
        
        return make_response(jsonify(data)), 200
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    

@app.route('/carbons', methods=['POST'])
def carbons():
#     img_param = request.args.get('img')
    electriccity = request.form['electriccity']
    gas = request.form['gas']
    transportation = request.form['transportation']
    food = request.form['food']
    organic_waste = request.form['organic_waste']
    inorganic_waste = request.form['inorganic_waste']
    food_type = request.form['food_type']
    
    print(food_type)
    res = prediction(float(electriccity), float(gas), float(transportation), float(food), float(organic_waste), float(inorganic_waste), food_type)
    try:
        data = {
            'code': 200,
            'message': 'Berhasil memprediksi!',
            'prediksi': float(f"{res:.2f}")
        }
        
        return make_response(jsonify(data)), 200
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)



@app.route('/test', methods=['GET'])
def test():
    return 'Hallow ddd'

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)
