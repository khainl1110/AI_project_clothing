import json
from databases import client 

def get_clothes(limit=None, sort_order=None, item_type=None, color=None, brand=None, price_ceiling=None, price_floor=None):
  """
  Retrieves clothing items specifically from the 'lacoste' collection.

  Args:
    limit: Optional integer, the maximum number of items to retrieve.
    sort_order: Optional string, 'cheapest' or 'expensive' to sort by price.
shirt', 'jacket', 'trouser', 'sneaker', 'backpack', 'belt', or 'shoe' to filter by item type(s).
    item_type: Optional string or list of strings, 'polo', '
    color: Optional string or list of strings, to filter items by color (e.g., 'dark', 'beige', or ['red', 'blue']).
    brand: Optional string, to filter items by brand (e.g., 'Lacoste', 'Ralph Lauren').

  Returns:
    A JSON string of a list of dictionaries, whre each dictionary represents a clothing item.
  """
  # Using the database name specified by the user
  lacoste_db = client['web_scrap']
  collection = lacoste_db['clothes']


  query = {}
  price_query = {}
  if brand is not None:
    query['brand'] = brand
  if item_type is not None:
    if isinstance(item_type, str):
        item_type = [item_type]
    query["type"] = {"$in": item_type}
  if color is not None:
    # Convert single string to list
    if isinstance(color, str):
        color = [color]
    color_conditions = [
        {"colors": {"$regex": c, "$options": "i"}}
        for c in color # Filter out None values
    ]
    query["$or"] = color_conditions
  if price_ceiling is not None:
    price_query['$lt'] = price_ceiling
  if price_floor is not None:
    price_query['$gt'] = price_floor

  if price_query:
    query['price'] = price_query
  print("MongoDB query", query)
  retrieved_data = collection.find(query, {'_id': 0})
  if limit is not None:
    retrieved_data = retrieved_data.limit(limit)

  if sort_order is not None:
    if sort_order == 'expensive':
        retrieved_data = retrieved_data.sort("price", -1)
    elif sort_order == 'cheapest':
        retrieved_data = retrieved_data.sort("price", 1)
  data_list = list(retrieved_data)  # consume cursor ONCE
  return json.dumps(data_list)