from config import MEETSTREAM_API_KEY  # oops: the key is committed right next to the code


def client_headers() -> dict:
    return {"Authorization": f"Bearer {MEETSTREAM_API_KEY}"}
