import json
import os
os.chdir(r'C:\Users\paulo.roberto\Documents')
# file = json.loads('PowerBIPerformanceData.json',)

with open('PowerBIPerformanceData.json', 'r') as f:
    array = json.load(f)

print (array)