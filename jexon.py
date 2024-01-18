import json

def jexon(text):
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
                    yield json_object  # Yield the JSON object instead of appending to a list
                except json.JSONDecodeError:
                    pass
                start_pos = None

# Example usage
raw_result = "Some text before JSON {\"key\": \"value\"} and some after."
for json_object in jexon(raw_result):
    print(json_object)
