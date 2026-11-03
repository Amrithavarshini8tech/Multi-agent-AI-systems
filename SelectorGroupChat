import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.conditions import (
    MaxMessageTermination,
    TextMentionTermination
)
from autogen_agentchat.teams import SelectorGroupChat

async def main():
    print("Multiple Agent")

    model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
        api_key="sqTy_XBqFGkFdkA",
    )

    
    researcher = AssistantAgent(
            name="research",
            model_client=model_client,
            system_message="you are a researcher. your role is to gather information and create well-written articles. just provide reseach data and facts "
        )

    writer = AssistantAgent(
            name="writerAgent",
            model_client=model_client,
            system_message="You are a writer. your role is to take research information and create well-written articles. wait for the reasearch to be provoided, then write the content"
        )

    critic = AssistantAgent(
            name="criticAgent",
            model_client=model_client,
            system_message="you are a critic. review written content and provide fedback. say 'TERMINATE' when satisfied with the final result"
        )

    max_messages_termination=MaxMessageTermination(max_messages=6)
    text_termination=TextMentionTermination("TERMINATE")

    termination = text_termination |max_messages_termination
    team=SelectorGroupChat(participants=[critic, writer, researcher], model_client=model_client, termination_condition=termination, allow_repeated_speaker=True)

    await Console(
        team.run_stream(task="Research on renewable energy trend")
    )
    
    await model_client.close()


asyncio.run(main())

#User — asks questions and participates in the conversation.-> from task
#MathTeacher — explains mathematical concepts and answers questions. -> from roundrobin agent1
#Student — responds to the teacher, asks follow-up questions, and explores the concepts further.-> from roundrobin agent1
#Termination condition: MaxMessageTermination(max_messages=6)
