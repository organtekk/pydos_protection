"""DDoS Protection Module"""
from .server import start_protection_server
from .config import load_config

__version__ = "1.0.0"
__all__ = ['start_protection_server', 'load_config']