# LEETCODE (medium)

"""You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. 
Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. 
For example, '...' and '....' are valid directory or file names.

The simplified canonical path should follow these rules:
The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.

Example 1:

Input: path = "/home/"

Output: "/home"

Explanation:

The trailing slash should be removed."""


# Time Complexity: O(n)
def simplifyPath(path):
    components=path.split('/')  # Splitting the path using "/" separating "." and ".."
    st=[]  # stack (Pushing into stack = moving further into directory & Poping means the reverse)

    for i in components:
        if i=="" or i == ".":  # "." are ignored
            continue
        elif i=="..":
            if st:
                st.pop()
        else:
            st.append(i)
    
    return "/"+"/".join(st)

print(simplifyPath(path = "/.../a/../b/c/../d/./"))


"""
Example Walkthrough:
    Example path:
    path = "/home/../usr//bin/./script"
    
    Initialization:
    components = ["", "home", "..", "usr", "", "bin", ".", "script"]
    st = []

    Processing Components:
    "": Skip.
    "home": Push to stack: st = ["home"].
    "..": Pop from stack: st = [].
    "usr": Push to stack: st = ["usr"].
    "": Skip.
    "bin": Push to stack: st = ["usr", "bin"].
    ".": Skip.
    "script": Push to stack: st = ["usr", "bin", "script"].

    Final Result:
    "/usr/bin/script"
"""