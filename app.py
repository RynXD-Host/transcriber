from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_json():
    data = {
        'status': 'active',
        'creator': 'RynXD',
        'space': 'Penafsiran'
    }

    return jsonify(data)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and file.filename.endswith('.opus'):
        file_path = os.path.join(file.filename)
        file.save(file_path)
        #####
        script_js = os.path.join('convert.js')
        command = ['node', script_js, file_path, output_file]
        resultjs = subprocess.run(command, capture_output=True, text=True)
        
        #####
        # Execute another script with the file path as argument
        script_py = os.path.join('process_opus.py')
        resultpy = subprocess.run(['python', script_py, 'result.mp3'], capture_output=True, text=True)
        
        return jsonify({"message": f"{resultpy.stdout}"}), 200
    else:
        return jsonify({"error": "Invalid file format. Only .opus files are allowed."}), 400

output_file = os.path.join('result.mp3')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860, debug=True)
    