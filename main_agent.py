from langchain.agents import create_agent

from llm import llm
from tools import clothing_search


agent = create_agent(
    model=llm,
    tools=[clothing_search],
)


result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Find me 5 red Lacoste polos."
        }
    ]
})


print(result["messages"][-1].content)