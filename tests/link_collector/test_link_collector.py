import unittest
from link_collector.link_collector import LinkCollector


class HtmlLinkCollectorTestCase(unittest.TestCase):
    def setUp(self):
        self.path = 'http://localhost:8000'

    def test_read_index_html(self):
        link_collector = LinkCollector('index.html')
        links = link_collector.collect_links(self.path)
        self.assertIsNotNone(links)
        self.assertEqual(len(links), 6)


if __name__ == '__main__':
    unittest.main()
