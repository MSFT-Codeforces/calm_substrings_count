
import os
import re
from typing import Tuple, Optional


def _normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def _parse_input(input_text: str) -> Tuple[Optional[int], Optional[str], Optional[str]]:
    """
    Single test case parser.
    Returns (n, s, err). If err is not None, parsing/validation failed.
    """
    txt = _normalize_newlines(input_text)

    # Parse by tokens (robust to extra blank lines), but still enforce the intended 2-item format.
    tokens = txt.split()
    if len(tokens) < 2:
        return None, None, "Input: expected 2 tokens (n and s)."
    if len(tokens) > 2:
        return None, None, f"Input: expected exactly 2 tokens (n and s), got {len(tokens)}."

    n_str, s = tokens[0], tokens[1]

    try:
        n = int(n_str)
    except ValueError:
        return None, None, f"Input: n is not an integer: {n_str!r}"

    if not (1 <= n <= 200000):
        return None, None, f"Input: n={n} out of range [1..200000]."

    if len(s) != n:
        return None, None, f"Input: string length is {len(s)}, expected n={n}."

    if re.fullmatch(r"[a-z]+", s) is None:
        return None, None, "Input: string contains characters outside [a-z]."

    return n, s, None


def _read_single_int_strict(output_text: str) -> Tuple[Optional[int], Optional[str]]:
    """
    Strictly reads exactly one integer from output_text.
    Allowed:
      - "123"
      - "123\n"
      - "-5"
      - "-5\n"
    Disallowed:
      - any leading/trailing spaces/tabs
      - extra newlines (more than one trailing '\n')
      - extra tokens
    Returns (value, err).
    """
    out = _normalize_newlines(output_text)

    if out == "":
        return None, "Output: empty output; expected one integer."

    # Allow at most one trailing newline.
    if out.endswith("\n"):
        core = out[:-1]
        if core.endswith("\n"):
            return None, "Output: more than one trailing newline; expected a single line."
    else:
        core = out

    if core == "":
        return None, "Output: missing integer before newline."

    # No other whitespace allowed anywhere in core.
    if any(ch.isspace() for ch in core):
        return None, "Output: unexpected whitespace; expected exactly one integer token."

    if re.fullmatch(r"-?\d+", core) is None:
        return None, f"Output: expected an integer, got {core!r}."

    try:
        return int(core), None
    except ValueError:
        # Should not happen given regex, but keep deterministic.
        return None, f"Output: failed to parse integer: {core!r}."


def check(input_text: str, output_text: str) -> Tuple[bool, str]:
    n, s, in_err = _parse_input(input_text)
    if in_err is not None:
        # Deterministic failure; input is expected valid in judge data.
        return False, in_err

    ans, out_err = _read_single_int_strict(output_text)
    if out_err is not None:
        return False, out_err

    # Range checks derivable without solving:
    # Calm substrings: cannot include length-1 substrings (always not calm),
    # so maximum calm substrings <= total substrings of length >= 2 = n(n-1)/2.
    max_possible = n * (n - 1) // 2

    if ans < 0:
        return False, f"Output: answer {ans} is negative; expected a nonnegative count."
    if ans > max_possible:
        return False, f"Output: answer {ans} exceeds maximum possible {max_possible} for n={n}."

    return True, "OK"


if __name__ == "__main__":
    in_path = os.environ.get("INPUT_PATH")
    out_path = os.environ.get("OUTPUT_PATH")
    if not in_path or not out_path:
        raise SystemExit("Environment variables INPUT_PATH and OUTPUT_PATH must be set.")
    with open(in_path, "r", encoding="utf-8") as f:
        inp = f.read()
    with open(out_path, "r", encoding="utf-8") as f:
        out = f.read()
    ok, _reason = check(inp, out)
    print("True" if ok else "False")
