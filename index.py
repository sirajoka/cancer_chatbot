import os
import requests

from dotenv import load_dotenv


load_dotenv()

# Get the values from environment variables
customer_id = os.getenv("CUSTOMER_ID")
x_api_key = os.getenv("X_API_KEY")
customerid = os.getenv("CUSTOMERID")
tokens = os.getenv("TOKEN")

def Chatbot(query):
    
    url = 'https://api.vectara.io/v1/query'

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'customer-id': customer_id,
        'x-api-key': x_api_key
    }


    data = {
        "query": [
            {
                "query": query,
                "start": 0,
                "numResults": 5,
                "corpusKey": [
                    {
                        "customerId": customerid,
                        "corpusId": 2,
                        "semantics": "DEFAULT",
                        "dim": [
                            {
                                "name": "string",
                                "weight": 0
                            }
                        ],
                        "metadataFilter": "part.lang = 'eng'",
                        "lexicalInterpolationConfig": {
                            "lambda": 0
                        }
                    }
                ],
                "rerankingConfig": {
                    "rerankerId": 272725717
                },
                "summary": [
                    {
                        "summarizerPromptName": "string",
                        "maxSummarizedResults": 0,
                        "responseLang": "string"
                    }
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_json = response.json()

            # Check if results are available
        if "responseSet" in response_json and len(response_json["responseSet"]) > 0:
                        # Extract and print the text from each response
            for result in response_json["responseSet"][0]["response"]:
                text = result.get("text", "")
                                                       # print("Extracted Text:")
                #print(text)
        else:
            print("No results were found for the query.")
    else:
        print(f"Request failed with status code: {response.status_code}")
    s = requests.Session()

    #api_base = os.getenv("OPENAI_API_BASE")
    #token = os.getenv("OPENAI_API_KEY")
    api_base = "https://api.endpoints.anyscale.com/v1"
    token = tokens 
    url = f"{api_base}/chat/completions"
    body = {
      "model": "meta-llama/Llama-2-70b-chat-hf",
        "messages": [{"role": "system", "content": "Your name is Kamal and you are a helpful and casual consultation doctor , you will extract and summarize factual information from {text} and give an accurate response(don't summarize links so write them as source), The is information from {text} is to prevent you from hallucination and guide you to provide factual information. Make sure you are conversational, use relevant emojis in some some cases. You understand how to handle compliment and greetings such as Hello, what's up, hey, Thank you etc. In a circumstance in which you don't have enough information just say 'I'm out of information, can say something different?' "}, {"role": "user", "content": ask}],
          "temperature": 0.7
          }

    response = s.post(url, headers={"Authorization": f"Bearer {token}"}, json=body)

    if response.status_code == 200:
        response_json = response.json()
        chatbot_response = response_json["choices"][0]["message"]["content"]
                      #print("Chatbot Response:")
        print(chatbot_response)
    else:
        print(f"Request failed with status code: {response.status_code}")
                                            
ask = input()
answer = Chatbot(ask)

print(answer)


