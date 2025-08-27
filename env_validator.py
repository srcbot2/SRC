import sys
import logging

# Setup logging
LOG_PATH = "logs/error.log"
logging.basicConfig(filename=LOG_PATH, level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

# 🔧 Hardcoded values for testing
ENV_VARS = {
    "API_ID": "21240850",
    "API_HASH": "593eec13b2638de5e9bb4284ea8631ec",
    "BOT_TOKEN": "8296889818:AAG7lfuJU-ewxjDLH7O4wmW92B5K4CxSM4w",
    "OWNER_ID": "6662470778",
    "TARGET_CHAT_IDS": "-1002944027661,-1002944027661"
}

def validate_env():
    errors = []

    # Presence check
    for key, value in ENV_VARS.items():
        if not value or value.strip() == "":
            errors.append(f"[ENV_CHECK] Missing: {key}")

    # Format checks
    try:
        int(ENV_VARS["API_ID"])
    except:
        errors.append("[ENV_CHECK] API_ID must be an integer")

    if len(ENV_VARS["API_HASH"]) < 32:
        errors.append("[ENV_CHECK] API_HASH looks too short")

    if ENV_VARS["BOT_TOKEN"].count(":") != 1:
        errors.append("[ENV_CHECK] BOT_TOKEN format invalid")

    if not ENV_VARS["OWNER_ID"].isdigit():
        errors.append("[ENV_CHECK] OWNER_ID must be numeric")

    # Chat ID checks
    chat_ids = [cid.strip() for cid in ENV_VARS["TARGET_CHAT_IDS"].split(",") if cid.strip()]
    if len(set(chat_ids)) != len(chat_ids):
        errors.append("[ENV_CHECK] Duplicate chat IDs in TARGET_CHAT_IDS")
    for cid in chat_ids:
        if not cid.startswith("-100") or not cid[4:].isdigit():
            errors.append(f"[ENV_CHECK] Invalid chat ID format: {cid}")

    # Final verdict
    if errors:
        for err in errors:
            logging.error(err)
            print(err)
        sys.exit(1)
    else:
        print("[ENV_CHECK] All hardcoded environment variables are valid.")

if __name__ == "__main__":
    validate_env()
