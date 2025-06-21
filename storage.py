import json
import os
from pathlib import Path

DATA_FILE = Path('contacts.json')


def load_contacts():
    """Load contacts from JSON file"""
    try:
        if DATA_FILE.exists():
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        return []
    except (json.JSONDecodeError, IOError) as e:
        print(
            f"Warning: Could not load contacts file ({e}). Starting with empty contact book.")
        return []


def save_contacts(contacts):
    """Save contacts to JSON file"""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(contacts, f, indent=2)
    except IOError as e:
        print(f"Error: Could not save contacts to file ({e})")
