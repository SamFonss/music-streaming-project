# Music Streaming System with Network Optimization
Welcome to my Music Streaming System repository! This project is a music streaming platform that allows users to upload, stream, and download audio files. It is designed to optimize network efficiency using routing protocols and network monitoring, ideal for users interested in high-performance audio streaming.

# Features

**User Authentication**: Secure login system with permissions management to control user access levels (view-only, upload permissions, guest access).

**Audio Upload and Streaming**: Users can upload audio files and stream files directly from the platform.

**Download Functionality**: Users can download audio files from the server.

**Network Optimization**: Incorporates BGP/OSPF concepts to ensure optimized routing and efficient data flow.

**Automated Traffic Monitoring**: Scripts for real-time monitoring of network traffic to maintain and troubleshoot optimal performance.


**Project Structure**

```
music_streaming/
│
├── core/
│   ├── templates/
│   │   ├── registration/
│   │   │   ├── login.html            # Login page
│   │   │   ├── password_change.html  # Password change page
│   │   │   └── password_reset.html   # Password reset page
│   │   │
│   │   ├── menu.html             # Main menu for browsing/uploading files
│   │   ├── upload.html           # File upload page
│   │   └── browse.html           # File browsing and streaming page
│   │         
│   ├── models.py             # Database models, including audio file metadata
│   ├── views.py              # Views for file upload, browsing, and streaming
│   └── forms.py              # Forms for user inputs and file uploads
│   
├── music_streaming/
│   ├── settings.py           # Django project configuration settings
│   └── urls.py               # Project URL routing 
│ 
├── manage.py                 # Django project management tool
├── README.md                 # Project documentation
└── requirements.txt          # Dependencies
```
# Getting Started

**Prerequisites**

```
Python 3.8+
Django 4.0+
PostgreSQL (with initial setup for network optimization testing)
Git for version control
```
# Installation

**Clone the Repository
**
```
git clone https://github.com/SamFonss/music-streaming-project.git
cd music-streaming-project
```
**Create a Virtual Environment
**
```
python3 -m venv venv
source venv/bin/activate
```
**Install Dependencies
**
```
pip install -r requirements.txt
```
**Set Up Database
**
Configure PostgreSQL in settings.py:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'music_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
**Apply Migrations
**
```
python manage.py migrate
```
**Run the Server
**
```
python manage.py runserver
```
# Usage

**User Registration and Login**

Register and log in to access upload/browse functionalities.

**Guest Access**

Continue as a guest to browse files without upload permissions.

**Uploading and Streaming**

Logged-in users with upload permissions can add audio files to the platform.
All users can stream and download audio files.

**Network Optimization**

This project utilizes TCP/IP for primary data transfer and applies Border Gateway Protocol (BGP) and Open Shortest Path First (OSPF) concepts to optimize routing in simulated network scenarios. It includes scripts for traffic monitoring and troubleshooting.

**Traffic Monitoring**

The project provides shell scripts to monitor network activity on the server. You can run these scripts to see real-time traffic metrics, helping maintain efficient routing and performance.

**Contributions**

Contributions are welcome! If you want to contribute, please open an issue or submit a pull request.

# License

MIT License

# Contact
For questions or further collaboration, please reach out via GitHub Issues or email at samfonss@gmail.com.
