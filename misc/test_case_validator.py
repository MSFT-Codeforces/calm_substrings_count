
import sys
import re

MAX_N = 2 * 10**5

int_re = re.compile(r"^[0-9]+$")
str_re = re.compile(r"^[a-z]+$")

def valid_case(n_line: str, s_line: str) -> bool:
    # Strict format: no leading/trailing spaces, no extra tokens
    if not int_re.fullmatch(n_line):
        return False
    try:
        n = int(n_line)
    except:
        return False
    if not (1 <= n <= MAX_N):
        return False

    if not str_re.fullmatch(s_line):
        return False
    if len(s_line) != n:
        return False
    return True

def validate_lines_as_pairs(lines) -> bool:
    if len(lines) == 0 or (len(lines) % 2) != 0:
        return False
    for i in range(0, len(lines), 2):
        if not valid_case(lines[i], lines[i + 1]):
            return False
    return True

def validate_lines_with_T(lines) -> bool:
    if len(lines) < 3:
        return False
    if not int_re.fullmatch(lines[0]):
        return False
    try:
        t = int(lines[0])
    except:
        return False
    if t < 1:
        return False
    if len(lines) != 1 + 2 * t:
        return False
    idx = 1
    for _ in range(t):
        if not valid_case(lines[idx], lines[idx + 1]):
            return False
        idx += 2
    return True

def main():
    data = sys.stdin.read()
    if data == "":
        print("False")
        return

    # splitlines() drops trailing empty line caused by final '\n', but preserves
    # empty lines in the middle as '' entries (which we want to reject).
    lines = data.splitlines()

    # Reject any empty line (strict format)
    if any(line == "" for line in lines):
        print("False")
        return

    ok = False

    # Prefer T-mode if it fits exactly; otherwise pairs-mode.
    if validate_lines_with_T(lines):
        ok = True
    elif validate_lines_as_pairs(lines):
        ok = True

    print("True" if ok else "False")

if __name__ == "__main__":
    main()
