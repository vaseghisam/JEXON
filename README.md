# JEXON: JSON Object Extractor
JEXON: A Python utility for extracting and parsing JSON objects from mixed text content.

## Overview
JEXON is a Python utility designed to efficiently extract and parse JSON objects from strings containing mixed text and JSON content. This tool is ideal for processing logs, unstructured data, or text streams where JSON objects are embedded within other textual data.

## Features
- Robust JSON extraction from mixed text formats.
- Handles nested and multiple JSON objects within a single text.
- Lightweight with no external dependencies.

## Installation
No installation is required. Simply download the `jexon.py` file and include it in your Python project.

## Usage
To use JEXON in your Python script, import the function and pass a string containing JSON objects.

```python
from jexon import jexon

text_with_jsons = '{"name": "John", "age": 30} Some text here {"item": "apple", "quantity": 5}'
json_objects = jexon(text_with_jsons)
print(json_objects)
```

## Dependencies
```python
import json
```

## How It Works

JEXON iterates over the provided text, identifies the structure of JSON objects, and extracts them. It uses Python's built-in json library to parse and validate JSON content.

## Contributing

Contributions to JEXON are welcome! If you have suggestions for improvements or encounter any issues, please feel free to open an issue or submit a pull request.

License

MIT License

## Contact

For any additional questions or comments, please feel free to contact the author.
