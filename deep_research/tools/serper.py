import requests
import json
import os
from models.serper import SerperSearchResult

def Search(query: str) -> SerperSearchResult:
    url = "https://google.serper.dev/search"

    payload = json.dumps({
        "q": query
    })

    serper_api_key = os.getenv("SERPER_API_KEY")

    headers = {
        'X-API-KEY': serper_api_key,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return SerperSearchResult(**response.json())
