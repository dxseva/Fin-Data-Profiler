import cProfile
import pstats
import sys
from io import StringIO
from contextlib import redirect_stdout
import financial

if len(sys.argv) == 3:
    ticker = sys.argv[1]
    field_name = sys.argv[2]
else:
    ticker = 'MSFT'
    field_name = 'Total Revenue'

sys.argv = ['financial.py', ticker, field_name]

cProfile.run('financial.main()', 'profiling-tottime.stats')

p = pstats.Stats('profiling-tottime.stats')
output = StringIO()
with redirect_stdout(output):
    p.sort_stats('tottime').print_stats()
with open('profiling-tottime.txt', 'w') as f:
    f.write(output.getvalue())
