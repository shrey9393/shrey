import os
import random
import subprocess
from datetime import datetime, timedelta

start_date = datetime(2023, 3, 1)
end_date = datetime(2023, 3, 11)

# Create a list of dates within the specified range
date_list = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

for i, date in enumerate(date_list):
    # Create file with name git(i).py
    filename = f"git{i}.py"
    with open(filename, "w") as f:
        f.write("# This is a sample file")

    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "data"])
    subprocess.run(["git", "commit", "--amend", "--date", f"{date:%Y-%m-%d %H:%M:%S}", "--no-edit"])
    subprocess.run(["git", "push", "origin", "master"])

    # Print message to confirm file creation and push to GitHub with the date
    print(f"Created files and pushed to GitHub on {date}")
