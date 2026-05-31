from src.services.bmi_service import BMIService
from src.models.input_model import BMIInput

class BMI_CLI:
    def __init__(self):
        self.service = BMIService()

    def get_numeric_input(self, prompt: str) -> float:
        while True:
            try:
                value = input(prompt)
                return float(value)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def run(self):
        print("--- BMI Calculator ---")
        
        height = self.get_numeric_input("Please enter height: ")
        weight = self.get_numeric_input("Please enter weight (kg): ")
        
        input_data = BMIInput(height=height, weight=weight)
        try:
            result = self.service.get_bmi_analysis(input_data)
            
            print("\n--- Result ---")
            print(f"Your BMI: {result.bmi}")
            print(f"Category: {result.category}")
            print(f"Suggestion: {result.suggestion}")
            print("-----------------")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    cli = BMI_CLI()
    cli.run()
