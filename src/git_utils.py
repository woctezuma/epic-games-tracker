import subprocess

from src.utils import extract_list_difference

LINE_SEPARATOR = '\n'
ADDITION_PREFIX = '+ '
DELETION_PREFIX = '- '
FIELD_SEPARATOR = '"'
GAME_INDEX = 1


def bytes_to_str(data_as_bytes):
    return data_as_bytes.decode()


def git_status():
    args = ["git", "status"]
    return run_subprocess(args)


def git_diff(file_path):
    args = ["git", "diff", file_path]
    return run_subprocess(args)


def run_subprocess(args):
    output = subprocess.run(args, capture_output=True, check=True)
    stdout = bytes_to_str(output.stdout)
    stderr = bytes_to_str(output.stderr)
    return stdout, stderr


def filter_status(stdout, pattern):
    return [line for line in stdout.split(LINE_SEPARATOR) if pattern in line]


def filter_diff(stdout, prefix):
    return [line for line in stdout.split(LINE_SEPARATOR) if line.startswith(prefix)]


def filter_additions(stdout):
    return filter_diff(stdout, ADDITION_PREFIX)


def filter_deletions(stdout):
    return filter_diff(stdout, DELETION_PREFIX)


def extract_games(lines):
    games = []
    for line in lines:
        elements = line.split(FIELD_SEPARATOR)
        if len(elements) > GAME_INDEX:
            game_name = elements[GAME_INDEX]
            games.append(game_name)

    return games


def extract_new_games(stdout):
    added_games = extract_games(filter_additions(stdout))
    deleted_games = extract_games(filter_deletions(stdout))
    return extract_list_difference(added_games, deleted_games)
