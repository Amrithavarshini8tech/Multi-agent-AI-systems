import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient


async def main():
    print("Single Agent - Ask the agent")


    model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
        api_key="xx",
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
