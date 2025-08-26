def extract_media(messages):
    paths = []
    for msg in messages:
        if msg.media:
            path = client.download_media(msg, file="downloads/")
            paths.append(path)
    return paths
