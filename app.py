from flask import Flask, render_template, request, jsonify, send_file
import os
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import random
import time

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Routes for different pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/crack-detection')
def crack_detection():
    return render_template('crack_detection.html')

@app.route('/map-system')
def map_system():
    return render_template('map_system.html')

@app.route('/surveillance')
def surveillance():
    return render_template('surveillance.html')

# API Routes
@app.route('/api/dashboard-data')
def get_dashboard_data():
    """API endpoint to get real-time dashboard data"""
    power_output = round(480 + random.random() * 40, 1)
    water_flow = round(290 + random.random() * 20, 1)
    
    # Simulate anomaly detection
    has_anomaly = random.random() > 0.7
    integrity_status = "Anomaly Detected" if has_anomaly else "Normal"
    
    return jsonify({
        'power_output': f"{power_output} MW",
        'water_flow': f"{water_flow} m³/s",
        'integrity_status': integrity_status,
        'has_anomaly': has_anomaly,
        'timestamp': time.time()
    })

@app.route('/api/check-anomalies', methods=['POST'])
def check_anomalies():
    """API endpoint to manually check for anomalies"""
    has_anomaly = random.random() > 0.7
    integrity_status = "Anomaly Detected" if has_anomaly else "Normal"
    
    return jsonify({
        'has_anomaly': has_anomaly,
        'integrity_status': integrity_status,
        'message': 'Anomaly detected in turbine!' if has_anomaly else 'System operating normally'
    })

@app.route('/api/upload-image', methods=['POST'])
def upload_image():
    """API endpoint to handle image upload for crack detection"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        try:
            # Read image data
            image_data = file.read()
            
            # Convert to base64 for frontend display
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            
            return jsonify({
                'success': True,
                'image_data': f"data:image/jpeg;base64,{image_base64}",
                'message': 'Image uploaded successfully'
            })
        except Exception as e:
            return jsonify({'error': f'Error processing image: {str(e)}'}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/api/process-crack-detection', methods=['POST'])
def process_crack_detection():
    """API endpoint to process crack detection"""
    try:
        data = request.get_json()
        image_data = data.get('image_data')
        
        if not image_data:
            return jsonify({'error': 'No image data provided'}), 400
        
        # In a real application, you would implement actual crack detection here
        # For now, we'll simulate the process
        
        # Simulate processing time
        time.sleep(1)
        
        # Return processed result (in real app, this would be the actual processed image)
        return jsonify({
            'success': True,
            'processed_image': image_data,  # In real app, return processed image
            'cracks_detected': random.choice([True, False]),
            'confidence': round(random.uniform(0.7, 0.95), 2),
            'crack_count': random.randint(0, 5),
            'message': 'Crack detection completed'
        })
        
    except Exception as e:
        return jsonify({'error': f'Error in crack detection: {str(e)}'}), 500

def allowed_file(filename):
    """Check if uploaded file is allowed"""
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)