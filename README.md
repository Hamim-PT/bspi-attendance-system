# APMS - Attendance & Practical Marks System

**Bangladesh Sweden Polytechnic Institute**  
**Computer Science & Technology Department**

A modern web-based attendance and sessional marks management system.

---

## 🌟 Features

- **Student Attendance Management**
- **Sessional Marks Tracking**
- **Subject-wise Management**
- **Responsive & Modern UI**
- **Easy to Use Interface**
- **Real-time Data**

---

## 🛠 Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (Development)
- **Styling**: Modern Glassmorphism + Gradient Design

---

## 📸 Screenshots

<img width="1357" height="657" alt="image" src="https://github.com/user-attachments/assets/43394814-ce91-4ac4-8e1d-b2d65346da07" />
<img width="1360" height="653" alt="image" src="https://github.com/user-attachments/assets/08733094-2f5f-4247-8e8a-7886adf1b8cf" />



---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Hamim-PT/bspi-attendance-system.git
cd bspi-attendance-system
```
### 2. Create & Activate a Virtual Environment
```Bash
# Create the virtual environment
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on Mac/Linux:
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install django
```
### 4. Setup Database
``` bash
python manage.py migrate
python manage.py createsuperuser
```
### 5. Run Server
```bash
python manage.py runserver
```
Go to: http://127.0.0.1:8000/

### 📁 Project Structure
```bspi-attendance-system/
├── attendance/          # Main application logic (Views, Models, Forms)
├── core/                # Project configurations and settings
├── static/              # CSS styles, JavaScript files, and UI assets
├── templates/           # HTML templates for views
├── manage.py            # Django command-line utility
├── README.md            # Project documentation
└── db.sqlite3           # Local development database
```
### 📄 License
This project is for educational purposes.



