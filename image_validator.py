import filetype

def is_valid_image(path):
    """
    Validate image using file path.
    Returns True if the file is a valid image.
    """
    kind = filetype.guess(path)
    return kind is not None and kind.mime.startswith("image/")

def is_valid_image_bytes(data):
    """
    Validate image using raw bytes (e.g., from Telegram media).
    Returns True if the bytes represent a valid image.
    """
    kind = filetype.guess(data)
    return kind is not None and kind.mime.startswith("image/")
