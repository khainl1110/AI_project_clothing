from langchain_core.tools import tool

from helper_functions import get_clothes


@tool
def clothing_search(
    limit: int | None = None,
    sort_order: str | None = None,
    item_type: str | list[str] | None = None,
    color: str | list[str] | None = None,
    brand: str | None = None,
    price_ceiling: float | None = None,
    price_floor: float | None = None,
) -> str:
    """
    Search the clothing database.

    Use this tool when the user wants to find clothing items.

    Args:
        limit: Maximum number of clothing items to return.
        sort_order: Use "cheapest" for lowest price first or
            "expensive" for highest price first.
        item_type: Clothing type such as "polo", "shirt",
            "jacket", "trouser", "sneaker", "backpack",
            "belt", or "shoe". Can be a list.
        color: Color such as "red", "blue", or "black".
            Can be a list of colors.
        brand: Brand such as "Lacoste" or "Ralph Lauren".
        price_ceiling: Maximum price.
        price_floor: Minimum price.
    """
    return get_clothes(
        limit=limit,
        sort_order=sort_order,
        item_type=item_type,
        color=color,
        brand=brand,
        price_ceiling=price_ceiling,
        price_floor=price_floor,
    )