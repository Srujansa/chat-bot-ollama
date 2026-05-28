READ THIS TO UNDERSTAND RAW  : 
https://chatgpt.com/share/6a168d70-a25c-8321-9244-16402d447dd4
IN LANGCHAIN TRANSITION : https://chatgpt.com/share/6a1699e5-0544-8320-8648-1b9e1a89001b
take-this github to learn langchain : https://github.com/krishnaik06/Langchain-V1-Crash-Course/blob/main
check at the end of chat : https://chatgpt.com/share/6a1699e5-0544-8320-8648-1b9e1a89001b
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
giving structured response so that other ai database can read 


from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama

# task schema
class TaskPlan(BaseModel):
    tasks: list[str] = Field(description="Task list")
    priority: str = Field(description="Overall priority")
    deadline: str = Field(description="Completion deadline")

# initialize model
llm = ChatOllama(model="llama3")

# structured planner model
structured_llm = llm.with_structured_output(
    TaskPlan
)

prompt = """
I need to prepare for interviews,
learn LangChain,
and complete ML project in 10 days.
"""

# generate plan
response = structured_llm.invoke(prompt)

print(response)


| Concept                 | Meaning                   |
| ----------------------- | ------------------------- |
| Middleware              | Logic layer around LLM    |
| SummarizationMiddleware | Compress old history      |
| trigger                 | When summarization starts |
| keep                    | Recent messages preserved |
| checkpointer            | Stores conversation state |
| thread_id               | Unique conversation ID    |
| ToolMessage             | Result from tool          |



full healthcare with all guardlayers implied

Layer 1
ContentFilterMiddleware()

Blocks harmful keywords.

Layer 2
PIIMiddleware()

Masks private data.

Layer 3
HumanInTheLoopMiddleware()

Human approval.

Layer 4
PIIMiddleware(output)

Protects outgoing responses.

Layer 5
SafetyGuardrailMiddleware()

Final AI safety inspection.














# ============================================
# HEALTHCARE AI AGENT WITH 5 GUARDRAIL LAYERS
# ============================================

# pip install langchain langgraph langchain-openai

from typing import Any

from langchain.agents import create_agent
from langchain.agents.middleware import (
    PIIMiddleware,
    HumanInTheLoopMiddleware,
    AgentMiddleware,
    AgentState,
    hook_config
)

from langchain_core.tools import tool
from langchain_core.messages import AIMessage

from langgraph.runtime import Runtime
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

from langchain_openai import ChatOpenAI


# ======================================================
# LAYER 1 : BEFORE_AGENT CONTENT FILTER
# Blocks harmful/off-topic requests before LLM runs
# ======================================================

class HealthcareSafetyFilter(AgentMiddleware):

    # banned dangerous topics
    BLOCKED_TOPICS = [
        "hack",
        "weapon",
        "drug synthesis",
        "suicide",
        "malware"
    ]

    @hook_config(can_jump_to=["end"])
    def before_agent(
        self,
        state: AgentState,
        runtime: Runtime
    ) -> dict[str, Any] | None:

        # if no messages then skip
        if not state["messages"]:
            return None

        # get first user message
        first_msg = state["messages"][0]

        # ensure message is from human
        if first_msg.type != "human":
            return None

        # convert input to lowercase
        content = first_msg.content.lower()

        # check banned topics
        for topic in self.BLOCKED_TOPICS:

            if topic in content:

                print(f"🚫 BLOCKED TOPIC: {topic}")

                # stop workflow immediately
                return {
                    "messages": [
                        {
                            "role": "assistant",
                            "content": (
                                "I can only help with safe healthcare-related requests."
                            )
                        }
                    ],

                    # terminate agent execution
                    "jump_to": "end"
                }

        return None


# ======================================================
# LAYER 5 : AFTER_AGENT OUTPUT VALIDATOR
# Adds medical disclaimer after AI generates response
# ======================================================

class MedicalOutputValidator(AgentMiddleware):

    DISCLAIMER = (
        "\n\n⚕️ This is general health information."
        " Please consult a doctor."
    )

    @hook_config(can_jump_to=["end"])
    def after_agent(
        self,
        state: AgentState,
        runtime: Runtime
    ) -> dict[str, Any] | None:

        # skip if no messages
        if not state["messages"]:
            return None

        # get last AI response
        last_message = state["messages"][-1]

        # ensure message is AI generated
        if not isinstance(last_message, AIMessage):
            return None

        # append disclaimer to response
        last_message.content += self.DISCLAIMER

        return None


# ======================================================
# TOOL 1 : SEARCH SYMPTOMS
# AI uses this tool to search disease symptoms
# ======================================================

@tool
def search_symptoms(symptoms: str) -> str:
    """
    Search medical symptoms.
    """

    return (
        f"Symptoms related to {symptoms} found."
    )


# ======================================================
# TOOL 2 : MEDICATION INFO
# AI uses this tool for medicine information
# ======================================================

@tool
def medication_info(medicine: str) -> str:
    """
    Get medicine details.
    """

    return (
        f"{medicine} is commonly used in healthcare."
    )


# ======================================================
# TOOL 3 : BOOK APPOINTMENT
# Sensitive action requiring human approval
# ======================================================

@tool
def book_appointment(
    patient_name: str,
    doctor: str,
    date: str
) -> str:
    """
    Book hospital appointment.
    """

    return (
        f"Appointment booked for "
        f"{patient_name} with Dr.{doctor} on {date}"
    )


# ======================================================
# CREATE HEALTHCARE AGENT
# All 5 guardrail layers added here
# ======================================================

healthcare_agent = create_agent(

    # main LLM
    model="gpt-4o",

    # available tools
    tools=[
        search_symptoms,
        medication_info,
        book_appointment
    ],

    # middleware layers
    middleware=[

        # =====================================
        # LAYER 1 : INPUT FILTER
        # blocks harmful requests
        # =====================================
        HealthcareSafetyFilter(),

        # =====================================
        # LAYER 2 : INPUT PII REDACTION
        # hides emails before model sees them
        # =====================================
        PIIMiddleware(
            "email",
            strategy="redact",
            apply_to_input=True
        ),

        # =====================================
        # LAYER 3 : INPUT CREDIT CARD MASKING
        # masks sensitive card numbers
        # =====================================
        PIIMiddleware(
            "credit_card",
            strategy="mask",
            apply_to_input=True
        ),

        # =====================================
        # LAYER 4 : HUMAN APPROVAL
        # pauses before appointment booking
        # =====================================
        HumanInTheLoopMiddleware(
            interrupt_on={

                # approval required
                "book_appointment": True,

                # auto approved
                "search_symptoms": False,
                "medication_info": False
            }
        ),

        # =====================================
        # LAYER 5 : OUTPUT VALIDATION
        # adds medical disclaimer
        # =====================================
        MedicalOutputValidator()
    ],

    # stores paused state/memory
    checkpointer=InMemorySaver(),

    # system instructions for AI
    system_prompt=(
        "You are a healthcare assistant. "
        "Help users with symptoms, medicines, "
        "and appointments safely."
    )
)


# ======================================================
# TEST 1 : NORMAL MEDICAL QUERY
# Safe request passes through all layers
# ======================================================

config = {
    "configurable": {
        "thread_id": "health_session_1"
    }
}

result = healthcare_agent.invoke(

    {
        "messages": [
            {
                "role": "user",
                "content": (
                    "What are symptoms of diabetes?"
                )
            }
        ]
    },

    config=config
)

print("\n=== SAFE RESPONSE ===\n")

print(result["messages"][-1].content)


# ======================================================
# TEST 2 : PII REDACTION
# Email gets hidden automatically
# ======================================================

result = healthcare_agent.invoke(

    {
        "messages": [
            {
                "role": "user",

                "content": (
                    "My email is john@gmail.com "
                    "What medicine helps headache?"
                )
            }
        ]
    },

    config=config
)

print("\n=== PII REDACTION ===\n")

print(result["messages"][-1].content)


# ======================================================
# TEST 3 : BLOCK HARMFUL REQUEST
# Dangerous request blocked before AI runs
# ======================================================

result = healthcare_agent.invoke(

    {
        "messages": [
            {
                "role": "user",

                "content": (
                    "How to synthesize drugs?"
                )
            }
        ]
    },

    config=config
)

print("\n=== BLOCKED REQUEST ===\n")

print(result["messages"][-1].content)


# ======================================================
# TEST 4 : HUMAN APPROVAL FLOW
# Appointment booking pauses for approval
# ======================================================

appointment_config = {
    "configurable": {
        "thread_id": "appointment_1"
    }
}

# step 1 : invoke request
result = healthcare_agent.invoke(

    {
        "messages": [
            {
                "role": "user",

                "content": (
                    "Book appointment with "
                    "Dr Sharma on Monday"
                )
            }
        ]
    },

    config=appointment_config
)

print("\n=== WAITING FOR APPROVAL ===\n")

print(result)


# ======================================================
# STEP 2 : HUMAN APPROVES
# Resume paused workflow
# ======================================================

approved = healthcare_agent.invoke(

    Command(
        resume={
            "decisions": [
                {
                    "type": "approve"
                }
            ]
        }
    ),

    config=appointment_config
)

print("\n=== APPROVED RESPONSE ===\n")

print(approved["messages"][-1].content)


