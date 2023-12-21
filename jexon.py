import json
import re

def jexon(text):
    valid_jsons = []
    start_pos = None
    braces_count = 0
    
    for i, char in enumerate(text):
        if char == '{':
            if start_pos is None:
                start_pos = i
            braces_count += 1
        elif char == '}':
            braces_count -= 1
            if braces_count == 0 and start_pos is not None:
                potential_json = text[start_pos:i+1]
                try:
                    json_object = json.loads(potential_json)
                    valid_jsons.append(json_object)
                except json.JSONDecodeError:
                    pass
                start_pos = None
    
    return valid_jsons

# Test with your text
json_objects = jexon(raw_result)
print(json_objects)
