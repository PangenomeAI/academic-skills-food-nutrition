#!/usr/bin/env python3
"""Offline self-test for institution profiles and food-fetch setup config.

This script uses only local files and the Python standard library. It never starts
a browser and never sends a network request.

Usage:
  python3 scripts/check_institution_profiles.py --selftest
"""
import importlib.util
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent.parent
PROFILES_PATH = ROOT / "food-fetch" / "references" / "institution-profiles.md"
SETUP_PATH = ROOT / "scripts" / "food_fetch_setup.py"
REQUIRED_FIELDS = {
    "id",
    "name",
    "library_home",
    "library_search",
    "openurl_base",
    "authentication",
}
URL_FIELDS = ("library_home", "library_search", "openurl_base")
FORBIDDEN_KEY_PARTS = (
    "password",
    "passwd",
    "cookie",
    "token",
    "session",
    "secret",
    "credential",
    "login_url",
    "otp",
)


def parse_profiles(path):
    """Parse the deliberately small YAML-shaped block without a YAML dependency."""
    profiles = []
    current = None
    for line in path.read_text(encoding="utf-8").splitlines():
        start = re.match(r"^\s*-\s+id:\s*(\S.*?)\s*$", line)
        if start:
            current = {"id": start.group(1)}
            profiles.append(current)
            continue
        field = re.match(r"^\s{4}([a-z_]+):\s*(\S.*?)\s*$", line)
        if current is not None and field:
            current[field.group(1)] = field.group(2)
    return profiles


def load_setup_module():
    spec = importlib.util.spec_from_file_location("food_fetch_setup", SETUP_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def assert_no_sensitive_keys(value):
    if isinstance(value, dict):
        for key, item in value.items():
            lowered = str(key).lower()
            assert not any(part in lowered for part in FORBIDDEN_KEY_PARTS), key
            assert_no_sensitive_keys(item)
    elif isinstance(value, list):
        for item in value:
            assert_no_sensitive_keys(item)


def selftest():
    profiles = parse_profiles(PROFILES_PATH)
    assert profiles, "no institution profiles found"
    assert len(profiles) == 1, "institution-profiles.md must contain exactly one entry"

    ids = [profile.get("id") for profile in profiles]
    assert len(ids) == len(set(ids)), "institution ids must be unique"

    unimelb = next((profile for profile in profiles if profile.get("id") == "unimelb"), None)
    assert unimelb is not None, "unimelb profile is missing"
    assert REQUIRED_FIELDS <= set(unimelb), "unimelb profile has missing fields"
    assert unimelb == {
        "id": "unimelb",
        "name": "University of Melbourne",
        "library_home": "https://library.unimelb.edu.au/",
        "library_search": "https://librarysearch.unimelb.edu.au/",
        "openurl_base": "https://unimelb.hosted.exlibrisgroup.com/sfxlcl41",
        "authentication": "OpenAthens / University SSO",
    }
    for field in URL_FIELDS:
        parsed = urlparse(unimelb[field])
        assert parsed.scheme == "https" and parsed.netloc, f"{field} must be HTTPS"

    setup = load_setup_module()
    previous = os.environ.get("FOOD_FETCH_CONFIG_DIR")
    try:
        with tempfile.TemporaryDirectory() as tmp:
            os.environ["FOOD_FETCH_CONFIG_DIR"] = tmp
            path = Path(setup.config_path())

            new_cfg = setup.set_config("institutional")
            assert new_cfg["institution"] == "unimelb"
            assert setup.is_configured(setup.load())
            raw_new = json.loads(path.read_text(encoding="utf-8"))
            assert raw_new["institution"] == "unimelb"
            assert_no_sensitive_keys(raw_new)
            assert_no_sensitive_keys({key: None for key in setup.ALLOWED_KEYS})

            path.write_text(
                json.dumps({"configured": True, "mode": "institutional"}),
                encoding="utf-8",
            )
            old_cfg = setup.load()
            assert setup.is_configured(old_cfg)
            assert old_cfg["institution"] == "unimelb"
            assert_no_sensitive_keys(json.loads(path.read_text(encoding="utf-8")))
    finally:
        if previous is None:
            os.environ.pop("FOOD_FETCH_CONFIG_DIR", None)
        else:
            os.environ["FOOD_FETCH_CONFIG_DIR"] = previous

    print("OK: institution profiles and food-fetch setup selftest passed")


def main(argv):
    if "--selftest" not in argv:
        print(__doc__)
        return 2
    selftest()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
