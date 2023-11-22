import os
from pathlib import Path

import pandas as pd

dates = pd.date_range(start="2023-12-01", end="2023-12-25")

for date in dates:
    date = str(date.date())
    base = f"{date}/{date}."

    os.makedirs(date)

    Path(f"{base}txt").touch()
    Path(f"{base}mojo").touch()
    Path(f"{base}py").touch()
    Path(f"{base}data").touch()
