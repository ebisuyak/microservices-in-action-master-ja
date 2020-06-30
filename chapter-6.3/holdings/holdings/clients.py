import logging

import requests
from tenacity import before_log, retry, wait_exponential, stop_after_delay, wait_random


class MarketDataClient(object):
    logger = logging.getLogger(__name__)

    base_url = 'http://market-data:8000'

    def _make_request(self, url):
        response = requests.get(
            f"{self.base_url}/{url}", headers={'content-type': 'application/json'})
        return response.json()

    @retry(wait=wait_exponential(multiplier=1, max=5) + wait_random(0, 1),
        stop=stop_after_delay(5),
        before=before_log(logger, logging.DEBUG))
    def all_prices(self):
        return self._make_request("prices")

    def price(self, code):
        return self._make_request(f"prices/{code}")
