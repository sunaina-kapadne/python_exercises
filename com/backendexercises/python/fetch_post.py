import requests

def fetch_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        response = requests.get(url, timeout=5)  # 5 second timeout
        response.raise_for_status()  # Raise error for bad status codes (e.g. 404, 500)
        return response.json()  # Convert response body to Python dict
    except requests.RequestException as e:
        print(f"Error fetching post {post_id}: {e}")
        return None
