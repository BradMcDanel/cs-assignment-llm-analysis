import os
from copy import deepcopy

import openai
import anthropic

api_key = os.getenv("OPENAI_API_KEY", "")
if api_key != "":
    openai.api_key = api_key
else:
    print("Warning: OPENAI_API_KEY is not set")

ant_api_key = os.getenv("ANTHROPIC_API_KEY", "")
if ant_api_key != "":
    ant_client = anthropic.Anthropic(api_key=ant_api_key)
else:
    ant_client = None
    
def call(messages, **kwargs) -> list:
    model = kwargs["model"]
    if "claude" in model:
        # handle system message for anthropic
        if messages[0]["role"] == "system":
            messages = deepcopy(messages)
            system = messages[0]["content"]
            messages.pop(0)
        else:
            system = None
            
        res = ant_client.messages.create(
            messages=messages,
            system=system,
            max_tokens=kwargs.get("max_tokens", 4096),
            **kwargs
        )
        return res.content[0].text
    else: # OPENAI
        res = openai.ChatCompletion.create(messages=messages, **kwargs)
        return res["choices"][0]["message"]["content"]

