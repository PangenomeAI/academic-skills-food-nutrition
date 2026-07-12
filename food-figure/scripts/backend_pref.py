#!/usr/bin/env python3
"""Store the user's Python-vs-R plotting backend preference for food-figure.

Usage:
  python backend_pref.py get           # print 'python' or 'r'; exit 1 if unset
  python backend_pref.py set python     # or: set r
  python backend_pref.py clear
  python backend_pref.py path           # print the config file location
  python backend_pref.py --selftest

Config: JSON at ~/.config/food-nutrition-skills/food-figure.json
(override with the FOOD_FIGURE_CONFIG env var).
"""
import json
import os
import sys

VALID = ("python", "r")


def config_path():
    override = os.environ.get("FOOD_FIGURE_CONFIG")
    if override:
        return override
    base = os.environ.get("XDG_CONFIG_HOME") or os.path.join(os.path.expanduser("~"), ".config")
    return os.path.join(base, "food-nutrition-skills", "food-figure.json")


def read_config(path):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (FileNotFoundError, ValueError):
        return {}


def write_config(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def get_backend(path):
    return read_config(path).get("backend")


def set_backend(path, backend):
    if backend not in VALID:
        raise SystemExit(f"backend must be one of {VALID}")
    data = read_config(path)
    data["backend"] = backend
    write_config(path, data)
    return backend


def clear_backend(path):
    data = read_config(path)
    data.pop("backend", None)
    write_config(path, data)


def selftest():
    import tempfile
    tmp = os.path.join(tempfile.mkdtemp(), "cfg.json")
    assert get_backend(tmp) is None
    assert set_backend(tmp, "r") == "r"
    assert get_backend(tmp) == "r"
    set_backend(tmp, "python")
    assert get_backend(tmp) == "python"
    clear_backend(tmp)
    assert get_backend(tmp) is None
    try:
        set_backend(tmp, "julia")
    except SystemExit:
        pass
    else:
        raise AssertionError("invalid backend should raise")
    print("OK: backend_pref selftest passed")


def main(argv):
    if len(argv) == 2 and argv[1] == "--selftest":
        selftest()
        return 0
    path = config_path()
    if len(argv) == 2 and argv[1] == "get":
        b = get_backend(path)
        if not b:
            return 1
        print(b)
        return 0
    if len(argv) == 3 and argv[1] == "set":
        print(set_backend(path, argv[2]))
        return 0
    if len(argv) == 2 and argv[1] == "clear":
        clear_backend(path)
        return 0
    if len(argv) == 2 and argv[1] == "path":
        print(path)
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
