import asyncio
import os

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.conditions import TextMentionTermination


async def main():
    print("Multiple Agent")

    model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
        api_key="y_XBqFGkFdVsAZfQo71mbcCRB09nNxYpmKQH6J_IfhAN2wZDkbgopka-oyr9kA",
    )

    # Agent 1: Math Teacher
    AI_agent = AssistantAgent(
            name="MathTeacher",
            model_client=model_client,
            system_message="""
            You are a math teacher.
            Help the student understand and solve math problems.
            Explain concepts clearly with examples.
            Ask follow-up questions to check understanding.

            When the student says THANKS DONE or something similar,
            acknowledge them and respond with exactly:
            LESSON COMPLETE
            """
        )
     # Agent 2: Student (Human)
    Me_user = UserProxyAgent(
            name="student"
            )

    team = RoundRobinGroupChat(
        participants=[AI_agent, Me_user],
        termination_condition=TextMentionTermination("LESSON COMPLETE")
    )

    await Console(
        team.run_stream(task="I need help with Algebra problem, can you help me solve 2*4")
    )
    
    await model_client.close()


asyncio.run(main())

#User — asks questions and participates in the conversation.-> from task
#MathTeacher — explains mathematical concepts and answers questions. -> from roundrobin agent1
#Student — responds to the teacher, asks follow-up questions, and explores the concepts further.-> from roundrobin agent1
#Termination condition: MaxMessageTermination(max_messages=6)
