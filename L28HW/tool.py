# Tool Name : Crop Purchase Analyzer
# Domain : Agriculture <- From examples
# Author : Jordan A. Baumann

# Description: Computes information that is
# useful for deciding which of several types of
# crops to purchase. Precision is necessary
# because of the financial and often high risk
# of the types of large purchases common in agriculture
# Usage : See README.md for a sample call.
# -------------------------------------------------------

from math import ceil

def analyze_crop_purchase(
        cost: float,
        budget: float,
        sell_price: float,
        growth_time: int,
        growth_capacity: int) -> dict:
    """
    Calculates important financial information about a crop
    Args:
    cost (float): price of crop per instance of crop,
    sell_price (float): average price earned back from a crop,
    budget (float): max amount willing to be spent on these crops,
    growth_time (int): expected amount of days for each crop to grow,
    growth_capacity (int): amount of crop able to be planted at the same time

    Returns:
    dict: {
    "purchase_quantity": amount of crop to purchase (int),
    "purchase_quantity_unit": unit of purchase_quantity (string),
    "expected_profit": average net gain from these crops after selling (float),
    "expected_profit_unit": unit of expected_profit (string),
    "total_harvests": amount of harvests if planted as expected (int),
    "total_harvests_unit": unit of total_harvests (string),
    "wait_time: expected time to these grow crops (int)
    "wait_time_unit": unit of wait_time (string),
    }
    Raises:
    TypeError: if any input is of an unexpected type
    ValueError: if any input is of an unexpected type or value
    """
    
    # --- Input Validation ---
    try:
        cost = float(cost)
        budget = float(budget)
        sell_price = float(sell_price)
        growth_time = int(growth_time)
        growth_capacity = int(growth_capacity)

    except Exception as e:
        print("Cannot convert input values to valid types")
        raise e
    
    if cost <= 0 or budget < 0 or sell_price < 0 or\
        growth_time < 0 or growth_capacity <= 0:
        print("Invalid value/s")
        raise ValueError

    # --- Core Logic ---
    purchase_quantity: int = int(budget // cost)
    expected_profit: float = purchase_quantity * (sell_price - cost)
    total_harvests: int = int(ceil(purchase_quantity / growth_capacity))
    wait_time: int = total_harvests * growth_time

    return {"purchase_quantity": purchase_quantity,
        "purchase_quantity_unit": "seeds",
        "expected_profit": expected_profit,
        "expected_profit_unit": "$",
        "total_harvests": total_harvests,
        "total_harvests_unit": "crops",
        "wait_time": wait_time,
        "wait_time_unit": "days"}

print(analyze_crop_purchase(0.25, 15.17, 1.0, 3, 4))