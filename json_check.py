import json

fields = ("timestamp", "referer", "location", "remoteHost", "partyId", "sessionId", "pageViewId", "eventType", "item_id", "item_price", "item_url", "basket_price", "detectedDuplicate", "detectedCorruption", "firstInSession", "userAgentName")
schema = {
    "timestamp": 'int',
    "referer": 'string (url)',
    "location": 'string (url)',
    "remoteHost": 'string',
    "partyId": 'string',
    "sessionId": 'string',
    "pageViewId": 'string',
    "eventType": ['string (itemBuyEvent)', 'string (itemViewEvent)'],
    "item_id": 'string',
    "item_price": "int",
    "item_url": "string (url)",
    "basket_price": "string",
    "detectedDuplicate": "bool",
    "detectedCurruption": "bool",
    "firstInSession": "bool",
    "userAgentName": "string",
}

with open("shop.json") as f:
    data = json.load(f)
    for obj in data:
        for field in obj:
            if field not in fields:
                print(f"Поле {field} лишнее")
            for true_field in fields:
                if true_field not in obj:
                    print(f"Не хватает поля {true_field}")
                else:
                    print(f"Поле {true_field} найдено")



            if field in schema:
                value = obj[field]
                expected = schema[field]
                if expected == "int" and not isinstance(value, int):
                    print(f"Ошибка: поле {field} должно быть int, а не {type(value)}")
                elif expected == "bool" and not isinstance(value, bool):
                    print(f"Ошибка: поле {field} должно быть bool, а не {type(value)}")
                elif expected == "string" and not isinstance(value, str):
                    print(f"Ошибка: поле {field} должно быть строкой")
                elif '(url)' in expected and not (value.startswith("http://") or value.startswith("https://")):
                    print(f"Ошибка: поле {field} должно быть URL, а не '{value}'")
                elif 'itemBuyEvent' in expected or 'itemViewEvent' in expected:
                    if value not in ['itemBuyEvent', 'itemViewEvent']:
                        print(f"Ошибка: поле {field} должно быть 'itemBuyEvent' или 'itemViewEvent'")
                else:
                    print(f"Другая ошибка. JSON не содержит поля {field}")



