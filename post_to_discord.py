from src.data_utils import PAGE_MAPPINGS_FNAME, SANDBOX_IDS_FNAME
from src.discord_utils import DISCORD_NEW_HEADER, DISCORD_TROPHY_HEADER, post_git_diff_to_discord


def main():
    post_git_diff_to_discord(fname=PAGE_MAPPINGS_FNAME, header=DISCORD_NEW_HEADER)
    post_git_diff_to_discord(fname=SANDBOX_IDS_FNAME, header=DISCORD_TROPHY_HEADER)

    return


if __name__ == '__main__':
    main()
