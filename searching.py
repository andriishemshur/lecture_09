import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    if field not in set(data.keys()):
        return None
    return data[field]

def linear_search(sequence, number):
    searched_res = {"positions": [], "count": 0 }
    for idx, value in enumerate(sequence):
        if value == number:
            searched_res["positions"].append(idx)
            searched_res["count"] += 1
    return searched_res

def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    results = linear_search(sequential_data, 0)
    print(results)

if __name__ == '__main__':
    main()