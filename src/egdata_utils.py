from urllib.parse import quote

import requests


def trigger_regen_for_slugs(slugs: list[str]) -> None:
    """Trigger regeneration for each slug via egdata.app API."""
    for slug in slugs:
        encoded_slug = quote(slug, safe='')
        try:
            response = requests.put(
                f'https://api.egdata.app/regen/{encoded_slug}', timeout=10
            )
            response.raise_for_status()
            print(f'Triggered regen for: {slug}')
        except Exception as e:
            print(f'Failed to trigger regen for {slug}: {e}')
