from agentscope.tool import FunctionTool, Toolkit
from services.clothing_service import get_clothes as search_clothing


def search_clothes(
    brand: str = "",
    item_type: str = "",
    color: str = "",
    limit: int = 5,
) -> str:
    """Search clothing products by brand, type, and color.

    Args:
        brand: Clothing brand, e.g. Lacoste.
        item_type: Clothing type, e.g. polo.
        color: Desired color.
        limit: Maximum number of products.
    """

    if not 1 <= limit <= 20:
        return "Limit must be between 1 and 20."

    products = search_clothing(
        brand=brand or None,
        item_type=item_type or None,
        color=color or None,
        limit=limit,
    )

    return str(products)


def build_clothing_toolkit():
    return Toolkit(
        tools=[
            FunctionTool(
                search_clothes,
                is_read_only=True,
            )
        ]
    )