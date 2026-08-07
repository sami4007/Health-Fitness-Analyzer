import json
import os
from models.health_record import User


DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "health_data.json")


class UserController:
    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
       
        if not os.path.exists(DATA_FILE):
            os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
            with open(DATA_FILE, "w") as f:
                json.dump([], f)
            return []
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def save_users(self):
      
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w") as f:
            json.dump(self.users, f, indent=4)

    def generate_user_id(self):
        if not self.users:
            return "U001"
        max_id = 0
        for user in self.users:
            uid = user.get("user_id", "U000")
            if uid.startswith("U"):
                try:
                    num = int(uid[1:])
                    if num > max_id:
                        max_id = num
                except ValueError:
                    pass
        return f"U{max_id + 1:03d}"

    def calculate_health_metrics(self, height, weight, age):
        bmi = weight / ((height / 100) ** 2)

        if bmi < 18.5:
            status = "Underweight"
            health_score = 65
            recommended_calories = 2500
            rec_message = """STATUS : UNDERWEIGHT

• Increase daily calorie intake by 300 kcal
• Eat protein-rich foods
• Strength training 3-4 days/week
• Drink at least 2.5L water daily
• Sleep 7-8 hours
• Maintain a balanced diet
"""
        elif bmi < 25:
            status = "Healthy"
            health_score = 100
            recommended_calories = 2200
            rec_message = """STATUS : HEALTHY

• Maintain your current weight
• Exercise 30 minutes daily
• Drink 2.5-3L water
• Eat a balanced diet
• Sleep 7-8 hours
• Continue healthy habits
"""
        elif bmi < 30:
            status = "Overweight"
            health_score = 80
            recommended_calories = 1800
            rec_message = """STATUS : OVERWEIGHT

• Walk at least 30 minutes daily
• Reduce 500 calories/day
• Avoid sugary drinks
• Eat more vegetables and fruits
• Drink plenty of water
• Exercise regularly
"""
        else:
            status = "Obese"
            health_score = 60
            recommended_calories = 1500
            rec_message = """STATUS : OBESE

• Consult a healthcare professional
• Follow a low-calorie diet
• Exercise 45-60 minutes daily
• Avoid fast food and soft drinks
• Drink at least 3L water
• Monitor your weight regularly
"""

        body_fat = (1.20 * bmi) + (0.23 * age) - 16.2
        water_need = weight * 0.035
        ideal_weight = 22 * ((height / 100) ** 2)

        return {
            "bmi": round(bmi, 2),
            "status": status,
            "health_score": health_score,
            "recommended_calories": recommended_calories,
            "body_fat": round(body_fat, 2),
            "water_need": round(water_need, 2),
            "ideal_weight": round(ideal_weight, 2),
            "recommendation": rec_message,
        }

    def add_user(self, name, gender, age, height, weight, calories, exercise, water_intake):
        user_id = self.generate_user_id()
        metrics = self.calculate_health_metrics(height, weight, age)

        user_data = {
            "user_id": user_id,
            "name": name,
            "gender": gender,
            "age": age,
            "height": height,
            "weight": weight,
            "calories": calories,
            "exercise": exercise,
            "water_intake": water_intake,
            "bmi": metrics["bmi"],
            "status": metrics["status"],
            "body_fat": metrics["body_fat"],
            "water_need": metrics["water_need"],
            "ideal_weight": metrics["ideal_weight"],
            "recommended_calories": metrics["recommended_calories"],
            "health_score": metrics["health_score"]
        }

        user = User.from_dict(user_data)

        self.users.append(user_data)
        self.save_users()
        return user, metrics["recommendation"]
