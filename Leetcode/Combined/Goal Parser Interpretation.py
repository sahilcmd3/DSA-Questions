# LEETCODE 1678

"""You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)"
in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al".
The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command."""


def interpret(command):
    dict_map = {"G": "G", "()": "o", "(al)": "al"}
    res = ""
    i = 0

    while i < len(command):
        if command[i] == "G":
            res += dict_map["G"]
            i += 1
        elif command[i : i + 2] == "()":
            res += dict_map["()"]
            i += 2
        elif command[i : i + 4] == "(al)":
            res += dict_map["(al)"]
            i += 4
    return res


if __name__ == "__main__":
    print(interpret(command="G()()()()(al)"))
