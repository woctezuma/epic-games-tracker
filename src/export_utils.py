from src.markdown_utils import format_data_as_markdown


def write_lines_to_disk(lines, fname):
    with open(fname, 'w', encoding='utf8') as f:
        for line in lines:
            f.write(f"{line}\n")
    return


def write_data_to_disk(data, fname):
    lines = format_data_as_markdown(data)
    write_lines_to_disk(lines, fname)
    return


def write_markdown_files(data):
    sorted_data = sorted(data.items(), key=lambda x: x[1]["slug"])
    write_data_to_disk(sorted_data, "by_game_slug.md")

    sorted_data = sorted(data.items(), key=lambda x: x[1]["averageRating"], reverse=True)
    write_data_to_disk(sorted_data, "by_average_rating.md")

    sorted_data = sorted(data.items(), key=lambda x: x[1]["ratingCount"], reverse=True)
    write_data_to_disk(sorted_data, "by_num_raters.md")

    sorted_data = sorted(data.items(), key=lambda x: x[1]["numProgressed"], reverse=True)
    write_data_to_disk(sorted_data, "by_num_players.md")

    sorted_data = sorted(data.items(), key=lambda x: x[1]["numCompleted"], reverse=True)
    write_data_to_disk(sorted_data, "by_num_platinum_trophies.md")

    return
