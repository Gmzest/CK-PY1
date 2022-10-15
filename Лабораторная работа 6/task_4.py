import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    ...  # TODO реализовать конвертер из csv в json
    with open("output.csv", 'r') as f:
        head_lst = f.readline()[:-1].split(",")
        rows_lst = [line[:-1].split(",") for line in f.readlines()]
        return [dict(zip(head_lst, line)) for line in rows_lst]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
