from pathlib import Path

from src.markdown_utils import format_data_as_markdown

OUTPUT_FOLDER = 'docs'


def write_lines_to_disk(lines, fname):
    with Path(fname).open('w', encoding='utf8') as f:
        for line in lines:
            f.write(f"{line}\n")


def write_data_to_disk(data, fname):
    lines = format_data_as_markdown(data)
    write_lines_to_disk(lines, fname)


def deal_with_none(v, min_value=0):
    # Reference: https://stackoverflow.com/a/12971697/376454
    if not v:
        return min_value
    return v


def write_markdown_files(data):
    sorted_data = dict(sorted(data.items(), key=lambda x: x[1]["slug"]))
    write_data_to_disk(sorted_data, f"{OUTPUT_FOLDER}/by_game_slug.md")

    sorted_data = dict(
        sorted(
            data.items(),
            key=lambda x: deal_with_none(x[1]["averageRating"]),
            reverse=True,
        ),
    )
    write_data_to_disk(sorted_data, f"{OUTPUT_FOLDER}/by_average_rating.md")

    sorted_data = dict(
        sorted(
            data.items(),
            key=lambda x: deal_with_none(x[1]["ratingCount"]),
            reverse=True,
        ),
    )
    write_data_to_disk(sorted_data, f"{OUTPUT_FOLDER}/by_num_raters.md")

    sorted_data = dict(
        sorted(data.items(), key=lambda x: x[1]["numProgressed"], reverse=True),
    )
    write_data_to_disk(sorted_data, f"{OUTPUT_FOLDER}/by_num_players.md")

    sorted_data = dict(
        sorted(data.items(), key=lambda x: x[1]["numCompleted"], reverse=True),
    )
    write_data_to_disk(sorted_data, f"{OUTPUT_FOLDER}/by_num_platinum_trophies.md")

    sorted_data = dict(
        sorted(data.items(), key=lambda x: x[1]["maxRarity"], reverse=True),
    )
    write_data_to_disk(sorted_data, f"{OUTPUT_FOLDER}/by_max_rarity.md")
