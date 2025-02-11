# Deepseek-R1 Integration using OPENROUTER:

* This script demonstrates how to use OpenRouter.ai as an API proxy for OpenAI-compatible models, specifically the DeepSeek-R1 model.

## Features:
Uses OpenRouter.ai as a gateway to access AI models.
Supports setting custom HTTP headers for ranking on OpenRouter.
Sends a chat completion request to the DeepSeek-R1 model.

## Install the OpenAI Python SDK:
pip install openai
Get an API key from OpenRouter.

## Usage:
1. Import OpenAI and Initialize Client

* from openai import OpenAI

* client = OpenAI(
*  base_url="https://openrouter.ai/api/v1",  # OpenRouter API endpoint
*  api_key="your-api-key",  # Replace with your actual OpenRouter API key)

base_url: Directs requests to OpenRouter instead of OpenAI’s official API.
api_key: Required for authentication.

2. Sending a Chat Completion Request

* completion = client.chat.completions.create(
*  extra_headers={
*    "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional: Helps with ranking on OpenRouter.ai
*    "X-Title": "<YOUR_SITE_NAME>",  # Optional: Site title for ranking on OpenRouter.ai
*  },
*  extra_body={},  # Reserved for additional API parameters
*  model="deepseek/deepseek-r1:free",  # Specifies the AI model to use
* messages=[
*    {
      "role": "user",
      "content": "How a non technical user transit to data analyst?"
    }
  ]
* )

Sends a message to the AI model as a user query.
The model processes the request and returns a response.

## 3. Print the Response

print(completion.choices[0].message.content)

Extracts and prints the model's response from the completion object.

## Example Output

Transitioning to a data analyst role involves learning SQL, Python, and data visualization tools like Power BI or Tableau. Start with online courses, practice datasets, and work on smal
