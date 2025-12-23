from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../.env", override=True)

if __name__ == "__main__":
    print(os.getenv("OPENAI_API_KEY"))