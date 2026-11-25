"""Write one dad joke to /output/entry.txt.

The joke is a single dad joke of at most 200 characters, told in the
classic question-and-answer shape a father would deliver across the
dinner table: the setup asks why, and the punchline lands on a pun
at the very end. Stdlib only, no network, deterministic: the same
bytes on every run.
"""

import os

JOKE = "Why did the dad unplug the router at dinner? He wanted the whole family to reconnect."
# The joke is 85 characters, comfortably inside the 1-200 gate.

assert 1 <= len(JOKE) <= 200, "dad joke must be 1-200 characters"
assert JOKE.strip(), "dad joke must not be only white space"



def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
