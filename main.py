import json
from typing import List, Dict

def path_to_file_list(path: str) -> List[str]:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[Dict[str, str]]:
    return [{"English": e.strip(), "German": g.strip()} for e, g in zip(english_file_list, german_file_list)]

def write_file_list(file_list: List[Dict[str, str]], path: str) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(file_list, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    english_path = './english.txt'
    german_path = './german.txt'
    output_path = './concated.json'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)
    write_file_list(processed_file_list, output_path)
