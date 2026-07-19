import json
import os
from config import USERS_FILE


def calculate_bmi(height, weight):
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        return round(bmi, 2)
    
def get_bmi_category(bmi):

        if bmi < 18.5:
            return "Underweight"

        elif bmi < 25:
            return "Normal"

        elif bmi < 30:
            return "Overweight"

        else:
            return "Obese"


def load_users():
        if not os.path.exists(USERS_FILE):
            return []

        try:
            with open(USERS_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []


def save_users(users):
        with open(USERS_FILE, "w") as file:
            json.dump(users, file, indent=4)


def validate_age(age):
        return 1 <= age <= 120


def validate_height(height):
        return 50 <= height <= 250


def validate_weight(weight):
        return 10 <= weight <= 400


def generate_user_id(users):
        if not users:
            return "U001"

        last_id = users[-1]["user_id"]
        number = int(last_id[1:])
        return f"U{number + 1:03}"