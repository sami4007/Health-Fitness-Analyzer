"""
Daily Summary Model
Represents one daily summary in the Health Fitness System.
"""


class DailySummary:

    def __init__(
        self,
        user_id,
        date,
        water,
        calories_burned
    ):
        self.user_id = user_id
        self.date = date
        self.water = water
        self.calories_burned = calories_burned

    def to_dict(self):
        """
        Convert DailySummary object to dictionary.
        """

        return {
            "user_id": self.user_id,
            "date": self.date,
            "water": self.water,
            "calories_burned": self.calories_burned
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a DailySummary object from a dictionary.
        """

        return cls(
            user_id=data["user_id"],
            date=data["date"],
            water=data["water"],
            calories_burned=data["calories_burned"]
        )