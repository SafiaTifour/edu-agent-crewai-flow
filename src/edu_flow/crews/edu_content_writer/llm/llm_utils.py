from dotenv import load_dotenv
import os
from crewai import LLM

load_dotenv()

def get_llm():
    api_key = os.getenv("OPENROUTER_API_KEY")
    return LLM(
        model="openrouter/deepseek/deepseek-r1",
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )
