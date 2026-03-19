from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#        Gemini FAST Api
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

@app.post("/chat-gemini")
async def chat_gemini(prompt: str):
    try:
        print("Received:", prompt)

        response = model.generate_content(prompt)

        print("Response:", response)
        return {"reply": response.text}

    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}