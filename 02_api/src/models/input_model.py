from pydantic import BaseModel, Field

class BMIInput(BaseModel):
    height: float = Field(..., description="Height in cm or m (auto-detected)")
    weight: float = Field(..., description="Weight in kg")
