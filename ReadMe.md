# Hydro Power Plant Dashboard - Flask Application

This is a Flask conversion of your HTML/CSS/JS hydro power plant dashboard with enhanced backend functionality.

## Project Structure

```
hydro_flask_app/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── templates/                      # HTML templates
│   ├── base.html                  # Base template with common layout
│   ├── index.html                 # Home page
│   ├── dashboard.html             # Real-time dashboard
│   ├── crack_detection.html       # Image upload and processing
│   ├── map_system.html            # Interactive map with markers
│   └── surveillance.html          # Security monitoring system
├── static/                        # Static files
│   ├── css/                       # Additional CSS files (if needed)
│   ├── js/                        # Additional JavaScript files
│   ├── images/                    # Dam images (dam1.jpg, dam2.jpg, dam3.jpg)
│   └── uploads/                   # Uploaded files for crack detection
└── README.md                      # This file
```

## Installation & Setup

### 1. Create Project Directory
```bash
mkdir hydro_flask_app
cd hydro_flask_app
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create Directory Structure
```bash
mkdir templates static static/css static/js static/images static/uploads
```

### 5. Add Your Images
Copy your dam images to the `static/images/` directory:
- `dam1.jpg`
- `dam2.jpg` 
- `dam3.jpg`

### 6. Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Features

### 🏠 Home Page (`/`)
- Project overview and features
- Rotating slideshow of dam images
- Navigation to all modules

### 📊 Dashboard (`/dashboard`)
- Real-time power output monitoring
- Water flow measurements
- Integrity status tracking
- Anomaly detection system
- Auto-refresh every 5 seconds

### 🔍 Crack Detection (`/crack-detection`)
- Image upload functionality
- Client-side image processing (grayscale conversion)
- Simulated AI crack detection
- Download processed images
- Results display with confidence scores

### 🗺️ Map System (`/map-system`)
- Interactive Leaflet map
- Google Maps embed as fallback
- Click-to-mark inspection points
- Simulated crack location markers
- Multiple map types (standard/topographic)

### 📹 Surveillance (`/surveillance`)
- Live camera feed simulation
- Motion detection alerts
- Security breach notifications
- Recording controls
- Alert logging system

## API Endpoints

### Dashboard APIs
- `GET /api/dashboard-data` - Get real-time dashboard metrics
- `POST /api/check-anomalies` - Manual anomaly detection

### Crack Detection APIs
- `POST /api/upload-image` - Upload image for processing
- `POST /api/process-crack-detection` - Process uploaded image

## Key Improvements Over Static Version

1. **Backend Processing**: Real server-side image handling
2. **API Integration**: RESTful endpoints for data exchange
3. **Real-time Updates**: Live dashboard data updates
4. **File Upload**: Proper file handling for crack detection
5. **Session Management**: Flask session support
6. **Scalable Architecture**: Easy to add new features
7. **Error Handling**: Comprehensive error management
8. **Loading States**: User feedback during operations

## Customization

### Adding New Pages
1. Create a new template in `templates/`
2. Add a route in `app.py`
3. Update navigation in `base.html`

### Adding New APIs
1. Add route handler in `app.py`
2. Return JSON responses for AJAX calls
3. Handle errors appropriately

### Styling Changes
- Modify CSS in `base.html` or create separate CSS files in `static/css/`
- All original styling has been preserved and enhanced

## Production Deployment

For production deployment, consider:

1. **Environment Variables**: Use environment variables for configuration
2. **Database**: Add PostgreSQL or MySQL for data persistence
3. **Security**: Implement authentication and CSRF protection
4. **File Storage**: Use cloud storage for uploaded images
5. **Caching**: Add Redis for session management
6. **Monitoring**: Implement logging and monitoring

### Example Production Configuration
```python
# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or 'static/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
```

## Troubleshooting

### Common Issues

1. **Port already in use**: Change port in `app.py` or kill existing process
2. **Images not loading**: Ensure images are in `static/images/` directory
3. **Upload errors**: Check file permissions on `static/uploads/` directory
4. **Module not found**: Ensure virtual environment is activated

### Debug Mode
The application runs in debug mode by default. For production, set:
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.