import os
import sys


cwd = os.getcwd()
ecad_path = os.path.join(cwd, 'ecad')

print(ecad_path)

ErcFileName = ""
isErcFileAvailable = False
SummaryLine = ""
hasWarnings = False
cntWarnings = 0
hasErrors = False
cntErrors = 0

# Check if *.erc file exists

for _, _, filenames in os.walk(ecad_path):
    for file in filenames:
        if file.endswith('.erc'):
            isErcFileAvailable = True
            ErcFileName = file

if not isErcFileAvailable:
    print("ERC report file is missing. Make sure a report file is created with the ending .erc")
    sys.exit(10)

# Check quantity of warnings and errors

erc_file_path = os.path.join(ecad_path, ErcFileName)
with open(erc_file_path, encoding="utf8") as file:
    for cnt, line in enumerate(file):
        if line.startswith(" ** ERC messages:"):
            SummaryLine = line
            break

cntWarnings = int(SummaryLine.split(' ')[10])
cntErrors = int(SummaryLine.split(' ')[7])

if cntWarnings > 0:
    hasWarnings = True

if cntErrors > 0:
    hasErrors = True

if hasWarnings or hasErrors:
    print("Schematic has {} warnings and {} errors.".format(cntWarnings, cntErrors))
    sys.exit(10)

# All checks passed

print("Schematic checked without known errors.")
