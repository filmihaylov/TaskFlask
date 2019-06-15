import unittest
import os
import json
from app import app
from multiprocessing import Process
import time

class FlaskAppTestCase(unittest.TestCase):
    server = Process(target=app.run)

    def setUp(self):
        print("starting server process")
        self.server.start()

    def tearDown(self):
        self.server.terminate()
        self.server.join()
        print("server terminating")


    def test_firs(tself):
        pass




if __name__ == "__main__":
    unittest.main()