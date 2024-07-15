from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

if not OPENAI_API_KEY:
    raise Exception("Provide the OpenAI API key as an env variable.")
