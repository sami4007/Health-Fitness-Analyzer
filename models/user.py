"""
User Model
Represents one user in the Health Fitness System.
"""


class User:

    def __init__(
        self,
        user_id,
        name,
        age,
        gender,
        height,
        weight,
        activity_level,
        goal,
        bmi,
        bmi_category
    ):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.activity_level = activity_level
        self.goal = goal
        self.bmi = bmi
        self.bmi_category = bmi_category

    def to_dict(self):
        """
        Convert User object to dictionary.
        """

        return {
            "user_id": self.user_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "activity_level": self.activity_level,
            "goal": self.goal,
            "bmi": self.bmi,
            "bmi_category": self.bmi_category
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a User object from a dictionary.
        """

        return cls(
            user_id=data["user_id"],
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            height=data["height"],
            weight=data["weight"],
            activity_level=data["activity_level"],
            goal=data["goal"],
            bmi=data["bmi"],
            bmi_category=data.get("bmi_category", "Unknown")
        )