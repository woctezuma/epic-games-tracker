from src.data_utils import PAGE_MAPPINGS_FNAME, SANDBOX_IDS_FNAME
from src.discord_utils import post_git_diff_to_discord_using_keyword
from src.webhook_utils import WEBHOOK_KEYWORD_NEW, WEBHOOK_KEYWORD_TROPHY


def main():
    post_git_diff_to_discord_using_keyword(fname=PAGE_MAPPINGS_FNAME, webhook_keyword=WEBHOOK_KEYWORD_NEW)
    post_git_diff_to_discord_using_keyword(fname=SANDBOX_IDS_FNAME, webhook_keyword=WEBHOOK_KEYWORD_TROPHY)



if __name__ == '__main__':
    main()
