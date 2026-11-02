import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import MaxMessageTermination


async def main():
    print("Multiple Agent")

    model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
        api_key="YpmKQH6J_IfhAN2wZDkbgopka-oyr9kA",
    )

    
    agent1 = AssistantAgent(
            name="MathTeacher",
            model_client=model_client,
            system_message="you are a math teacher, explain concets clearly and ask follow up questions"
        )

    agent2 = AssistantAgent(
            name="student",
            model_client=model_client,
            system_message="you are a curious student. Ask questions and show case your thinking process"
        )

    team = RoundRobinGroupChat(
        participants=[agent1, agent2],
        termination_condition=MaxMessageTermination(max_messages=6),
    )

    await Console(
        team.run_stream(task="Let's discuss what is multiplication and how it works")
    )
    
    await model_client.close()


asyncio.run(main())

#User — asks questions and participates in the conversation.-> from task
#MathTeacher — explains mathematical concepts and answers questions. -> from roundrobin agent1
#Student — responds to the teacher, asks follow-up questions, and explores the concepts further.-> from roundrobin agent1
#Termination condition: MaxMessageTermination(max_messages=6)
