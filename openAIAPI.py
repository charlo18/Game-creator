import os
from openai import OpenAI
from dotenv import load_dotenv

class AIModel:
    def __init__(self):
        self.client = None
        self._load_api_key()

    #to hide key
    def _read_Key(self):
        with open('apiKey.txt', 'r', encoding='utf-8') as f:
            return f.read().strip()

    #values for the model
    def get_llm_response(self,prompt):
        completion = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "system","content": "You are an AI assistant.",},{"role": "user", "content": prompt},],temperature=0.0,)
        response = completion.choices[0].message.content
        return response

    #load the api key
    def _load_api_key(self):
        self.client = OpenAI(api_key = self._read_Key())
    
