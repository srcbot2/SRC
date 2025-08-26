import os
import sys

# ⚠️ Hardcoded for local testing — remove in production
os.environ["API_ID"] = "21240850"
os.environ["API_HASH"] = "593eec13b2638de5e9bb4284ea8631ec"
os.environ["BOT_TOKEN"] = "8296889818:AAG7lfuJU-ewxjDLH7O4wmW92B5K4CxSM4w"
os.environ["OWNER_ID"] = "6662470778"
os.environ["TARGET_CHAT_IDS"] = "-1003014498688,-1002944027661"

REQUIRED_KEYS = [
    "API_ID",
    "API_HASH",
    "BOT_TOKEN",
    "OWNER_ID",
    "TARGET_CHAT_IDS"
]

def validate_env():
    errors = []
    for key in REQUIRED_KEYS:
        value = os.getenv(key)
        if not value:
            errors.append(f"❌ Missing: {key}")
        elif key == "BOT_TOKEN" and ":" not in value:
            errors.append(f"⚠️ BOT_TOKEN format invalid: {value}")
        elif key == "TARGET_CHAT_IDS":
            ids = value.split(",")
            for chat_id in ids:
                if not chat_id.strip().startswith("-100"):
                    errors.append(f"⚠️ Invalid TARGET_CHAT_ID: {chat_id.strip()}")

    if errors:
        print("\n🔍 ENV Validation Failed:")
        for err in errors:
            print(err)
        sys.exit("🛑 Fix .env before launching bot.")
    else:
        print("✅ All required ENV variables are present and valid.")

if __name__ == "__main__":
    validate_env()
