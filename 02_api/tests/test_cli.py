import pytest
import io
from unittest.mock import patch
from src.ui.cli import BMI_CLI

def test_cli_e2e_success():
    cli = BMI_CLI()
    with patch('builtins.input', side_effect=['175', '70']):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            cli.run()
            output = fake_out.getvalue()
            assert "Your BMI: 22.86" in output
            assert "Category: Normal weight" in output

def test_cli_e2e_invalid_input():
    cli = BMI_CLI()
    # Input 'abc' first, then valid values
    with patch('builtins.input', side_effect=['abc', '180', '80']):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            cli.run()
            output = fake_out.getvalue()
            assert "Invalid input. Please enter a numeric value." in output
            assert "Your BMI" in output # Should eventually succeed
