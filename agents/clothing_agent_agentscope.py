import inspect
import os

from agentscope import model
from agentscope.agent import Agent
from agentscope.credential import OpenAICredential
from agentscope.model import OpenAIChatModel

from formatters.mistral_formatter import MistralFormatter
from tools.clothing_tools import build_clothing_toolkit
from prompts.clothing_assistant import CLOTHING_ASSISTANT_PROMPT


def build_clothing_agent():
    credential = OpenAICredential(
        api_key=os.environ["MISTRAL_API_KEY"],
        base_url="https://api.mistral.ai/v1",
    )

    model = OpenAIChatModel(
        model="mistral-small-2506",
        credential=credential,
        formatter=MistralFormatter(),
        stream=False
    )

    # print("Formatter:", model.formatter)
    # print("Formatter class:", type(model.formatter))
    # print("Bound format signature:", inspect.signature(model.formatter.format))

    return Agent(
        name="ClothingAssistant",
        system_prompt=CLOTHING_ASSISTANT_PROMPT,
        model=model,
        toolkit=build_clothing_toolkit(),
    )