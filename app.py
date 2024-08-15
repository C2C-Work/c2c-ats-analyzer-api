from flask import Flask, request, jsonify
from flask_cors import CORS
from concurrent.futures import ThreadPoolExecutor, as_completed
import calculations
import api_work
app = Flask(__name__)

# Configure CORS with specific options
cors = CORS(app, resources={
    r"/submit": {"origins": "*"}  # Allow all origins for the /submit endpoint
})



@app.route('/submit', methods=['POST'])
def submit():
    file_name = request.args.get('fileName', '')
    file_type = request.args.get('fileType', '')
    job_description = request.args.get('job_description', '')
    additional_information = request.args.get('additional_information', '')
    experience = request.args.get('experience', '')
    extracted_text = request.args.get('ext-text', '')
    
    output = api_work.get_data(job_description, additional_information, experience, extracted_text)
    return output

if __name__ == '__main__':
    app.run(debug=True)
