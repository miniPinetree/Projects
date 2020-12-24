wizards = [
    {'name': '해리', 'age': 40},
    {'name': '허마이오니', 'age': 40},
    {'name': '론', 'age': 41},
]

professor_wizards = [
    {'name': '덤블도어', 'age': 116},
    {'name': '맥고나걸', 'age': 85},
    {'name': '스네이프', 'age': 60},
]

def get_age(name, wizards):
    for wizard in wizards:
        if wizard["name"] == name:
            return wizard["age"]
    return "해당하는 이름이 없습니다"

print(get_age('맥고나걸', professor_wizards))