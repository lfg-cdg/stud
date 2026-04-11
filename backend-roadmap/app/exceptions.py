class NotesApiException(Exception):
    "ловит все ошибки программы"

class ValidationError(NotesApiException):
    "невалидные входные данные"

class NotFoundError(ValidationError):
    "данные не найдены"