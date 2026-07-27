"""
Food Model
Represents one food item in the Health Fitness System.
"""


class Food:

    def __init__(
        self,
        food_name,
        calories,
        protein,
        carbs,
        fat
    ):
        self.food_name = food_name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

    def to_dict(self):
        """
        Convert Food object to dictionary.
        """

        return {
            "food_name": self.food_name,
            "calories": self.calories,
            "protein": self.protein,
            "carbs": self.carbs,
            "fat": self.fat
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a Food object from a dictionary.
        """

        return cls(
            food_name=data["food_name"],
            calories=data["calories"],
            protein=data["protein"],
            carbs=data["carbs"],
            fat=data["fat"]
        )