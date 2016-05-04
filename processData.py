#! /usr/bin/env python3
"""
processData.py
This module reads people data from a JSON file and determines
number of people alive per year and per decade.
This is written in Python 3.  The data it creates won't have the correct
form if compiled in Python 2.
"""
import os
import csv
import json

class DataProcessor():
    
    def __init__(self, pd):
        """
        Take in a JSON file, and create a dictionary from it.
        """
        if type(pd) == str:
            self.popData = json.loads(pd)
        else:
            self.popData = json.load(pd)
        
    def yearCount(self, year):
        """
        Go through the data and add people to the year's population count.
        """
        count = 0
        for k, v in self.popData.items():
            if (v["birth"] <= year) and (v["death"] > year or not v["death"]):
                count += 1
        return count
    
    def popCount(self, startYear, endYear, chartData = False):
        """
        Going from startYear to endYear, count the number of people alive per year.
        If chartData is True, generate a decade average for each decade in the range
        between startYear and endYear.
        """
        currYear = startYear
        highestPop = 0
        highestYear = [startYear]
            
        if chartData:
            chartfn = str(startYear) + "to" + str(endYear) + ".csv"
            chartf = open(chartfn, "w")
            fieldnames = ["decade", "averagePop"]
            chartw = csv.DictWriter(chartf, fieldnames = fieldnames)
            chartw.writeheader()
            currDec = startYear
            currDecAv = 0
            currDecTot = 0

        while currYear <= endYear: 
            currPop = self.yearCount(currYear)
            if currPop > highestPop:
                highestPop = currPop
                highestYear = [currYear]
            elif currPop == highestPop:
                highestYear.append(currYear)      
            if chartData:
                if (currYear + 1 - startYear) % 10:
                    currDecTot += currPop
                else:
                    currDecAv = round(currDecTot / 10)
                    chartw.writerow({fieldnames[0] : currDec, fieldnames[1]: currDecAv})
                    currDec = currYear + 1 
                    currDecTot = 0 
            currYear += 1    
        if chartData:
            chartf.close()
        return highestPop, highestYear
    
if __name__ == "__main__":
    with open("peopleData.json", "r") as peopleData:
        pd = DataProcessor(peopleData)
        highestPop, highestYear = pd.popCount(1900, 2000, True)
        print("Highest population was", highestPop)
        print("In the years", ", ".join(str(x) for x in highestYear))
        
        
    
