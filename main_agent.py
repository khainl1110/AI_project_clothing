from langchain.agents import create_agent

import langsmith as ls 

from llm import llm
from tools import clothing_search
from dotenv import load_dotenv
load_dotenv(override=True)
agent = create_agent(
    model=llm,
    tools=[clothing_search],
)

DEBUG_AGENT = True
with ls.tracing_context(enabled=DEBUG_AGENT):
    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": "Find me 5 red Lacoste polos."
            }
        ]
    })
    print(result["messages"][-1].content)