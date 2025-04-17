# AI Career Coach

This application provides AI-powered career coaching for Vietnamese students seeking jobs in the UK, tailored to specific industries.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd the_ai_coach
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up OpenAI API Key:**
    Create a `.env` file in the root directory (`the_ai_coach/`) and add your OpenAI API key:
    ```
    OPENAI_API_KEY='your_openai_api_key_here'
    ```
    Replace `'your_openai_api_key_here'` with your actual key.

## Running the Application

You need to run the backend (FastAPI) and frontend (Streamlit) separately.

1.  **Run the Backend (FastAPI):**
    Open a terminal, navigate to the root directory (`the_ai_coach/`), and run:
    ```bash
    uvicorn backend.main:app --reload
    ```
    The backend will usually be available at `http://localhost:8000`.

2.  **Run the Frontend (Streamlit):**
    Open a *second* terminal, navigate to the root directory (`the_ai_coach/`), and run:
    ```bash
    streamlit run frontend/app.py
    ```
    The frontend will usually open automatically in your browser at `http://localhost:8501`.

3.  **Interact:**
    Go to the Streamlit app in your browser, enter an industry, and start chatting with the AI coach! 