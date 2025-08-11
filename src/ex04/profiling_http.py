import cProfile
import pstats
import sys
from io import StringIO
from contextlib import redirect_stdout
import importlib

sys.argv = ['financial_enhanced.py', 'AAPL', 'totalRevenue']
financial_enhanced = importlib.import_module("financial_enhanced")

cProfile.runctx("financial_enhanced.main()", globals(), locals(), "profiling-http.stats")

with open("profiling-http.txt", "w") as f:
    output = StringIO()
    with redirect_stdout(output):
        p = pstats.Stats("profiling-http.stats")
        p.sort_stats("tottime").print_stats()
    f.write(output.getvalue())
