import re


def validate_name(name):
    """Validate contact name (letters and spaces only)"""
    return bool(re.fullmatch(r'^[a-zA-Z\s]+$', name)) if name else False


def validate_phone(phone):
    """Validate phone number (digits only, 10-15 characters)"""
    return phone.isdigit() and 10 <= len(phone) <= 15


def validate_email(email):
    """Basic email validation"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email)) if email else False
