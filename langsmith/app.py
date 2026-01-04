from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv(override=True)

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

def get_air_quality(city: str) -> str:
    """Get air quality for a given city."""
    return f"The air quality in {city} is always good!"

agent = create_agent(
    model="openai:gpt-4o-mini",
    tools=[get_weather, get_air_quality],
    system_prompt="Never answer questions about the weather",
)

if __name__ == "__main__":
    # Run the agent
    agent.invoke(
        {"messages": [{"role": "user", "content": "What is the air quality in San Francisco?"}]}
    )

