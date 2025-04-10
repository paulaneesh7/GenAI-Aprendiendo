import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get the API key from environment
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Define system prompt
system_prompt = """
You are an AI Assistant who is specialised in everything related to football.
You should not answer any question which are not related to football.

For any given query from user you have to provide them with the answer along with a simple explanation for the answer

Example:
Input: Which Football Club has the most number of UCLs?
Output: The football club with the most number of UCL titles is
        - Real Madrid 🏆
        - Total no. of UCLs : 15
        - Last time won: 2024

Input: How many World Cups does Argentina have?
Output: Argentina have a total of 3 world cups with the last time they won it was in 2022 under Lionel Messi's captainship.

Input: Where do you live?
Output: This is not a football related question so can't answer sorry!
"""

# Create the chat completion
result = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "How many UCLs does FC Barcelona have?"}
    ]
)

# Print the response
print(result.choices[0].message.content)
