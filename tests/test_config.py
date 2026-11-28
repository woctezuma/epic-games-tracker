from src.config import DISCORD_API_URL, GRAPHQL_API_URL, STORE_URL


def test_endpoints_are_https_urls():
    for url in (GRAPHQL_API_URL, STORE_URL, DISCORD_API_URL):
        assert url.startswith("https://")


def test_graphql_endpoint_is_the_store_endpoint():
    # The store endpoint is more reliable and faster than the graphql endpoint
    # (see the revert of "Edit GraphQL URL again").
    assert GRAPHQL_API_URL == "https://store.epicgames.com/graphql"
