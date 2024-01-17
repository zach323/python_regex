import unittest
import event_regex as er
class TestRegex(unittest.TestCase):

    def test_regex_expected(self):

        
        exp_port1 = 11332
        exp_port2 = 19778
        exp_port3 = 60641
        event_reader = er.EventReader('event.txt')
        event = er.Event(event_reader.read_event_from_file())

        re_pattern = r'''((?<=port\s)\d+)|((?<=Port:\s)\d+)|((?<=port:")\d+(?="))'''

        results = er.search(event, event_reader, re_pattern)
        self.assertEqual(int(results[0][0]), exp_port1)
        self.assertEqual(int(results[1][1]), exp_port2)
        self.assertEqual(int(results[2][2]), exp_port3)

    def test_regex_unexpected(self):


        exp_port = 123456


        event_reader = er.EventReader('event2.txt')
        event = er.Event(event_reader.read_event_from_file())

        re_pattern = r'''((?<=port\s)\d+)|((?<=Port:\s)\d+)|((?<=port:")\d+(?="))'''

        results = er.search(event, event_reader, re_pattern)
        self.assertEqual(int(results[2][2]), exp_port)
        self.assertEqual(int(results[1][1]), exp_port)

if __name__ == '__main__':
    unittest.main()