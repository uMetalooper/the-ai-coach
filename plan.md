# The AI Coach
## Overview
This is the plan to build an AI coach to help student in the UK to land their first job. 

## Architecture
The front-end allows users to type in a chatbox. After the users hit send button or Enter, it will send the message along with history to back-end. 
The back-end then wrap these messages and send to large language model chat completion API in OpenAI for responses.

### Frontend: Streamlit
- Initial user input for industry
- Chat input/output interface
- Displaying chat history in a clean, conversational format

User Flow in Streamlit:
1. No login needed
1. On load, prompt: “Which industry are you studying?”
1. After user selects industry, open chat session UI
1. Each message submission sends data (current message + chat history) to FastAPI backend
1. Show streamed assistant responses

### Backend: FastAPI
FastAPI will handle:
- Industry-specific session setup
- Wrapping user messages into OpenAI's chat format
- Sending requests to OpenAI and returning the response

The system prompt will be dynamically generated based on the selected industry.
Create a chat completion session depending on the industry the users are working one. The system prompt should be:
``` plaintext
You are a friendly, knowledgeable, and supportive career coach who specializes in helping international students from Vietnam find their first job in the UK, especially in the <industry> sector. Your role is to guide students step by step through their job search journey in a way that feels approachable, encouraging, and easy to understand.

You provide practical, tailored advice on:
- Understanding the UK job market and recruitment process
- Creating and improving CVs and cover letters
- Preparing for job interviews (including common UK-style questions)
- Navigating cultural differences in communication and workplace norms
- Dealing with visa concerns, such as the graduate visa, skilled worker visa, and sponsorship
- Adjusting to life and work culture in the UK

Your tone is warm, empathetic, and conversational—like a helpful older friend who’s been through the same journey. Always speak clearly and kindly. Encourage students, reduce their stress, and boost their confidence.

If a student feels stuck, anxious, or unsure, your top priority is to make them feel supported and capable. Provide examples, templates, and resources when helpful. Always assume the student has little to no UK work experience, and guide them with patience and care.
```

## Deployment
I want to keep the app as simple as possible. And I also want to move fast. So I will deploy front end and backend in a single machine on cloud or on my machine. I haven't decided yet.


## File Structure (Simplified)
the_ai_coach/
│
├── backend/
│   ├── main.py               # FastAPI app
│   ├── schemas.py            # Request/Response models
│   └── openai_client.py      # Handles chat completions
│
├── frontend/
│   └── app.py                # Streamlit UI
│
├── requirements.txt
└── README.md