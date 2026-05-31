import io
import sys
from unittest.mock import patch
from src.ui.cli import BMI_CLI

def test_cli_flow():
    cli = BMI_CLI()
    
    # Test Case 1: Valid inputs (cm)
    with patch('builtins.input', side_effect=['175', '70']):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            cli.run()
            output = fake_out.getvalue()
            assert "--- BMI Calculator ---" in output
            assert "Your BMI: 22.86" in output
            assert "Category: Normal weight" in output
            print("✓ Valid input (cm) passed")

    # Test Case 2: Valid inputs (m)
    with patch('builtins.input', side_effect=['1.75', '70']):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            cli.run()
            output = fake_out.getvalue()
            assert "Your BMI: 22.86" in output
            print("✓ Valid input (m) passed")

    # Test Case 3: Invalid input then valid input
    # First input 'abc' (invalid), then '175', then '70'
    with patch('builtins.input', side_effect=['abc', '175', '70']):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            cli.run()
            output = fake_out.getvalue()
            assert "Invalid input. Please enter a numeric value." in output
            assert "Your BMI: 22.86" in output
            print("✓ Input validation passed")

    # Test Case 4: Format check (Wireframe comparison)
    with patch('builtins.input', side_effect=['175', '70']):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            cli.run()
            output = fake_out.getvalue()
            assert "--- Result ---" in output
            assert "-----------------" in output
            print("✓ Format verification passed")

if __name__ == "__main__":
    try:
        test_cli_flow()
        print("ALL PHASE 5 CLI TESTS PASSED")
    except Exception as e:
        print(f"TEST FAILED: {e}")
        exit(1)
