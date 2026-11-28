from src.api import send_post_request_to_api, to_data
from src.config import GRAPHQL_API_URL


class FakeResponse:
    def __init__(self, ok, payload=None, status_code=200):
        self.ok = ok
        self._payload = payload
        self.status_code = status_code

    def json(self):
        return self._payload


class FakeScraper:
    def __init__(self, response):
        self.response = response
        self.requests = []

    def post(self, url, json=None, timeout=None):
        self.requests.append((url, json, timeout))
        return self.response


def test_to_data_returns_json_when_response_is_ok():
    response = FakeResponse(ok=True, payload={"data": {"x": 1}})
    assert to_data(response) == {"data": {"x": 1}}


def test_to_data_returns_none_when_response_is_not_ok(capsys):
    response = FakeResponse(ok=False, status_code=503)
    assert to_data(response, verbose=True) is None
    assert "503" in capsys.readouterr().out


def test_to_data_is_silent_when_not_verbose(capsys):
    response = FakeResponse(ok=False, status_code=503)
    assert to_data(response, verbose=False) is None
    assert capsys.readouterr().out == ""


def test_send_post_request_hits_the_graphql_endpoint():
    payload = {"data": {"StorePageMapping": {"mapping": {"sandboxId": "abc"}}}}
    scraper = FakeScraper(FakeResponse(ok=True, payload=payload))

    data = send_post_request_to_api({"query": "{...}"}, scraper=scraper, verbose=False)

    assert data == payload
    url, json_data, _timeout = scraper.requests[0]
    assert url == GRAPHQL_API_URL
    assert json_data == {"query": "{...}"}
