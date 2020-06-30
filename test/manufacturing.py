import os
import sys


cwd = os.getcwd()
mfg_path = os.path.join(cwd, 'mfg')
drills_path = os.path.join(mfg_path, 'drill')
gerber_path = os.path.join(mfg_path, 'gerber')

isFolderAvailable = False
isDrillFolderAvailable = False
isDrillAvailable = False
isGerberFolderAvailable = False
isGerberAvailable = False

# Check if 'mfg' folder exists

if os.path.exists(mfg_path):
    isFolderAvailable = True
else:
    print("Manufacturing folder is missing.")
    sys.exit(10)

# Check if 'drill' folder exists inside 'mfg' folder

if os.path.exists(drills_path):
    isDrillFolderAvailable = True
else:
    print("Drill folder is missing.")
    sys.exit(10)

# Check if 'gerber' folder exists inside 'mfg' folder

if os.path.exists(gerber_path):
    isGerberFolderAvailable = True
else:
    print("Gerber folder is missing.")
    sys.exit(10)

# All checks passed

print("Manufacturing data checked without known errors.")
