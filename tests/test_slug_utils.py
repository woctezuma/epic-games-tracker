from src.slug_utils import (
    filter_out_dummy_mappings,
    get_namespace_slug,
    get_offer_slug,
    get_product_slug,
    is_a_dummy_mapping,
    to_slug,
)


def make_store_element(offer_slugs=None, mappings=None, product_slug="game", url_slug="url-slug"):
    return {
        "offerMappings": [{"pageSlug": s} for s in offer_slugs] if offer_slugs else None,
        "catalogNs": {"mappings": [{"pageSlug": m} for m in mappings]} if mappings is not None else None,
        "productSlug": product_slug,
        "urlSlug": url_slug,
    }


def test_offer_slug_has_highest_priority():
    element = make_store_element(offer_slugs=["offer-slug"], mappings=["ns-slug"], product_slug="prod")
    assert to_slug(element) == "offer-slug"


def test_namespace_slug_is_used_when_no_offer():
    element = make_store_element(mappings=["ns-slug"], product_slug="prod")
    assert to_slug(element) == "ns-slug"


def test_dummy_mappings_are_filtered_out_when_several_mappings():
    element = make_store_element(mappings=["game-bundle", "real-slug"])
    assert get_namespace_slug(element) == "real-slug"


def test_single_dummy_mapping_is_kept():
    element = make_store_element(mappings=["game-bundle"])
    assert get_namespace_slug(element) == "game-bundle"


def test_product_slug_has_home_suffix_removed():
    assert get_product_slug(make_store_element(product_slug="game/home")) == "game"


def test_product_slug_is_used_when_no_offer_nor_namespace():
    element = make_store_element(product_slug="prod")
    assert to_slug(element) == "prod"


def test_url_slug_is_the_fallback():
    element = make_store_element(product_slug=None, url_slug="url-slug")
    assert to_slug(element) == "url-slug"


def test_get_offer_slug_with_empty_offers():
    assert get_offer_slug(make_store_element(offer_slugs=[])) is None
    assert get_offer_slug(make_store_element()) is None


def test_is_a_dummy_mapping():
    assert is_a_dummy_mapping({"pageSlug": "game-bundle"})
    assert is_a_dummy_mapping({"pageSlug": "game--premium-edition"})
    assert not is_a_dummy_mapping({"pageSlug": "game"})


def test_filter_out_dummy_mappings():
    mappings = [{"pageSlug": "game-bundle"}, {"pageSlug": "game"}, {"pageSlug": "other--premium-edition"}]
    assert filter_out_dummy_mappings(mappings) == [{"pageSlug": "game"}]
