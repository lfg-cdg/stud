from dataclasses import dataclass


@dataclass
class AppConfig(slots=True):
    app_name: str
    debug: bool
    version: str

