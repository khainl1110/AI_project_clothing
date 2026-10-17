from llm import llm
from tools import clothing_search


llm_with_tools = llm.bind_tools([clothing_search])

response = llm_with_tools.invoke(
    "Find me 5 red Lacoste polos."
)

print(response)