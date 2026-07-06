markdown# Vibe Check Bot 🤗

A supportive FastAPI + Groq AI bot that acts like a caring friend - listens to your problems and responds with empathy and encouragement.

## How it works

1. Send a message describing how you're feeling via a POST request
2. The API sends it to Groq's LLM (llama-3.3-70b-versatile) with a "supportive friend" system prompt
3. The AI detects the emotion/context on its own (no separate mood field needed) and responds with empathy, comfort, or encouragement

## Tech Stack

- **FastAPI** - web framework for the API
- **Pydantic** - request/response validation
- **Groq API** - LLM for generating supportive responses
- **python-dotenv** - environment variable management

## Project Structure
vibe-check-bot/
├── main.py           # FastAPI app + route
├── groq_client.py     # Groq API call logic (system + user prompts)
├── schemas.py         # Pydantic request/response models
├── .env                # API key (not committed)
└── requirements.txt

## Setup

1. Clone the repo
2. Install dependencies:
pip install -r requirements.txt
3. Create a `.env` file with your Groq API key:
GROQ_API_KEY=your_key_here
4. Run the server:
python -m uvicorn main:app --reload

## API Usage

**POST** `/chat`

Request body:
```json
{
  "message": "I'm feeling really nervous about my exam tomorrow"
}
```

Response:
```json
{
  "reply": "Hey, it's so great that you reached out! I'm here for you..."
}
```

## Author

Built by Bilal (Dhani Baksh) as part of learning AI integration - prompt engineering to let the AI infer context/emotion without explicit fields.
