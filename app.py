from flask import Flask, render_template, request
from model import predict_resume
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'resume' not in request.files:
        return 'No file uploaded'

    file = request.files['resume']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    result = predict_resume(filepath)

    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
