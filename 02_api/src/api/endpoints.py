from fastapi import APIRouter, HTTPException
from src.models.input_model import BMIInput
from src.models.output_model import BMIOutput
from src.services.bmi_service import BMIService

router = APIRouter()
bmi_service = BMIService()

@router.post("/calculate", response_model=BMIOutput)
async def calculate_bmi(input_data: BMIInput):
    """
    Calculate BMI based on height and weight.
    Auto-detects height units (cm vs m).
    """
    try:
        return bmi_service.get_bmi_analysis(input_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
