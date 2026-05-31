from src.models.input_model import BMIInput
from src.models.output_model import BMIOutput

class BMIService:
    @staticmethod
    def normalize_height(height: float) -> float:
        """
        Automatically detect if height is in cm or m and convert to m.
        Logic: If height > 3.0, assume cm.
        """
        if height > 3.0:
            return height / 100.0
        return height

    @staticmethod
    def calculate_bmi(height: float, weight: float) -> float:
        """
        Calculate BMI using formula: weight / (height^2)
        """
        normalized_height = BMIService.normalize_height(height)
        if normalized_height <= 0:
            raise ValueError("Height must be greater than zero.")
        
        bmi = weight / (normalized_height ** 2)
        return round(bmi, 2)

    @staticmethod
    def get_category_and_suggestion(bmi: float) -> tuple[str, str]:
        """
        Determine BMI category and provide corresponding suggestion.
        """
        if bmi < 18.5:
            return "Underweight", "Increase caloric intake and consult a nutritionist."
        elif 18.5 <= bmi < 25.0:
            return "Normal weight", "Maintain current lifestyle and healthy diet."
        elif 25.0 <= bmi < 30.0:
            return "Overweight", "Consider increased physical activity and diet control."
        else:
            return "Obese", "Seek professional medical advice for weight management."

    def get_bmi_analysis(self, input_data: BMIInput) -> BMIOutput:
        """
        Main interface to perform complete BMI analysis.
        """
        bmi = self.calculate_bmi(input_data.height, input_data.weight)
        category, suggestion = self.get_category_and_suggestion(bmi)
        
        return BMIOutput(
            bmi=bmi,
            category=category,
            suggestion=suggestion
        )
