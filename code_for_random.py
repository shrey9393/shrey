import os
import random
import subprocess
from datetime import datetime, timedelta

start_date = datetime(2022, 10, 16)
end_date = datetime(2023, 4, 15)
for i in range(1, 100):
    filename = f"git{i}.py"
    with open(filename, "w") as f:
        f.write("# This is a sample file")

    # Generate random date within specified range
    random_date = start_date + \
        timedelta(days=random.randint(0, (end_date - start_date).days))

    # Run Git commands to add, commit, and push the file to GitHub with random date
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "data"])
    subprocess.run(["git", "commit", "--amend", "--date",
                   f"{random_date:%Y-%m-%d %H:%M:%S}", "--no-edit"])
    subprocess.run(["git", "push", "origin", "master"])

    # Print message to confirm file creation and push to GitHub with the random date
    print(f"Created files and pushed to GitHub on {random_date}")
