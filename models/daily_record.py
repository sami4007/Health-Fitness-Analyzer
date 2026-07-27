"""
Daily Record Model
Represents one meal record in the Health Fitness System.
"""


class DailyRecord:

    def __init__(
        self,
        user_id,
        date,
        meal,
        food_name,
        servings
    ):
        self.user_id = user_id
        self.date = date
        self.meal = meal
        self.food_name = food_name
        self.servings = servings

    def to_dict(self):
        """
        Convert DailyRecord object to dictionary.
        """

        return {
            "user_id": self.user_id,
            "date": self.date,
            "meal": self.meal,
            "food_name": self.food_name,
            "servings": self.servings
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a DailyRecord object from a dictionary.
        """

        return cls(
            user_id=data["user_id"],
            date=data["date"],
            meal=data["meal"],
            food_name=data["food_name"],
            servings=data["servings"]
        )