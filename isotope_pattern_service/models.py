from typing import List

from pydantic import BaseModel, Field


class ComputeRequest(BaseModel):
    formula: str = Field(..., description="Molecular formula, e.g. 'C2H5OH'")


class Isotope(BaseModel):
    name: str
    mass: float
    abundance: float
    count: int


class IsotopeFormula(BaseModel):
    name: str
    mass: float
    probability: float
    isotopes: List[Isotope]
