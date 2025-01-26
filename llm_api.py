import requests

def call_llm_api(query):
    # Replace with the actual API endpoint and API key
    api_endpoint = "https://api.example.com/llm"
    api_key = "your_api_key"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "query": query
    }

    response = requests.post(api_endpoint, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "API call failed"}

# Example usage
if __name__ == "__main__":
    query = "What is the capital of France?"
    response = call_llm_api(query)
    print(response)
