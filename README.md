# isotope-pattern-service #

A REST API service, built with [FastAPI](https://fastapi.tiangolo.com/), that
exposes the [`isotope-pattern-lib`](https://pypi.org/project/isotope-pattern-lib/)
library over HTTP.

## Requirements ##

`python >= 3.9`

## Development ##

The project uses [`uv`](https://docs.astral.sh/uv/) as its package manager.

```
uv sync --group test
```

Run the test suite:

```
uv run pytest tests
```

Run the service locally:

```
uv run uvicorn isotope_pattern_service.main:app --reload
```

## API ##

### `POST /isotope-patterns/api/compute` ###

Computes the isotope pattern of a molecular formula by calling
`isotope_pattern_lib.api.compute_isotope_pattern`.

**Request body:**
```json
{
  "formula": "C2H5OH"
}
```

**Response body:**
```json
[
  {
    "name": "C2H5OH",
    "mass": 46.0419,
    "probability": 0.955,
    "isotopes": [
      { "name": "C12", "mass": 12.0, "abundance": 0.989, "count": 2 },
      { "name": "H1", "mass": 1.007825, "abundance": 1.0, "count": 6 },
      { "name": "O16", "mass": 15.994915, "abundance": 0.998, "count": 1 }
    ]
  }
]
```

An unknown element in the formula results in `400 Bad Request`. A missing
`formula` field results in `422 Unprocessable Entity`.
