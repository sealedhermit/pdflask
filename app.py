from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16MB

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'file1' not in request.files or 'file2' not in request.files:
        return jsonify({'error': 'Files not provided'}), 400

    file1 = request.files['file1']
    file2 = request.files['file2']

    if file1.filename == '' or file2.filename == '':
        return jsonify({'error': 'Invalid filenames'}), 400

    filename1 = secure_filename(file1.filename)
    filename2 = secure_filename(file2.filename)

    file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
    file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))

    return jsonify({'message': 'Files uploaded successfully'}), 200

@app.route('/compare', methods=['POST'])
def compare_files():
    # Placeholder for comparison logic
    # Replace this with your actual comparison logic
    matched_data = [
        {'name': 'John', 'rank_exam_1': 3, 'rank_exam_2': 5},
        {'name': 'Emma', 'rank_exam_1': 1, 'rank_exam_2': 2},
    ]
    return jsonify(matched_data), 200

if __name__ == '__main__':
    app.run(debug=True)
