#!/bin/bash

# Paths
OLD_ENV="/Users/yazanmulla/techcs-236346/z3env"
NEW_ENV="/Users/yazanmulla/Desktop/techcs-236346FORK/z3env-copy"

# Step 1: Activate old environment
source "$OLD_ENV/bin/activate"

# Step 2: Export current packages
pip freeze > /tmp/requirements.txt

# Step 3: Deactivate the old environment
deactivate

# Step 4: Create new environment
python3 -m venv "$NEW_ENV"

# Step 5: Activate new environment
source "$NEW_ENV/bin/activate"

# Step 6: Install all packages
pip install -r /tmp/requirements.txt

# Step 7: Clean up
rm /tmp/requirements.txt

# Done!
echo "✅ New virtual environment created at $NEW_ENV and activated."
