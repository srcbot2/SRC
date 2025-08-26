from image_validator import is_valid_image, is_valid_image_bytes

def test_image_path(path):
    if is_valid_image(path):
        print(f"✅ '{path}' is a valid image file.")
    else:
        print(f"❌ '{path}' is NOT a valid image file.")

def test_image_bytes(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        if is_valid_image_bytes(data):
            print(f"✅ Bytes from '{path}' represent a valid image.")
        else:
            print(f"❌ Bytes from '{path}' do NOT represent a valid image.")
    except Exception as e:
        print(f"⚠️ Error reading file '{path}': {e}")

if __name__ == "__main__":
    test_image_path("sample.jpg")
    test_image_bytes("sample.jpg")
