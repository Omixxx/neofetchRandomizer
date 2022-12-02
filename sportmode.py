#!/usr/bin/env python
import json
import os
import sys
import subprocess
import random
from shutil import which


def get_random_element_in_a_list(list):
    return list[random.randint(0, len(list) - 1)]


def get_random_classic_logo(data) -> str:
    logos = []
    for logo in data['logos']:
        logos.append(logo)
    return get_random_element_in_a_list(logos)


def get_random_minimal_logo(data) -> str:
    logos = []
    for logo in data['small_logos']:
        logos.append(logo)
    return get_random_element_in_a_list(logos)


def main(logos, mode):
    if mode == '1' or mode.lower() == 'classic':
        opt = get_random_classic_logo(logos)
    elif mode == '2' or mode.lower() == 'minimal':
        opt = get_random_minimal_logo(logos)
        opt = f"{opt}_small"
    else:
        print("Invalid mode")
        print()
        sys.exit(1)

    subprocess.run(["neofetch", "--ascii_distro", opt])


if __name__ == "__main__":
    assert which("neofetch") is not None, "Neofetch is not installed"
    
    file_path = os.path.realpath(os.path.dirname(__file__)) 
    with open(file_path + "/logos.json") as f:
        logos = json.load(f)

    if len(sys.argv) < 2:
        print("Usage: python3 sportmode.py [classic | minimal]")
        sys.exit(1)

    mode = sys.argv[1]

    main(logos, mode)
