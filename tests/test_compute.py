from fastapi.testclient import TestClient

from isotope_pattern_service.main import app

client = TestClient(app)


def test__should_return_isotope_patterns__when_formula_is_valid():

    response = client.post("/isotope-patterns/api/compute", json={"formula": "C2H5OH"})

    assert response.status_code == 200

    patterns = response.json()
    assert len(patterns) > 0
    for pattern in patterns:
        assert "name" in pattern
        assert "mass" in pattern
        assert "probability" in pattern
        assert "isotopes" in pattern
        for isotope in pattern["isotopes"]:
            assert {"name", "mass", "abundance", "count"} <= isotope.keys()


def test__should_return_bad_request__when_formula_contains_unknown_element():

    response = client.post("/isotope-patterns/api/compute", json={"formula": "Xx2"})

    assert response.status_code == 400
    assert "Xx" in response.json()["detail"]


def test__should_return_unprocessable_entity__when_formula_field_is_missing():

    response = client.post("/isotope-patterns/api/compute", json={})

    assert response.status_code == 422
