import requests

def post_webhook(url, payload):
    requests.post(url, json=payload, timeout=3)
