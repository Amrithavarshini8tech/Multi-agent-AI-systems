import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient


async def main():
    print("Hello")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Set the OPENAI_API_KEY environment variable before running this script."
        )

    model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
        api_key=api_key,
    )

    try:
        assistant = AssistantAgent(
            name="assistant",
            model_client=model_client,
        )

        await Console(assistant.run_stream(task="What is 25 * 8?"))
    finally:
        await model_client.close()


asyncio.run(main())