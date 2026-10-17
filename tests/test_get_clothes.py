from helper_functions import get_clothes
import json

def test_get_clothes():
    result = get_clothes(brand="Lacoste")

    assert result is not None
    assert len(result) > 0
    print("Return type:", type(result))
    assert all(item["brand"].lower() == "lacoste" for item in result)

    print("\n=== Test 2: Brand + Type ===")
    result = get_clothes(brand="Lacoste", item_type="polo")

    assert result is not None
    assert len(result) > 0
    assert all(item["brand"].lower() == "lacoste" for item in result)
    assert all(item["type"].lower() == "polo" for item in result)

    print("\n=== Test 3: Brand + Type + Color ===")
    print(get_clothes(
        brand="Lacoste",
        item_type="polo",
        color="red"
    ))

    print("\n=== Test 4: Multiple colors ===")
    print(get_clothes(
        brand="Lacoste",
        color=["red", "blue"]
    ))

    print("\n=== Test 5: Price ===")
    print(get_clothes(
        brand="Lacoste",
        price_floor=50,
        price_ceiling=150
    ))

    print("\n=== Test 6: Cheapest ===")
    print(get_clothes(
        brand="Lacoste",
        sort_order="cheapest",
        limit=5
    ))

    print("\n=== Test 7: Most expensive ===")
    print(get_clothes(
        brand="Lacoste",
        sort_order="expensive",
        limit=5
    ))