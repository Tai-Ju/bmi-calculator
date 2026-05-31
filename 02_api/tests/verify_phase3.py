from src.services.bmi_service import BMIService
from src.models.input_model import BMIInput

def test_bmi_service():
    service = BMIService()
    
    # Test height normalization
    assert service.normalize_height(175) == 1.75, "Should convert cm to m"
    assert service.normalize_height(1.75) == 1.75, "Should keep m as m"
    print("✓ Height normalization passed")

    # Test BMI calculation
    # 70 / (1.75^2) = 70 / 3.0625 = 22.857... -> 22.86
    assert service.calculate_bmi(175, 70) == 22.86, "BMI calculation (cm) failed"
    assert service.calculate_bmi(1.75, 70) == 22.86, "BMI calculation (m) failed"
    print("✓ BMI calculation passed")

    # Test Category and Suggestion
    # Underweight < 18.5
    cat, sug = service.get_category_and_suggestion(18.0)
    assert cat == "Underweight" and "Increase caloric intake" in sug
    # Normal 18.5 - 24.9
    cat, sug = service.get_category_and_suggestion(22.0)
    assert cat == "Normal weight" and "Maintain current lifestyle" in sug
    # Overweight 25.0 - 29.9
    cat, sug = service.get_category_and_suggestion(27.0)
    assert cat == "Overweight" and "Consider increased physical activity" in sug
    # Obese >= 30.0
    cat, sug = service.get_category_and_suggestion(32.0)
    assert cat == "Obese" and "Seek professional medical advice" in sug
    print("✓ BMI category and suggestions passed")

    # Test full analysis interface
    input_data = BMIInput(height=175, weight=70)
    output = service.get_bmi_analysis(input_data)
    assert output.bmi == 22.86
    assert output.category == "Normal weight"
    print("✓ Full analysis interface passed")

if __name__ == "__main__":
    try:
        test_bmi_service()
        print("ALL PHASE 3 TESTS PASSED")
    except AssertionError as e:
        print(f"TEST FAILED: {e}")
        exit(1)
