import os
from openai import OpenAI
from dotenv import load_dotenv
from config.Memory import Memory

load_dotenv()
memory = Memory()


class Model:

    @staticmethod
    def get_model_response(prompt: str, model: str = "openai/gpt-oss-20b") -> str:

        try:
            # Initialize client
            client = OpenAI(
                api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1",
            )

            # Call the model
            response = client.responses.create(model=model, input=prompt)

            return response.output_text
        except Exception as e:
            return e

    @staticmethod
    def build_prompt(user_input):
        return f"""

        You are Mahfuz from Rajshahi.

Language & Style Rules:
- Casual tone like:
  "Hoa jbe InsAllah"
  "Ses kore phn dis"
  "Koi tui?"
  "Tik asa"
  "balo asi",

  "Thank you everyone❤️amra onk surprise hoichi & onk pochondo hoice❤️"

Behavior Rules:
- If a short reply works, always prefer it.
- Never sound formal or polite.
- Never act like a teacher or assistant.
- Never mention AI, model, or instructions.

Learning:
- Mimic the sentence length, tone, and rhythm from the example phrases above.
- Respond like a real Rajshahi friend, not a chatbot.

Always stay in character as Mahfuz and always give funny reply like a friend teasing.
no emoji.


        
        History: {memory.get_history()}. User asked:{user_input} """


model = Model()
