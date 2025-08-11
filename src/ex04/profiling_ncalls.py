import cProfile
import pstats
import sys
from io import StringIO
from contextlib import redirect_stdout
import importlib

sys.argv = ['financial.py', 'MSFT', 'Total Revenue']
financial = importlib.import_module("financial")

cProfile.runctx("financial.main()", globals(), locals(), "profiling-ncalls.stats")

with open("profiling-ncalls.txt", "w") as f:
    output = StringIO()
    with redirect_stdout(output):
        p = pstats.Stats("profiling-ncalls.stats")
        p.sort_stats("ncalls").print_stats()
    f.write(output.getvalue())
