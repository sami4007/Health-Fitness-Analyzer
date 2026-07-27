"""
Calorie Controller
Handles all business logic related to Dashboard 2.
"""

import json
import os
import numpy as np
from datetime import datetime, timedelta

from config import (
    USERS_FILE,
    FOOD_DATABASE_FILE,
    DAILY_RECORD_FILE,
    DAILY_SUMMARY_FILE
)

from models.user import User
from models.food import Food
from models.daily_record import DailyRecord
from models.daily_summary import DailySummary


class CalorieController:

    def __init__(self):

     self.users = self.load_users()

     self.food_database = self.load_food_database()

     self.daily_records = self.load_daily_records()

     self.daily_summary = self.load_daily_summary()
    # -------------------------------------------------

    def load_users(self):

        if not os.path.exists(USERS_FILE):
            return []

        try:

            with open(USERS_FILE, "r") as file:

                users = json.load(file)

                return [
                    User.from_dict(user)
                    for user in users
                ]

        except json.JSONDecodeError:

            return []

    # -------------------------------------------------

    def load_food_database(self):

        if not os.path.exists(FOOD_DATABASE_FILE):
            return []

        try:

            with open(FOOD_DATABASE_FILE, "r") as file:

                foods = json.load(file)

                return [
                    Food.from_dict(food)
                    for food in foods
                ]

        except json.JSONDecodeError:

            return []

    # -------------------------------------------------

    def load_daily_records(self):

        if not os.path.exists(DAILY_RECORD_FILE):
            return []

        try:

            with open(DAILY_RECORD_FILE, "r") as file:

                records = json.load(file)

                return [
                    DailyRecord.from_dict(record)
                    for record in records
                ]

        except json.JSONDecodeError:

            return []

    # -------------------------------------------------

    def load_daily_summary(self):

        if not os.path.exists(DAILY_SUMMARY_FILE):
            return []

        try:

            with open(DAILY_SUMMARY_FILE, "r") as file:

                summaries = json.load(file)

                return [
                    DailySummary.from_dict(summary)
                    for summary in summaries
                ]

        except json.JSONDecodeError:

            return []

    # -------------------------------------------------

    def save_daily_records(self):

        with open(DAILY_RECORD_FILE, "w") as file:

            json.dump(

                [
                    record.to_dict()
                    for record in self.daily_records
                ],

                file,

                indent=4

            )

    # -------------------------------------------------

    def save_daily_summary(self):

        with open(DAILY_SUMMARY_FILE, "w") as file:

            json.dump(

                [
                    summary.to_dict()
                    for summary in self.daily_summary
                ],

                file,

                indent=4

            )

    # -------------------------------------------------

    def get_all_foods(self):

        return self.food_database

    # -------------------------------------------------

    def search_food(self, keyword):

        keyword = keyword.lower()

        return [

            food

            for food in self.food_database

            if keyword in food.food_name.lower()

        ]

    # -------------------------------------------------

    def add_meal(

        self,

        user_id,

        date,

        meal,

        food_name,

        servings

    ):

        food = None

        for item in self.food_database:

            if item.food_name == food_name:

                food = item

                break

        if food is None:

            return None

        record = DailyRecord(

            user_id=user_id,

            date=date,

            meal=meal,

            food_name=food_name,

            servings=servings

        )

        self.daily_records.append(record)

        self.save_daily_records()

        return record

    # -------------------------------------------------

    def find_user(self, user_id):

        for user in self.users:

            if user.user_id == user_id:

                return user

        return None
        # -------------------------------------------------

    def calculate_bmr(self, user):

        gender = user.gender.lower()

        weight = float(user.weight)
        height = float(user.height)
        age = int(user.age)

        if gender == "male":

            return (
                (10 * weight)
                + (6.25 * height)
                - (5 * age)
                + 5
            )

        return (
            (10 * weight)
            + (6.25 * height)
            - (5 * age)
            - 161
        )

    # -------------------------------------------------

    def get_activity_multiplier(self, activity_level):

        activity = activity_level.lower()

        mapping = {

            "sedentary": 1.20,
            "light": 1.375,
            "moderate": 1.55,
            "active": 1.725,
            "very active": 1.90

        }

        return mapping.get(activity, 1.20)

    # -------------------------------------------------

    def calculate_daily_target(self, user):

        bmr = self.calculate_bmr(user)

        activity = self.get_activity_multiplier(
            user.activity_level
        )

        target = bmr * activity

        goal = user.goal.lower()

        if goal == "lose weight":

            target -= 500

        elif goal == "gain weight":

            target += 500

        return round(target)

    # -------------------------------------------------

    def get_food(self, food_name):

        for food in self.food_database:

            if food.food_name.lower() == food_name.lower():

                return food

        return None

    # -------------------------------------------------

    def get_daily_records(self, user_id, date):

        return [

            record

            for record in self.daily_records

            if record.user_id == user_id
            and record.date == date

        ]

    # -------------------------------------------------

    def calculate_daily_calories(self, user_id, date):

        total = 0

        records = self.get_daily_records(
            user_id,
            date
        )

        for record in records:

            food = self.get_food(
                record.food_name
            )

            if food:

                total += (
                    food.calories
                    * record.servings
                )

        return round(total, 2)

    # -------------------------------------------------

    def calculate_total_protein(self, user_id, date):

        total = 0

        records = self.get_daily_records(
            user_id,
            date
        )

        for record in records:

            food = self.get_food(
                record.food_name
            )

            if food:

                total += (
                    food.protein
                    * record.servings
                )

        return round(total, 2)

    # -------------------------------------------------

    def calculate_total_carbs(self, user_id, date):

        total = 0

        records = self.get_daily_records(
            user_id,
            date
        )

        for record in records:

            food = self.get_food(
                record.food_name
            )

            if food:

                total += (
                    food.carbs
                    * record.servings
                )

        return round(total, 2)

    # -------------------------------------------------

    def calculate_total_fat(self, user_id, date):

        total = 0

        records = self.get_daily_records(
            user_id,
            date
        )

        for record in records:

            food = self.get_food(
                record.food_name
            )

            if food:

                total += (
                    food.fat
                    * record.servings
                )

        return round(total, 2)

    # -------------------------------------------------

    def get_daily_summary(self, user_id, date):

        for summary in self.daily_summary:

            if (

                summary.user_id == user_id
                and summary.date == date

            ):

                return summary

        return None

    # -------------------------------------------------

    def get_calories_burned(self, user_id, date):

        summary = self.get_daily_summary(
            user_id,
            date
        )

        if summary:

            return summary.calories_burned

        return 0

    # -------------------------------------------------

    def get_water_intake(self, user_id, date):

        summary = self.get_daily_summary(
            user_id,
            date
        )

        if summary:

            return summary.water

        return 0

    # -------------------------------------------------

    def calculate_remaining_calories(
        self,
        user_id,
        date
    ):

        user = self.find_user(user_id)

        if user is None:

            return 0

        target = self.calculate_daily_target(
            user
        )

        consumed = self.calculate_daily_calories(
            user_id,
            date
        )

        burned = self.get_calories_burned(
            user_id,
            date
        )

        return round(
            target - consumed + burned,
            2
        )
        # -------------------------------------------------

    def update_water_intake(
        self,
        user_id,
        date,
        water
    ):

        summary = self.get_daily_summary(
            user_id,
            date
        )

        if summary:

            summary.water = water

        else:

            summary = DailySummary(

                user_id=user_id,

                date=date,

                water=water,

                calories_burned=0

            )

            self.daily_summary.append(summary)

        self.save_daily_summary()

    # -------------------------------------------------

    def update_calories_burned(
        self,
        user_id,
        date,
        calories
    ):

        summary = self.get_daily_summary(
            user_id,
            date
        )

        if summary:

            summary.calories_burned = calories

        else:

            summary = DailySummary(

                user_id=user_id,

                date=date,

                water=0,

                calories_burned=calories

            )

            self.daily_summary.append(summary)

        self.save_daily_summary()

    # -------------------------------------------------

    def daily_summary_report(
        self,
        user_id,
        date
    ):

        user = self.find_user(user_id)

        if user is None:

            return None

        return {

            "target_calories":
                self.calculate_daily_target(user),

            "consumed_calories":
                self.calculate_daily_calories(
                    user_id,
                    date
                ),

            "remaining_calories":
                self.calculate_remaining_calories(
                    user_id,
                    date
                ),

            "protein":
                self.calculate_total_protein(
                    user_id,
                    date
                ),

            "carbs":
                self.calculate_total_carbs(
                    user_id,
                    date
                ),

            "fat":
                self.calculate_total_fat(
                    user_id,
                    date
                ),

            "water":
                self.get_water_intake(
                    user_id,
                    date
                ),

            "calories_burned":
                self.get_calories_burned(
                    user_id,
                    date
                )

        }

    # -------------------------------------------------

    def weekly_summary_report(
     self,
     user_id,
     selected_date
 ):

     end_date = datetime.strptime(
        selected_date,
        "%Y-%m-%d"
     )

     weekly_calories = []

     for i in range(6, -1, -1):

        current_date = (
            end_date
            - timedelta(days=i)
        ).strftime("%Y-%m-%d")

        calories = self.calculate_daily_calories(
            user_id,
            current_date
        )

        weekly_calories.append(calories)

     valid_calories = [

       calorie

     for calorie in weekly_calories

     if calorie > 0

      ]

     if len(valid_calories) == 0:

      return {

        "daily_calories": [],

        "average": 0,

        "maximum": 0,

        "minimum": 0,

        "median": 0,

        "standard_deviation": 0,

        "has_data": False

      }

      calories = np.array(

      valid_calories,

       dtype=float

     )

     return {

        "daily_calories": weekly_calories,

        "average":
            round(
                np.mean(calories),
                2
            ),

        "maximum":
            round(
                np.max(calories),
                2
            ),

        "minimum":
            round(
                np.min(calories),
                2
            ),

        "median":
            round(
                np.median(calories),
                2
            ),

        "standard_deviation":
            round(
                np.std(calories),
                2
            ),

        "has_data": True


    }

    # -------------------------------------------------

    def remove_meal(
        self,
        user_id,
        date,
        meal,
        food_name
    ):

        for record in self.daily_records:

            if (

                record.user_id == user_id
                and record.date == date
                and record.meal == meal
                and record.food_name == food_name

            ):

                self.daily_records.remove(
                    record
                )

                self.save_daily_records()

                return True

        return False

    # -------------------------------------------------

    def clear_day(
        self,
        user_id,
        date
    ):

        self.daily_records = [

            record

            for record in self.daily_records

            if not (

                record.user_id == user_id
                and record.date == date

            )

        ]

        self.daily_summary = [

            summary

            for summary in self.daily_summary

            if not (

                summary.user_id == user_id
                and summary.date == date

            )

        ]

        self.save_daily_records()

        self.save_daily_summary()

    # -------------------------------------------------

    def get_meals_by_type(
        self,
        user_id,
        date,
        meal
    ):

        return [

            record

            for record in self.daily_records

            if (

                record.user_id == user_id
                and record.date == date
                and record.meal.lower() == meal.lower()

            )

        ]

    # -------------------------------------------------

    def get_all_meals(
        self,
        user_id,
        date
    ):

        return self.get_daily_records(
            user_id,
            date
        )