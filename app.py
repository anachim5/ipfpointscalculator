from flask import Flask, render_template, request
from numpy import log as ln

import math
def negative(number):
    return number*-1

app = Flask(__name__)

# Coefficients from the IPF GL document for classic (raw) powerlifting
COEFFICIENTS = {
    'man': {
        '3-lift': {'A': 1199.72839, 'B': 1025.18162, 'C': 0.00921},
        'bench': {'A': 320.98041, 'B': 281.40258, 'C': 0.01008}
    },
    'woman': {
        '3-lift': {'A': 610.32796, 'B': 1045.59282, 'C':0.03048},
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

if __name__ == '__main__':
    app.run(debug=True)