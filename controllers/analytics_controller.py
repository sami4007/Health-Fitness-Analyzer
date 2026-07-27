"""
Analytics Controller
"""

import csv

from utils import calculate_bmi, get_bmi_category


class AnalyticsController:

    def __init__(self):

        self.dataset_path = "data/enhanced_health_data.csv"

        self.data = []


    def load_dataset(self):

        self.data.clear()

        with open(self.dataset_path, "r", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            self.data = list(reader)

        rows = len(self.data)

        columns = len(self.data[0]) if rows > 0 else 0

        return rows, columns


    def analyze_dataset(self):

        if not self.data:
            self.load_dataset()

        total_bmi = 0

        healthy = 0
        overweight = 0
        obese = 0

        for row in self.data:

            height = float(row["Height (cm)"])
            weight = float(row["Weight (kg)"])

            bmi = calculate_bmi(height, weight)

            total_bmi += bmi

            category = get_bmi_category(bmi)

            if category in ("Underweight", "Normal"):
                healthy += 1

            elif category == "Overweight":
                overweight += 1

            elif category == "Obese":
                obese += 1

        average_bmi = round(total_bmi / len(self.data), 2)

        return {
            "average_bmi": average_bmi,
            "healthy": healthy,
            "overweight": overweight,
            "obese": obese
        }