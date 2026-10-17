from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

# open-mistral-nemo-2407 12B params
# mistral-small-2506 24B params
# devstral-small-2507 24B params
llm = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0,
)