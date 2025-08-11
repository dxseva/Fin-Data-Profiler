import cProfile
import pstats
import sys
from io import StringIO
from contextlib import redirect_stdout
import importlib

sys.argv = ['financial.py', 'MSFT', 'Total Revenue']
financial = importlib.import_module("financial")

cProfile.runctx("financial.main()", globals(), locals(), "profiling-cumulative.stats")

with open("pstats-cumulative.txt", "w") as f:
    output = StringIO()
    with redirect_stdout(output):
        p = pstats.Stats("profiling-cumulative.stats")
        p.sort_stats("cumulative").print_stats(5)
    f.write(output.getvalue())
