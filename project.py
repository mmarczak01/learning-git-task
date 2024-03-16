shopping_list = {
    "piekarnia" : ["chleb", "pączek", "bułki"],
    "warzywniak" : ["marchew", "seler", "rukola"]
} 

i = 0

print("Lista zakupów")
for (keys, values) in shopping_list.items():
    for value in values:
        values = values + [value.capitalize()]
        values.remove(value)
        i = i + 1
    print(f"Idę do {keys.capitalize()}, kupuję tu następujące rzeczy: {values}")
print(f"W sumie kupuję {i} produktów.")