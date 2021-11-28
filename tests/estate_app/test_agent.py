import unittest
from estate_app.agent import Agent


class AgentTestCase(unittest.TestCase):
    def test_add_property(self):
        agent = Agent()
        agent.add_property()
        agent.display_properties()



if __name__ == '__main__':
    unittest.main()