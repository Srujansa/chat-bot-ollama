READ THIS TO UNDERSTAND RAW  : 
https://chatgpt.com/share/6a168d70-a25c-8321-9244-16402d447dd4
IN LANGCHAIN TRANSITION : https://chatgpt.com/share/6a1699e5-0544-8320-8648-1b9e1a89001b
full agentic workflow ofopeai chatbot  :  
import os
from dotenv import load_dotenv
from langchain.agents import create_agent

# Load API key from .env
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


# ---------------- TOOL 1 ----------------
# Weather tool

def get_weather(city: str) -> str:
    """Get weather of a city."""

    return f"The weather in {city} is 32°C and sunny."


# ---------------- TOOL 2 ----------------
# Calculator tool

def add_numbers(a: int, b: int) -> str:
    """Add two numbers."""

    return f"Sum is {a + b}"


# ---------------- TOOL 3 ----------------
# Movie recommendation tool

def recommend_movie(genre: str) -> str:
    """Recommend movie based on genre."""

    return f"Recommended {genre} movie: Inception"


# ---------------- CREATE AGENT ----------------
# Agent gets access to all tools

agent = create_agent(

    model="gpt-5",

    tools=[
        get_weather,
        add_numbers,
        recommend_movie
    ],

    system_prompt="You are a helpful AI assistant."
)


# ---------------- RUN AGENT ----------------
# User asks multiple things

response = agent.invoke({

    "messages": [

        {
            "role": "user",

            "content":
            """
            What is the weather in Mysore?
            Also add 10 and 20.
            Recommend a sci-fi movie.
            """
        }

    ]
})


# ---------------- PRINT FINAL ANSWER ----------------

print(response["messages"][-1].content)
