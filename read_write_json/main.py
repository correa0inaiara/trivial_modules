__all__ = ['read_json', 'write_json']

import json

def read_json(filename: str = 'input'):
  with open(filename + ".json", "r", encoding='utf-8') as input_file:
    input_file.read(filename)

def escrever_json(data: dict, filename: str = 'output'):
  json_obj = json.dumps(data, indent=4, ensure_ascii=False)
  with open(filename + ".json", "w", encoding='utf-8') as output_file:
    output_file.write(json_obj)