import asyncio
from dotenv import load_dotenv

from agentscope.message import Msg, UserMsg
from openai import APIStatusError
from agents.clothing_agent_agentscope import build_clothing_agent

async def main():

    load_dotenv()

    agent = build_clothing_agent()

    while True:
        question = input("\nYou: ")

        if question.lower() in ["exit", "quit"]:
            break

        try:
            response = await agent.reply(
                Msg(
                name="user",
                role="user",
                content=[{"type": "text", "text": question}],
        )
            )
        except APIStatusError as e:
            print("Status:", e.status_code)
            print("Error body:", e.response.text)
            raise

        print("\nAgent:", response.get_text_content())


if __name__ == "__main__":
    asyncio.run(main())