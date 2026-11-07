import json
from typing import Optional

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI

from services.clothing_service import get_clothes
from prompts.clothing_assistant import CLOTHING_ASSISTANT_PROMPT


@tool
def search_clothes(
    brand: Optional[str] = None,
    item_type: Optional[str] = None,
    color: Optional[str] = None,
    price_floor: Optional[float] = None,
    price_ceiling: Optional[float] = None,
    sort_order: Optional[str] = None,
    limit: int = 5,
) -> str:
    """Search the clothing database.

    Args:
        brand: Brand to search for, such as Lacoste.
        item_type: Clothing type, such as polo or t-shirt.
        color: Desired color, such as red or navy.
        price_floor: Minimum allowed product price (exclusive).
             Set this when the user specifies a minimum price.
        price_ceiling: Maximum allowed product price (exclusive).
               Set this when the user specifies a maximum price.
        sort_order: 'cheapest' or 'expensive'.
        limit: The number of products to return.
    """
    if limit < 1 or limit > 20:
        return "Error: limit must be between 1 and 20."

    if price_floor is not None and price_floor < 0:
        return "Error: price_floor cannot be negative."

    if price_ceiling is not None and price_ceiling < 0:
        return "Error: price_ceiling cannot be negative."

    if (
        price_floor is not None
        and price_ceiling is not None
        and price_floor > price_ceiling
    ):
        return "Error: price_floor cannot exceed price_ceiling."

    if sort_order not in (None, "cheapest", "expensive"):
        return "Error: sort_order must be 'cheapest' or 'expensive'."

    # Call your existing MongoDB backend.
    products = get_clothes(
        brand=brand,
        item_type=item_type,
        color=color,
        price_floor=price_floor,
        price_ceiling=price_ceiling,
        sort_order=sort_order,
        limit=limit,
    )

    # Keep the model response small and JSON-serializable.
    return json.dumps(products, default=str)


def build_clothing_agent():
    model = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0,
    )

    return create_agent(
        model=model,
        tools=[search_clothes],
        system_prompt=CLOTHING_ASSISTANT_PROMPT,
    )


clothing_agent = build_clothing_agent()


def ask_clothing_agent(question: str) -> str:
    result = clothing_agent.invoke(
        {
            "messages": [
                {"role": "user", "content": question}
            ]
        }
    )

    return result["messages"][-1].content