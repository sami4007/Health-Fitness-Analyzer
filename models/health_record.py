class HealthRecord:
    def __init__(self, user_id, name, gender, age, height, weight, calories, exercise, water_intake, 
                 bmi, status, body_fat, water_need, ideal_weight, recommended_calories, health_score):
        self.user_id = user_id
        self.name = name
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.calories = calories
        self.exercise = exercise
        self.water_intake = water_intake
        self.bmi = bmi
        self.status = status
        self.body_fat = body_fat
        self.water_need = water_need
        self.ideal_weight = ideal_weight
        self.recommended_calories = recommended_calories
        self.health_score = health_score

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "gender": self.gender,
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            "calories": self.calories,
            "exercise": self.exercise,
            "water_intake": self.water_intake,
            "bmi": self.bmi,
            "status": self.status,
            "body_fat": self.body_fat,
            "water_need": self.water_need,
            "ideal_weight": self.ideal_weight,
            "recommended_calories": self.recommended_calories,
            "health_score": self.health_score
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            user_id=data.get("user_id", ""),
            name=data.get("name", ""),
            gender=data.get("gender", ""),
            age=data.get("age", 0),
            height=data.get("height", 0.0),
            weight=data.get("weight", 0.0),
            calories=data.get("calories", 0),
            exercise=data.get("exercise", 0.0),
            water_intake=data.get("water_intake", 0.0),
            bmi=data.get("bmi", 0.0),
            status=data.get("status", "Unknown"),
            body_fat=data.get("body_fat", 0.0),
            water_need=data.get("water_need", 0.0),
            ideal_weight=data.get("ideal_weight", 0.0),
            recommended_calories=data.get("recommended_calories", 0),
            health_score=data.get("health_score", 0)
        )