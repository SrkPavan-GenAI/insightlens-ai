import json

from src.config import MAX_HISTORY
from datetime import datetime

HISTORY_FILE = "data/history.json"


def load_history():

    try:

        with open(
            HISTORY_FILE,
            "r"
        ) as file:

            return json.load(file)

    except:

        return []


def save_history(record):

    history = load_history()

    record["timestamp"] = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

    history.insert(
        0,
        record
    )

    history = history[:MAX_HISTORY]

    with open(
        HISTORY_FILE,
        "w"
    ) as file:

        json.dump(
            history,
            file,
            indent=4
        )