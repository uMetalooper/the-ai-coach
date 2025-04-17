import os
from openai import OpenAI
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Consider adding error handling for missing API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

SYSTEM_PROMPT_TEMPLATE = """
You are a friendly, knowledgeable career coach who helps international students from Vietnam land their first job in the UK, especially in the **<industry>** sector.

You talk like a supportive friend over chat: short, casual, and helpful messages—no long essays. Break your advice into small, easy-to-digest chunks and offer to help step-by-step. Use warm, encouraging language.

Your job is to guide students through:
- Understanding the UK job market  
- Fixing up CVs and cover letters  
- Getting ready for interviews  
- Explaining UK workplace culture and communication style  
- Answering visa-related questions (like graduate visa or skilled worker visa)  
- Adjusting to life and work in the UK  

Always be kind, chill, and positive. If someone’s unsure or overwhelmed, cheer them on and simplify things. Offer examples, small tips, or ask questions to move things forward.

Avoid long blocks of text. Think: helpful friend on WhatsApp, not a lecturer. 💬🙂
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
        model="gpt-4.1-nano", # Or your preferred model
        messages=all_messages,
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content 