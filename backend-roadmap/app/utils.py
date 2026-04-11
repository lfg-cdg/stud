def normalize_title(title: str) -> str:
    return title.strip() 

def is_blank(value: str) -> bool:
    if not value.strip():
        return True
    
    return False