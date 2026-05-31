import pytest
from src.services.bmi_service import BMIService
from src.models.input_model import BMIInput

@pytest.fixture
def service():
    return BMIService()

def test_height_detection(service):
    # Test cm detection
    assert service.normalize_height(170.0) == 1.70
    assert service.normalize_height(185.5) == 1.855
    # Test m detection
    assert service.normalize_height(1.70) == 1.70
    assert service.normalize_height(1.855) == 1.855
    # Boundary: exactly 3.0 should be treated as m
    assert service.normalize_height(3.0) == 3.0
    # Boundary: slightly above 3.0 should be treated as cm
    assert service.normalize_height(3.1) == 0.031

def test_bmi_calculation_precision(service):
    # 70kg / (1.75m)^2 = 22.857... -> 22.86
    assert service.calculate_bmi(1.75, 70) == 22.86
    # 50kg / (1.60m)^2 = 19.531... -> 19.53
    assert service.calculate_bmi(1.60, 50) == 19.53

def test_bmi_classification_boundaries(service):
    # Underweight < 18.5
    assert service.get_category_and_suggestion(18.4)[0] == "Underweight"
    # Normal 18.5 - 24.9
    assert service.get_category_and_suggestion(18.5)[0] == "Normal weight"
    assert service.get_category_and_suggestion(24.9)[0] == "Normal weight"
    # Overweight 25.0 - 29.9
    assert service.get_category_and_suggestion(25.0)[0] == "Overweight"
    assert service.get_category_and_suggestion(29.9)[0] == "Overweight"
    # Obese >= 30.0
    assert service.get_category_and_suggestion(30.0)[0] == "Obese"
    assert service.get_category_and_suggestion(35.0)[0] == "Obese"

def test_english_output(service):
    cat, sug = service.get_category_and_suggestion(22.0)
    # Check if output is in English (basic check)
    assert cat == "Normal weight"
    assert "Maintain current lifestyle" in sug
