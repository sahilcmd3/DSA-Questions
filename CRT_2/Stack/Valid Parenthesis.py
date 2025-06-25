# LEETCODE 20


def isValid(s):
    st = []
    mapp = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapp.values():
            st.append(char)
        elif char in mapp.keys():
            if not st or mapp[char] != st.pop():
                return False

    return not st


if __name__ == "__main__":
    print(isValid(s="()[]{}"))
