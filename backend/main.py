from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from .schemas import ChatRequest
from .openai_client import get_openai_response_stream

app = FastAPI()

# --- CORS Middleware --- 
# Allows requests from Streamlit frontend (default port 8501)
origins = [
    "http://localhost",
    "http://localhost:8501",
    "http://127.0.0.1",
    "http://127.0.0.1:8501",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"], # Allow all methods (GET, POST, etc.)
    allow_headers=["*"], # Allow all headers
)
# --- End CORS --- 

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """Receives chat history and streams back the response."""
    # Convert Pydantic models back to dicts for the OpenAI client function
    messages_dict = [msg.model_dump() for msg in request.messages] # Use model_dump()
    
    # Get the streaming generator
    response_stream = get_openai_response_stream(request.industry, messages_dict)
    
    # Return a StreamingResponse
    # Use text/plain for simpler streaming handling in requests library
    return StreamingResponse(response_stream, media_type="text/plain")

# # Optional: Add CORS middleware if frontend and backend run on different origins
# # from fastapi.middleware.cors import CORSMiddleware
# # origins = [
# #     "http://localhost",
# #     "http://localhost:8501",  # Default Streamlit port
# # ]
# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=origins,
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # ) 