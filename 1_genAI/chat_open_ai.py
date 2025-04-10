import os
from openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()



client = OpenAI(
    # This is the default and can be omitted
    api_key = os.getenv('OPENAI_API_KEY')
)


response = client.responses.create(
    model="gpt-4o",
    instructions="You are a coding assistant that talks like a pirate.",
    input="How do I check if a Python object is an instance of a class?",
)

print(response.output_text)


# Currently this won't work as I don't have any credit in my open_ai_account