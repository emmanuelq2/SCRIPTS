import unittest

from time_add_seconds import add_seconds_to_times as solution


class TestAddSecondsToTimes(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solution(['10:00:00', '23:30:00'], 3600),
            ['11:00:00', '00:30:00']
        )

    def test2(self):
        self.assertEqual(
            add_seconds_to_times(['00:00:00'], 86399),
            ['23:59:59']
        )

    def test3(self):
        self.assertEqual(
            solution(['01:00:00', '02:00:00', '03:00:00'], 7200),
            ['03:00:00', '04:00:00', '05:00:00']
        )

    def test4(self):
        self.assertEqual(
            solution(['23:59:59'], 1),
            ['00:00:00']
        )

    def test5(self):
        self.assertEqual(
            add_seconds_to_times(['12:00:00'], 43200),
            ['00:00:00']
        )

    def test6(self):
        self.assertEqual(
            solution(['23:59:01', '23:59:02', '23:59:03'], 2),
            ['23:59:03', '23:59:04', '23:59:05']
        )

    def test7(self):
        self.assertEqual(
            solution(['13:14:15', '16:17:18', '19:20:21', '22:23:24'], 0),
            ['13:14:15', '16:17:18', '19:20:21', '22:23:24']
        )

    def test8(self):
        self.assertEqual(
            solution(['00:00:01', '00:00:02', '00:00:03', '00:00:04', '00:00:05', '00:00:06', '00:00:07', '00:00:08', '00:00:09', '00:00:10'], 30),
            ['00:00:31', '00:00:32', '00:00:33', '00:00:34', '00:00:35', '00:00:36', '00:00:37', '00:00:38', '00:00:39', '00:00:40']
        )


if __name__ == "__main__":
    unittest.main()