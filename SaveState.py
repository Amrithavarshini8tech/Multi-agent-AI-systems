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
        api_key="sk-proj---oyr9kA",
    )

    
    agent1 = AssistantAgent(
            name="Helper",
            model_client=model_client)

    agent2 = AssistantAgent(
            name="BackupHelper",
            model_client=model_client)

    team = RoundRobinGroupChat(
        participants=[agent1, agent2],
        termination_condition=MaxMessageTermination(max_messages=3),
    )

    await Console(
        team.run_stream(task="My favourite colour is blue")
    )
    state=await agent1.save_state()
    with open("memory.json", "w") as f:
        json.dump(state, f, default=str)

    with open("memory.json", "r") as f:
        saved_state = json.load(f)

    await agent2.load_state(saved_state)
    
    await Console(agent2.run_stream(task="what is my favorite colour?"))
    
    await model_client.close()


asyncio.run(main())

#User — asks questions and participates in the conversation.-> from task
#MathTeacher — explains mathematical concepts and answers questions. -> from roundrobin agent1
#Student — responds to the teacher, asks follow-up questions, and explores the concepts further.-> from roundrobin agent1
#Termination condition: MaxMessageTermination(max_messages=6)
