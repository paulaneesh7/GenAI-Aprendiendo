import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get the API key from environment
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client with the API key
client = OpenAI(api_key=api_key)


system_prompt = """
You are an AI assistant who is expert in breaking down complex problems and then resolve the user query.

For the given user input, analyse the input and break down the problem step by step.
Atleast think 5-6 steps on how to solve the problem before solving it down.

The steps are you get a user input, you analyse, you think, you again think for several times and then return an output with explanation and then finally you validate the output as well before giving final result.

Follow the steps in sequence that is "analyse", "think", "output", "validate" and finally "result".

Rules:
1. Follow the strict JSON output as per Output schema.
2. Always perform one step at a time and wait for next input
3. Carefully analyse the user query

Output Format:
{{ step: "string", content: "string" }}

Example:
Input: What is 2 + 2.
Output: {{ step: "analyse", content: "Alright! The user is intersted in maths query and he is asking a basic arthermatic operation" }}
Output: {{ step: "think", content: "To perform the addition i must go from left to right and add all the operands" }}
Output: {{ step: "output", content: "4" }}
Output: {{ step: "validate", content: "seems like 4 is correct ans for 2 + 2" }}
Output: {{ step: "result", content: "2 + 2 = 4 and that is calculated by adding all numbers" }}


"""


response = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},
    messages=[
        { "role": "system", "content": system_prompt },
        { "role": "user", "content": "what is 3 + 4 * 5" },

        # 
        { "role": "assistant", "content": json.dumps({ "step": "analyse", "content": "The user is asking for the result of an arithmetic expression which involves both addition and multiplication." })  },
        { "role": "assistant", "content": json.dumps({"step": "think", "content": "To solve the expression 3 + 4 * 5, I must remember to follow the order of operations, also known as PEMDAS (Parentheses, Exponents, Multiplication and Division (from left to right), Addition and Subtraction (from left to right))."})  },
        { "role": "assistant", "content": json.dumps({"step": "think", "content": "According to the order of operations, I should perform the multiplication first before the addition."})  },
        { "role": "assistant", "content": json.dumps({"step": "output", "content": "First, calculate 4 * 5, which equals 20."})  },
        { "role": "assistant", "content": json.dumps({"step": "output", "content": "Next, add the result of 4 * 5 to 3, giving us 3 + 20."})  },
        { "role": "assistant", "content": json.dumps({"step": "output", "content": "The result of 3 + 20 is 23."})  },
        { "role": "assistant", "content": json.dumps({"step": "validate", "content": "Double-checking the steps: 3 + (4 * 5) equals 3 + 20, which is 23. The calculation seems accurate."})  },
        { "role": "assistant", "content": json.dumps({"step": "result", "content": "The result of 3 + 4 * 5, following the correct order of operations, is 23."})  },
        { "role": "assistant", "content": json.dumps({"step": "result", "content": "3 + 4 * 5 = 23 and that is calculated by following the order of operations, solving multiplication first and then addition."})  },

    ]
)


print(response.choices[0].message.content)