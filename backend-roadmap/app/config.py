from dataclasses import dataclass


@dataclass(slots=True)
class AppConfig:
    app_name: str = "notes-api"
    debug: bool = True
    version: str = "0.1.0"
