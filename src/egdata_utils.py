from urllib.parse import quote

import requests

from src.api import TIMEOUT_IN_SECONDS

EGDATA_API_URL = 'https://api.egdata.app'
REGEN_ENDPOINT = '/offers/regen/'


def trigger_regen_for_slugs(slugs: list[str]) -> None:
    """Trigger regeneration for each slug via egdata.app API."""
    for slug in slugs:
        encoded_slug = quote(slug, safe='')
        try:
            response = requests.put(
                f'{EGDATA_API_URL}{REGEN_ENDPOINT}{encoded_slug}',
                timeout=TIMEOUT_IN_SECONDS,
            )
            response.raise_for_status()
            print(f'Triggered regen for: {slug}')
        except Exception as e:
            print(f'Failed to trigger regen for {slug}: {e}')
