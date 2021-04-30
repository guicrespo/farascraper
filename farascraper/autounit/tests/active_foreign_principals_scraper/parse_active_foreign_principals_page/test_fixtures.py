# THIS IS A GENERATED FILE
# Generated by: scrapy crawl active_foreign_principals_scraper  # noqa: E501
import os
import unittest
from glob import glob

from scrapy_autounit.player import Player


class AutoUnit(unittest.TestCase):
    def test__active_foreign_principals_scraper__parse_active_foreign_principals_page(self):
        _dir = os.path.dirname(os.path.abspath(__file__))
        fixtures = glob(os.path.join(_dir, "*.bin"))
        for fixture in fixtures:
            player = Player.from_fixture(fixture)
            player.playback()


if __name__ == '__main__':
    unittest.main()
