import os
import sys


cwd = os.getcwd()
ecad_path = os.path.join(cwd, 'ecad')

print(ecad_path)

DrcFileName = ""
isDrcFileAvailable = False

SummaryLineUnconnectedPads = ""
hasUnconnectedPads = False
cntUnconnectedPads = 0

SummaryLineErrors = ""
hasErrors = False
cntErrors = 0

# Check if *.rpt file exists

for _, _, filenames in os.walk(ecad_path):
    for file in filenames:
        if file.endswith('.rpt'):
            isDrcFileAvailable = True
            DrcFileName = file

if not isDrcFileAvailable:
    print("DRC report file is missing. Make sure a report file is created with the ending .rpt")
    sys.exit(10)

# Check quantity of warnings and errors

erc_file_path = os.path.join(ecad_path, DrcFileName)
with open(erc_file_path, encoding="utf8") as file:
    for cnt, line in enumerate(file):
        if "DRC errors **" in line:
            SummaryLineErrors = line
        if "unconnected pads **" in line:
            SummaryLineUnconnectedPads = line

cntUnconnectedPads = int(SummaryLineUnconnectedPads.split(' ')[2])
cntErrors = int(SummaryLineErrors.split(' ')[2])

if cntUnconnectedPads > 0:
    hasUnconnectedPads = True

if cntErrors > 0:
    hasErrors = True

if hasUnconnectedPads or hasErrors:
    print("PCB has {} errors and {} unconnected pads.".format(cntErrors, cntUnconnectedPads))
    sys.exit(10)

# All checks passed

print("PCB checked without known errors.")
