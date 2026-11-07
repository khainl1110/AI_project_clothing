from agentscope.tool import FunctionTool, Toolkit
from services.clothing_service import get_clothes


def get_clothes_tool(
    brand: str = "",
    item_type: str = "",
    color: str = "",
    price_floor: float = 0,
    price_ceiling: float = None,
    sort_order: str = None,
    limit: int = 5,
) -> str:
    """Search clothing products by brand, type, and color.

    Args:
            brand: Brand to search for, such as Lacoste.
            item_type: Clothing type, such as polo or t-shirt.
            color: Desired color, such as red or navy.
            price_floor: Minimum price.
            price_ceiling: Maximum price.
            sort_order: 'cheapest' or 'expensive'.
            limit: The number of products to return.
    """

    if not 1 <= limit <= 20:
        return "Limit must be between 1 and 20."

    products = get_clothes(
        brand=brand or None,
        item_type=item_type or None,
        color=color or None,
        price_floor=price_floor or None,
        price_ceiling=price_ceiling or None,
        sort_order=sort_order or None,
        limit=limit,
    )

    return str(products)


def build_clothing_toolkit():
    return Toolkit(
        tools=[
            FunctionTool(
                get_clothes_tool,
                is_read_only=True,
            )
        ]
    )