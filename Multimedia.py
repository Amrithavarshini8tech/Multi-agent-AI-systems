import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient


async def main():
    print("Single Agent - Ask the agent")

    model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
        api_key="xxx",
    )

    try:
        assistant = AssistantAgent(
            name="MultiModelAssistant",
            model_client=model_client,
        )

        image = Image.from_file("DodImage.jpg")
        multimodal_message = MultiModalMessage(
            content=["What do you see in this image?", image],
            source="user",
        )

        await Console(assistant.run_stream(task=multimodal_message))
    finally:
        await model_client.close()


asyncio.run(main())
