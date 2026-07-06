from dotenv import load_dotenv
from groq import Groq
import os


load_dotenv()

client = Groq(api_key = os.getenv("groq_api_key"))
def get_motivation(query : str):
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [{"role" : "user" , "content" : query },
                    
                   {"role" : "system","content" : "act like a close and humble and supportive friend who listen to problems motivate and give advice and help them to revocer from any frustration ,heartbreak,sadness and personal problems"}
                   ]
    )

    return response.choices[0].message.content