🧪 Chemical Equipment Data Analyzer
📌 Project Overview

The Chemical Equipment Data Analyzer is a full-stack application designed to analyze, manage, and visualize chemical equipment data efficiently.
This system works in two formats:

✅ Web Application (Browser-based)
✅ Desktop Application (Standalone Software)

Both applications are connected to a single Django-based backend server, ensuring centralized data processing and storage.

🎯 Project Objective

The main goal of this project is to build a unified platform that allows users to:

Upload equipment data using CSV files

Store and manage chemical equipment records

Analyze equipment data efficiently

Access the system from both web and desktop environments

🏗 System Architecture
Desktop App  →  
                → Django REST API → Database
Web App      →


Both clients communicate with the same backend API.

⚙ Tech Stack
🔙 Backend

Django

Django REST Framework

SQLite (Development Database)

🌐 Web Frontend

(Your frontend — React / HTML / JS — you can edit later)

💻 Desktop Application

(Your desktop tech — PyQt / Electron / Tkinter — edit later)

📂 Key Features

✔ CSV File Upload
✔ Equipment Data Storage
✔ REST API Integration
✔ Cross-Platform Access (Web + Desktop)
✔ Centralized Backend Server

📊 Example CSV Format
name,price,quantity
Tractor,500000,5
Pump,20000,10
Sensor,5000,20

🚀 How to Run Backend (Django)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Server will run at:

http://127.0.0.1:8000/

📡 API Endpoint Example
Upload CSV
POST /api/upload-csv/


Body → form-data
Key → file
Value → CSV File

👨‍💻 Author

Intern Project – Chemical Equipment Data Analyzer
