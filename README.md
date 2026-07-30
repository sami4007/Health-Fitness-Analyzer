# 🏃 Health Fitness Analyzer

A desktop-based **Health Fitness & Calorie Tracker** built with **Python** and **Tkinter** following the **Model-View-Controller (MVC)** architecture.

The application allows users to manage health profiles, record daily health activities, track calorie intake, and analyze health data through four integrated dashboards.

---

## 📌 Features

### 👤 User Management Dashboard
- Add new users
- Update user information
- Delete users
- Search users by ID
- View all users
- Automatic BMI calculation

---

### ❤️ Health Dashboard
- Record daily health information
- Track water intake
- Track exercise duration
- Track sleep hours
- Generate health recommendations
- Save daily health records

---

### 🍎 Calorie Dashboard
- Food database lookup
- Calculate meal calories
- Track daily calorie intake
- Display remaining calories
- Generate daily nutrition summary

---

### 📊 Analytics Dashboard
- Average BMI
- Average Age
- Highest & Lowest BMI
- Gender Distribution
- Health Status Distribution
- Statistical analysis using NumPy

---

# 🏗️ Project Structure

```
Health-Fitness-Analyzer/
│
├── assets/
│   └── themes/
│       └── style.py
│
├── controllers/
│   ├── analytics_controller.py
│   ├── calorie_controller.py
│   ├── health_controller.py
│   └── user_controller.py
│
├── dashboards/
│   ├── analytics_dashboard.py
│   ├── calorie_dashboard.py
│   ├── health_dashboard.py
│   └── user_dashboard.py
│
├── data/
│   ├── daily_records.json
│   ├── daily_summary.json
│   ├── enhanced_health_data.csv
│   ├── food_database.json
│   ├── health_data.json
│   └── users.json
│
├── models/
│   ├── daily_record.py
│   ├── daily_summary.py
│   ├── food.py
│   ├── health_record.py
│   └── user.py
│
├── app.py
├── config.py
├── main.py
└── utils.py
```

---

# 🧩 MVC Architecture

The project follows the **Model-View-Controller (MVC)** architecture.

### Model
Responsible for managing application data.

- User
- Health Record
- Daily Record
- Food
- Daily Summary

---

### View

The user interface is divided into four dashboards.

- User Dashboard
- Health Dashboard
- Calorie Dashboard
- Analytics Dashboard

---

### Controller

Controllers process user actions and connect the dashboards with the models.

- User Controller
- Health Controller
- Calorie Controller
- Analytics Controller

---

## 🔄 System Workflow

```
User

   │

   ▼

Dashboard (View)

   │

   ▼

Controller

   │

   ▼

Model

   │

   ▼

JSON / CSV Data

   │

   ▼

Updated Dashboard
```

---

# 💾 Data Storage

The application stores data using **JSON** files.

- users.json
- health_data.json
- daily_records.json
- daily_summary.json
- food_database.json

A CSV dataset is used for population health analysis.

- enhanced_health_data.csv

---

# 🛠️ Technologies Used

- Python
- Tkinter
- NumPy
- JSON
- CSV
- Object-Oriented Programming (OOP)
- MVC Architecture

---

# 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/sami4007/Health-Fitness-Analyzer.git
```

### Navigate to the project folder

```bash
cd Health-Fitness-Analyzer
```

### Install dependencies

```bash
pip install numpy
```

### Run the application

```bash
python main.py
```

---

# 🎯 Learning Outcomes

This project demonstrates:

- Python GUI development using Tkinter
- Model-View-Controller (MVC) Architecture
- Object-Oriented Programming
- JSON and CSV data handling
- NumPy statistical analysis
- Desktop application development

---

