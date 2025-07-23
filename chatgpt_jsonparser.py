# this is to print all the lines which contains the word 
import json 
with open("chat_export.json","r") as reader:
    buffer=json.load(reader)
    for var in buffer:
        if "dsa" in var["title"].lower():
            print(f"{var['title']}")

# to read the null moderations 
print("########")
for mods in buffer:
    if mods['moderation_results']:
        print(f"{mods['moderation_results']} on title: {mods['title']}")

print("########")
for msg in buffer:
    for nest1 in msg['mapping'].values():
        message = nest1.get("message")
        if (
            message and
            "content" in message and
            "parts" in message["content"] and 
            any(
                isinstance(part, str) and "sharvari" in part.lower()
                for part in message["content"]["parts"]
            )
        ):
            print(message["content"]["parts"])
            print('/n')

