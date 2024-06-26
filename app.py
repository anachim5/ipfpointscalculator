from flask import Flask, render_template, request,jsonify
from numpy import log as ln

import math
def negative(number):
    return number*-1

app = Flask(__name__)

# Coefficients from the IPF GL document for classic (raw) powerlifting
COEFFICIENTS = {
    'man': {
        'powerlifting': {'A': 1199.72839, 'B': 1025.18162, 'C': 0.00921},
        'bench': {'A': 320.98041, 'B': 281.40258, 'C': 0.01008}
    },
    'woman': {
        'powerlifting': {'A': 610.32796, 'B': 1045.59282, 'C':0.03048},
        'bench': {'A': 142.40398, 'B': 204.94518, 'C': 0.04724}
    }
}

def calculate_ipf_gl_points(total, bodyweight, gender, lift_type):
    coeff = COEFFICIENTS[gender][lift_type]
    ipf_coefficient = 100 / (coeff['A'] - coeff['B'] * math.pow(math.e,(-coeff['C']*bodyweight)))
    points = total * ipf_coefficient
    return round(points, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        total = float(request.form['total'])
        bodyweight = float(request.form['bodyweight'])
        gender = request.form['gender']
        lift_type = request.form['lift_type']
        result = calculate_ipf_gl_points(total, bodyweight, gender, lift_type)
    return render_template('index.html', result=result)

@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    data = request.json
    if not data or 'total' not in data or 'bodyweight' not in data or 'sex' not in data or 'lift_type' not in data:
        return jsonify({"error": "Missing required parameters"}), 400
    
    total = float(data['total'])
    bodyweight = float(data['bodyweight'])
    sex = data['sex'].lower()
    lift_type = data['lift_type'].lower()
    
    if sex not in ['man', 'woman']:
        return jsonify({"error": "Invalid sex parameter. Must be 'man' or 'woman'"}), 400
    
    if lift_type not in ['powerlifting', 'bench']:
        return jsonify({"error": "Invalid lift_type parameter. Must be 'powerlifting' or 'bench'"}), 400
    
    points = calculate_ipf_gl_points(total, bodyweight, sex, lift_type)
    
    return jsonify({
        "points": points,
        "total": total,
        "bodyweight": bodyweight,
        "sex": sex,
        "lift_type": lift_type
    })

if __name__ == '__main__':
    app.run(debug=True)