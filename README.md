# Epic Games Tracker

This repository contains Python code to track the numbers of players and ratings on the Epic Games store (EGS).

![Illustration cover][img-cover]

## Disclaimer

> [!Note]
> As of January 22, 2025, the leak is plugged: `numProgressed` and `numCompleted` cannot be directly fetched from Epic Games anymore.

## Requirements

-   Install the latest version of [Python 3.X][python-download-url].
-   Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run every day:
```bash
python fetch_mappings_for_today.py
```
```bash
python fetch_data_for_today.py
```

Alternatively:

-   either run every day [`epic_games_tracker.ipynb`][colab-notebook]
[![Open In Colab][colab-badge]][colab-notebook]

-   or schedule `update.sh` for daily runs.

To have a retrospective look at days on which some achievements were fixed, run:
```bash
python list_all_fixed_trophies.py
```

## Results

Visit [the website][tracker-website].

## References

- [`nikop/epic-games-ratings`][madjoki-egs-ratings]
- [`woctezuma/epic-games-ratings`][epic-games-ratings]
- [`woctezuma/epic-games-achievements`][epic-games-achievements]
- [`woctezuma/epic-games-player-estimates`][epic-games-player-estimates]

<!-- Definitions -->

[img-cover]: <https://github.com/woctezuma/epic-games-tracker/wiki/img/cover.png>
[python-download-url]: <https://www.python.org/downloads/>
[colab-notebook]: <https://colab.research.google.com/github/woctezuma/epic-games-tracker/blob/colab/epic_games_tracker.ipynb>
[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>
[tracker-website]: <https://woctezuma.github.io/epic-games-tracker/>
[madjoki-egs-ratings]: <https://github.com/nikop/epic-games-ratings>
[epic-games-ratings]: <https://github.com/woctezuma/epic-games-ratings>
[epic-games-achievements]: <https://github.com/woctezuma/epic-games-achievements>
[epic-games-player-estimates]: <https://github.com/woctezuma/epic-games-player-estimates>
