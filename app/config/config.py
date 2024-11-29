import json

def init_config() -> dict:
    try:
        with open('app/config/config.json') as config_file:
            config: dict = json.load(config_file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Config file not found. {e}")
    return config
