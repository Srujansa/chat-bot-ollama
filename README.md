READ THIS TO UNDERSTAND RAW  : 
https://chatgpt.com/share/6a168d70-a25c-8321-9244-16402d447dd4
IN LANGCHAIN TRANSITION : https://chatgpt.com/share/6a1699e5-0544-8320-8648-1b9e1a89001b
take-this github to learn langchain : https://github.com/krishnaik06/Langchain-V1-Crash-Course/blob/main
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

















# =========================================================
#        LANGCHAIN MODEL INTEGRATION EXAMPLES
# =========================================================

# This file shows:
# 1. OpenAI model
# 2. Gemini model
# 3. Groq model
# 4. Streaming
# 5. Batch processing


# =========================================================
#                 LOAD API KEYS
# =========================================================

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Store API keys in environment
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


# =========================================================
#          METHOD 1 : init_chat_model()
# =========================================================

# Generic model initializer
# Automatically detects provider

from langchain.chat_models import init_chat_model


# ---------------------------------------------------------
# OPENAI MODEL
# ---------------------------------------------------------

model = init_chat_model("gpt-4.1")

response = model.invoke("Hello how are you?")

print(response.content)


# =========================================================
#           METHOD 2 : ChatOpenAI
# =========================================================

# Direct OpenAI integration

from langchain_openai import ChatOpenAI


# Create OpenAI model
model = ChatOpenAI(

    model="gpt-4.1",

    temperature=0.7
)

# Send prompt to model
response = model.invoke("Explain AI simply")

# Print only text content
print(response.content)


# =========================================================
#           GOOGLE GEMINI INTEGRATION
# =========================================================

# Direct Gemini integration

from langchain_google_genai import ChatGoogleGenerativeAI


# Create Gemini model
model = ChatGoogleGenerativeAI(

    model="gemini-2.5-flash-lite"
)

# Ask question
response = model.invoke("Why do parrots talk?")

# Print response
print(response.content)


# =========================================================
#              GROQ MODEL INTEGRATION
# =========================================================

# Groq provides very fast inference

from langchain_groq import ChatGroq


# Create Groq model
model = ChatGroq(

    model="qwen/qwen3-32b"
)

# Ask question
response = model.invoke("What is quantum computing?")

# Print response
print(response.content)


# =========================================================
#                     STREAMING
# =========================================================

# stream()
# gives output token by token

for chunk in model.stream(

    "Write 100 words on Artificial Intelligence"

):

    # Print chunks in real-time
    print(chunk.text, end="", flush=True)


# =========================================================
#                    BATCH PROCESSING
# =========================================================

# batch()
# runs multiple prompts together

responses = model.batch([

    "What is AI?",

    "What is Machine Learning?",

    "What is Deep Learning?"
])


# Loop through all responses
for response in responses:

    print("\n")
    print(response.content)


# =========================================================
#                IMPORTANT FUNCTIONS
# =========================================================

# invoke()
# Single request

# stream()
# Real-time output

# batch()
# Multiple prompts together


# =========================================================
#                IMPORTANT MODEL CLASSES
# =========================================================

# ChatOpenAI
# OpenAI GPT models

# ChatGoogleGenerativeAI
# Gemini models

# ChatGroq
# Groq hosted models

# init_chat_model()
# Generic universal initializer


# =========================================================
#               IMPORTANT RESPONSE OBJECT
# =========================================================

# response.content
# actual text generated by model

# response
# full metadata + tokens + model info


# =========================================================
#                   EXAMPLE .env FILE
# =========================================================

"""
OPENAI_API_KEY=your_openai_key

GOOGLE_API_KEY=your_google_key

GROQ_API_KEY=your_groq_key
"""
