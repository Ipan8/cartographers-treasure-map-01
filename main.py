#!/usr/bin/env python3
"""Charm the Cartographers: Treasure Map Sprint — entry program.

Writes the treasure map image to /output/entry.png.

The map (a hand-drawn fictional island, "Isla del Croako", with 6 legible
labels: Lily Pad Lagoon, Mount Croak, The Singing Reeds, Frog Hollow,
Shipwreck Cove, X Marks the Spot) is stored base64-encoded in entry.b64
(the submission channel carries text only). This program decodes it back
to the real PNG, byte for byte.
"""

import base64
import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    b64_path = os.path.join(here, "entry.b64")
    if not os.path.exists(b64_path):
        # Fall back to the working directory.
        b64_path = os.path.join(os.getcwd(), "entry.b64")
    with open(b64_path, "r", encoding="ascii") as f:
        raw = f.read().strip()
    data = base64.b64decode(raw)
    os.makedirs("/output", exist_ok=True)
    out_path = "/output/entry.png"
    with open(out_path, "wb") as f:
        f.write(data)
    print("wrote %d bytes to %s" % (len(data), out_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
