"""
User Controller
Handles all business logic related to users.
"""

from models.user import User

from utils import (
    load_users,
    save_users,
    calculate_bmi,
    get_bmi_category,
    generate_user_id
)


class UserController:

    def __init__(self):
        self.users = load_users()

    def get_all_users(self):
        """
        Return all users.
        """
        return self.users

    def add_user(
        self,
        name,
        age,
        gender,
        height,
        weight,
        activity_level,
        goal
    ):

        user_id = generate_user_id(self.users)

        bmi = calculate_bmi(height, weight)
        category = get_bmi_category(bmi)

        user = User(
            user_id=user_id,
            name=name,
            age=age,
            gender=gender,
            height=height,
            weight=weight,
            activity_level=activity_level,
            goal=goal,
            bmi=bmi,
            bmi_category=category
        )

        self.users.append(user.to_dict())

        save_users(self.users)
        self.users = load_users()

        return user

    def find_user(self, user_id):

        for user in self.users:

            if user["user_id"] == user_id:

                return User.from_dict(user)

        return None
    
    def update_user(
        self,
        user_id,
        name,
        age,
        gender,
        height,
        weight,
        activity_level,
        goal
    ):

        for user in self.users:

            if user["user_id"] == user_id:

                bmi = calculate_bmi(height, weight)
                category = get_bmi_category(bmi)

                user["name"] = name
                user["age"] = age
                user["gender"] = gender
                user["height"] = height
                user["weight"] = weight
                user["activity_level"] = activity_level
                user["goal"] = goal
                user["bmi"] = bmi
                user["bmi_category"] = category

                save_users(self.users)

                return True

        return False

    def analyze_users(self):
        total_bmi = 0

        healthy = 0
        overweight = 0
        obese = 0

        total_users = len(self.users)

        if total_users == 0:
            return {
                "average_bmi": 0,
                "healthy": 0,
                "overweight": 0,
                "obese": 0
            }

        for user in self.users:
            bmi = float(user["bmi"])
            total_bmi += bmi

            category = user.get("bmi_category")

            if category is None:
                category = get_bmi_category(bmi)

            if category in ["Normal", "Healthy"]:
                healthy += 1
            elif category == "Overweight":
                overweight += 1
            elif category == "Obese":
                obese += 1

        return {
            "average_bmi": round(total_bmi / total_users, 2),
            "healthy": healthy,
            "overweight": overweight,
            "obese": obese
        }
    
    
    
    def delete_user(self, user_id):

        for user in self.users:

            if user["user_id"] == user_id:

                self.users.remove(user)

                save_users(self.users)

                return True

        return False