import os
import sys


cwd = os.getcwd()
doc_path = os.path.join(cwd, 'doc')

isFolderAvailable = False
isBomAvailable = False
isSchematicAvailable = False

# Check if 'doc' folder exists

if os.path.exists(doc_path):
    isFolderAvailable = True
else:
    print("Documentation folder is missing.")
    sys.exit(10)

# Check if BOM_* and SCHEMATIC_* file exist

for dirpath, dirnames, filenames in os.walk(doc_path):
    for file in filenames:
        if file.startswith('BOM_'):
            isBomAvailable = True
        if file.startswith('SCHEMATIC_'):
            isSchematicAvailable = True

if not isBomAvailable:
    print("BOM file is missing.")
    sys.exit(10)

if not isSchematicAvailable:
    print("Schematic file is missing.")
    sys.exit(10)

# All checks passed

print("Documentation checked without known errors.")
