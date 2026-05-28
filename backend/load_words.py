import json
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import SessionLocal
from models import Word

db = SessionLocal()

with open('words_data.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

for item in words:
    exists = db.query(Word).filter(Word.word == item["word"]).first()
    if not exists:
        word = Word(word=item["word"], level=item["level"])
        db.add(word)

db.commit()
print("Words loaded successfully.")
