from pydantic import BaseModel, Field

class BMIOutput(BaseModel):
    bmi: float = Field(..., description="Calculated BMI value")
    category: str = Field(..., description="BMI category (English)")
    suggestion: str = Field(..., description="Health suggestion (English)")
