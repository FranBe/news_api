import configparser
from pathlib import Path
import os

class Config:

    def __init__(self):
        self.project_root = Path(__file__).resolve().parent.parent.parent

        self.config_file = self.project_root / "config" / "config.ini"

        self.parser = configparser.ConfigParser()
        self.parser.read(self.config_file)

    # General
    @property
    def debug(self):
        return self.parser.get("general", "debug")

    @property
    def log_path(self):
        return self.parser.getint("general", "log_path")

    @property
    def log_level(self):
        return self.parser.get("general", "log_level")

    # Email
    @property
    def smtp_server(self):
        return self.parser.get("email", "smtp_server")

    @property
    def smtp_port(self):
        return self.parser.getint("email", "smtp_port")

    @property
    def subject(self):
        return self.parser.get("email", "subject")

    # News API
    @property
    def base_url(self):
        return self.parser.get("news_api", "base_url")
