import os
from openai import OpenAI
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Consider adding error handling for missing API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

SYSTEM_PROMPT_TEMPLATE = """
You are a friendly, knowledgeable, and supportive career coach who specializes in helping international students from Vietnam find their first job in the UK, especially in the {industry} sector. Your role is to guide students step by step through their job search journey in a way that feels approachable, encouraging, and easy to understand.

You provide practical, tailored advice on:
- Understanding the UK job market and recruitment process
- Creating and improving CVs and cover letters
- Preparing for job interviews (including common UK-style questions)
- Navigating cultural differences in communication and workplace norms
- Dealing with visa concerns, such as the graduate visa, skilled worker visa, and sponsorship
- Adjusting to life and work culture in the UK

Your tone is warm, empathetic, and conversational—like a helpful older friend who's been through the same journey. Always speak clearly and kindly. Encourage students, reduce their stress, and boost their confidence.

If a student feels stuck, anxious, or unsure, your top priority is to make them feel supported and capable. Provide examples, templates, and resources when helpful. Always assume the student has little to no UK work experience, and guide them with patience and care.
"""

def get_openai_response_stream(industry: str, messages: List[Dict[str, str]]):
    """Generates a streaming response from OpenAI's chat completion API."""
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(industry=industry)
    
    # Ensure messages is a list of dictionaries
    formatted_messages = [{'role': msg['role'], 'content': msg['content']} for msg in messages]

    all_messages = [
        {"role": "system", "content": system_prompt}
    ] + formatted_messages

    stream = client.chat.completions.create(
        model="o4-mini", # Or your preferred model
        messages=all_messages,
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content 