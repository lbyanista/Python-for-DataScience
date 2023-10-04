import time
from datetime import datetime

timestamp = time.time()

scientific_notation = f"{timestamp:.2e}"

formated_date = datetime.utcfromtimestamp(
    timestamp).strftime("%b %d %Y")

print(
    f"Seconds since January 1, 1970: {timestamp:,.4f} or {scientific_notation} in scientific notation")
print(formated_date)
