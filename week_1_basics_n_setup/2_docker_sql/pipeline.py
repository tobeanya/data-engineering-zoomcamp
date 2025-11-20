import sys
import pandas as pd

print("Sys version:", sys.version)
print("Pandas version:", pd.__version__)
print(sys.argv)

day = sys.argv[1] if len(sys.argv) > 1 else "1/1/2025"

print("Hello from the Dockerized SQL pipeline!")
print('job finished successfully for day:', day)

print(f'job finished successfully for day = {day}')