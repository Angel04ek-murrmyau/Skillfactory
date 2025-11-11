import json

with open("people.json", "r", encoding="utf-8") as f:
    people = json.load(f)
    # ФИО
    print(sorted(people, key=lambda s: s['ФИО']))
    # Возраст
    print(sorted(people, key=lambda s: s['возраст']))