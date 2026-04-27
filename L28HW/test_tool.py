# test_tool.py
import pytest
from tool import analyze_crop_purchase

def test_happy_path():
    result = analyze_crop_purchase(0.25, 15.17, 1, 3, 4)
    assert result["purchase_quantity"] == 60
    assert result["purchase_quantity_unit"] == "seeds"
    assert result["expected_profit"] == 45.0
    assert result["expected_profit_unit"] == "$"
    assert result["total_harvests"] == 15
    assert result["total_harvests_unit"] == "crops"
    assert result["wait_time"] == 45
    assert result["wait_time_unit"] == "days"

def test_edge_case():
    result = analyze_crop_purchase(999999, 0, 0, 0, 999999)
    assert result["purchase_quantity"] == 0
    assert result["purchase_quantity_unit"] == "seeds"
    assert result["expected_profit"] == 0
    assert result["expected_profit_unit"] == "$"
    assert result["total_harvests"] == 0
    assert result["total_harvests_unit"] == "crops"
    assert result["wait_time"] == 0
    assert result["wait_time_unit"] == "days"

def test_invalid_input_raises():
    with pytest.raises(ValueError):
        analyze_crop_purchase(-1, 15.17, 1, 3, 4) # negative value should fail