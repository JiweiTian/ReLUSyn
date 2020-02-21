import csv
from attacksynthesis_1 import find_delta

inputs_to_change = [[i for i in range(74)]]

with open("attacksynthesis_3E.csv", 'w') as f:
    writer = csv.writer(f)
    for i in inputs_to_change:
        output = find_delta('../network_files/AP_predict.nt', '../network_files/input_1.csv', i, 200, 203)
        writer.writerows(output)
