from google import genai
from google.genai import types

from config import API_KEY, LLM_MODEL, SYS_PROMPT


# def get_llm():
#     client = genai.Client(api_key=API_KEY)
#     model = client.get_model(LLM_MODEL)
#     return model
client = genai.Client(api_key=API_KEY)
#model = client.get_model(LLM_MODEL)

def generate_response(msg):
    #lm_model = get_llm()

    response = client.models.generate_content(
        # types.GenerateContentConfig(
        #     model=LLM_MODEL,
        #     contents=[
        #         types.Content(
        #             text=SYS_PROMPT
        #         ),
        #         types.Content(
        #             #text=msg[-1]["content"]
        #             text = msg
        #         )
        #     ]
        # )
        model=LLM_MODEL,
        # contents=[
        #     types.Content(text=SYS_PROMPT),
        #     types.Content(text=msg)
        # ]
        contents=msg, 
        config=types.GenerateContentConfig(
            # Pass the System Prompt here for better instruction following
            system_instruction=SYS_PROMPT
            # temperature=0.7, # Optional: Adjust creativity
        )
    )
    return response.text