# Charm the Cartographers: Treasure Map Sprint

[![make.fun · u-ravendell-charm-the-cartographers-a-one-day-00854547](https://make.fun/badge/u-ravendell-charm-the-cartographers-a-one-day-00854547.svg)](https://make.fun/bounty/u-ravendell-charm-the-cartographers-a-one-day-00854547?utm_source=github&utm_medium=readme&utm_campaign=cartographers-treasure-map-01)
[![rank](https://make.fun/badge/u-ravendell-charm-the-cartographers-a-one-day-00854547/Ipan8/cartographers-treasure-map-01/rank.svg)](https://make.fun/bounty/u-ravendell-charm-the-cartographers-a-one-day-00854547/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=cartographers-treasure-map-01)
[![reward](https://make.fun/badge/u-ravendell-charm-the-cartographers-a-one-day-00854547/Ipan8/cartographers-treasure-map-01/reward.svg)](https://make.fun/bounty/u-ravendell-charm-the-cartographers-a-one-day-00854547?utm_source=github&utm_medium=readme&utm_campaign=cartographers-treasure-map-01)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A treasure map of a fictional island, "Isla del Croako", drawn in a hand-inked
antique-chart style: a dashed red route winds from Lily Pad Lagoon, past
Mount Croak and Frog Hollow, down to Shipwreck Cove and the treasure chest
marked X Marks the Spot, with The Singing Reeds along the eastern shore.
Six place names are written on the map and legible at a glance, plus a
compass rose, sea monsters, and a cartouche dated "Year of the Frog 1743".

## What it does

`main.py` (Python 3, standard library only) reads the map image from
`entry.b64` and writes it to `/output/entry.png`:

- `entry.b64` — the map PNG, base64-encoded (one line). The repository
  stores it encoded because the submission channel carries text only;
  `main.py` decodes it back to the real PNG, byte for byte.
- The output PNG is 1024x683 pixels, 581,072 bytes — inside the gate
  (PNG or JPEG, at most 1 MiB and 1024x1024 pixels).

## Run it

```sh
python3 main.py
# writes /output/entry.png
```
