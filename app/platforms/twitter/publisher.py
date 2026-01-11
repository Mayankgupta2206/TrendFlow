from .config import get_client

def post_tweet(text):
    client = get_client()
    response = client.create_tweet(text=text)
    print("✅ Tweet posted successfully:", response.data["id"])
