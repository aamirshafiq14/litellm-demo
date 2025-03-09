# Import completion function from litellm.
from litellm import completion

#Import os to fetch API Key from .env file.
import os

#Best practice is to save the api key in .env file and call it using dotenv.
#Import dotenv to fetch all of the information in .env file.
from dotenv import load_dotenv

#Now call the load_dotenv function to make the function effective.
load_dotenv()

#Fetch the GEMINI_API_KEY from os.getenv by saving it in variable api_key.
api_key = os.getenv("GEMINI_API_KEY")

#Now define a function to call the completion function in litellm in order to get response.
def gemini():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        api_key = api_key,
        messages=[{ "content": "What is the capital of Pakistan?","role": "user"}],
)
#To get a refined response, we use below line code    
    print(response['choices'][0]['message']['content'])

def gemini1():
    try:
        response = completion(
#Wrote wrong model name "openai/gemini-2.0-flash-exp",
# instead of "gemini/gemini-2.0-flash-exp" to check try except method
            model="openai/gemini-2.0-flash-exp",
            api_key = api_key,
            messages=[{ "content": "Write a poem about python?","role": "user"}],
            stream = True,
        )
        for part in response:
            print(part['choices'][0]['delta'].get('content', ''), end= '')
    except Exception as e:
        print("An error occurred")

