import risk_register
import pytest

def test_risk_init():
    risk = risk_register.Risk(name="Test Risk")
    assert risk.name == "Test Risk"
    assert risk.status == "Open"
    assert risk.severity == "Low"
    assert risk.probability == "Low"
    assert risk.object_id == "RSK001"

def test_invalid_risk_severity():
    with pytest.raises(ValueError):
        risk2 = risk_register.Risk(name="Test Risk", severity="Maximum")

def test_risk_str():
    risk3 = risk_register.Risk(name="Test Risk")
    assert str(risk3) == "RSK003: Test Risk (Open)"

def name_input_helper():
    assert risk_register.name_input_helper("Test name") == "Test name"


