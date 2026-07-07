from typing import List

from fastapi import APIRouter, HTTPException
from isotope_pattern_lib import api as isotope_pattern_api

from isotope_pattern_service.models import ComputeRequest, Isotope, IsotopeFormula

router = APIRouter(prefix="/isotope-patterns/api")


@router.post("/compute", response_model=List[IsotopeFormula])
def compute(request: ComputeRequest) -> List[IsotopeFormula]:

    try:
        pattern = isotope_pattern_api.compute_isotope_pattern(formula_string=request.formula)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    return [
        IsotopeFormula(
            name=pattern.name,
            mass=pattern.mass,
            probability=pattern.probability,
            isotopes=[
                Isotope(name=isotope.name, mass=isotope.mass, abundance=isotope.abundance, count=count)
                for isotope, count in pattern.isotopes.items()
            ],
        )
        for pattern in pattern
    ]
