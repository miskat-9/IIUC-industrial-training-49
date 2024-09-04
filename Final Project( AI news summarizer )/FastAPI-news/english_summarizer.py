import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client with API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize(text):
    # Hypothetical model ID for summarization
    model_id = "groq-summarizer-large"  # Replace with the actual model ID from Groq

    # Request completion from Groq API
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Please summarize the following text in English: {text}",
            }
        ],
        model=model_id,
    )

    # Return the summary
    return chat_completion.choices[0].message.content
