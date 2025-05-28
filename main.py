import json
from typing import List, Dict

def path_to_file_list(path: str) -> List[str]:
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[Dict[str, str]]:
    """Converts two lists of file paths into a list of JSON-serializable dictionaries"""
    return [{"English": e.strip(), "German": g.strip()} for e, g in zip(english_file_list, german_file_list)]

def write_file_list(json_obj: List[Dict[str, str]], path: str) -> None:
    """Writes a list of dictionaries to a JSON file"""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(json_obj, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    english_path = './english.txt'
    german_path = './german.txt'
    output_path = './concated.json'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_json_list = train_file_list_to_json(english_file_list, german_file_list)
    write_file_list(processed_json_list, output_path)
