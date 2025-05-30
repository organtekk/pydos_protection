import os
import json

DEFAULT_CONFIG = {
    "protected_ip": "0.0.0.0",
    "max_connections_per_ip": 10,
    "connection_timeout": 30,
    "default_port": 8080,
    "backlog": 100,
    "blacklist_file": os.path.join("blocked", "blacklisted.txt"),
    "log_file": "connections.log",
    "debug": False
}

def load_config(config_path="pylimit_config.json"):
    """Load or create configuration file"""
    try:
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = json.load(f)
                if all(key in config for key in DEFAULT_CONFIG):
                    return config
        
        # Create new config if missing or invalid
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, 'w') as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        return DEFAULT_CONFIG
        
    except Exception as e:
        print(f"Config error: {e}, using defaults")
        return DEFAULT_CONFIG