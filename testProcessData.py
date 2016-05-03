#! /usr/bin/env python3
"""
@author: mboyd

Test the yearCount and popCount methods of the processData module
"""
import unittest
import json
import os
import csv
from processData import DataProcessor

class ProcessDataTest(unittest.TestCase):
    
    def setUp(self):
        self.testData = json.dumps({1:  {"name": "John Doe", "birth": 1902, "death": 1941},
                            2:  {"name": "Sue Simmons", "birth": 1912, "death": 1988},
                            3:  {"name": "Jack Sprat", "birth": 1925, "death": 1976},
                            4:  {"name": "Manny Mellmick", "birth": 1932, "death": 1998},
                            5:  {"name": "Charles Chadwick", "birth": 1945, "death": 2014},
                            6:  {"name": "Vance Vargas", "birth": 1952, "death": False},
                            7:  {"name": "Tommy Thompson", "birth": 1916, "death": 2002},
                            8:  {"name": "Raven Ronaldson", "birth": 1986, "death": False},
                            9:  {"name": "Kasmir Kandahari", "birth": 1936, "death": 1999},
                            10: {"name": "Jessica Jones", "birth": 1988, "death": False}})
        self.pd = DataProcessor(self.testData)
        
    
    def testYearCount(self):
        self.assertEqual(self.pd.yearCount(1900), 0, "There should be 0 people alive in the year 1900.")
        self.assertEqual(self.pd.yearCount(1950), 6, "There should be 6 people alive in the year 1950.")
        self.assertEqual(self.pd.yearCount(2000), 5, "There should be 5 people alive in the year 2000.")
        
    def testPopCount(self):
        self.assertEqual(self.pd.popCount(1900, 1930), (4, [1925, 1926, 1927, 1928, 1929, 1930]))
        self.assertEqual(self.pd.popCount(1940, 1950), (6, [1940, 1945, 1946, 1947, 1948, 1949, 1950]))
        
    def testCSV(self):
        self.pd.popCount(1900, 1930, True)
        here = os.path.dirname(__file__)
        csvFile = os.path.join(here, "1900to1930.csv")
        self.assertTrue(os.path.exists(csvFile), "CSV File should have been created")
        if os.path.exists(csvFile):
            with open(csvFile) as csvf:
                dr = csv.reader(csvf)
                for i, row in enumerate(dr):
                    if i == 1:
                        self.assertEqual(int(row[0]), 1900)
                        self.assertEqual(int(row[1]), 1)
                    if i == 2:
                        self.assertEqual(int(row[0]), 1910)
                        self.assertEqual(int(row[1]), 2)
                    if i == 3:
                        self.assertEqual(int(row[0]), 1920)
                        self.assertEqual(int(row[1]), 3)       
        
        
if __name__ == "__main__":
    unittest.main()
    