# profiling_sleep.py
import cProfile
import pstats
import sys
from io import StringIO
from contextlib import redirect_stdout
import importlib

# Подмена sys.argv для financial.py
sys.argv = ['financial.py', 'MSFT', 'Total Revenue']

# Импорт после подмены аргументов
financial = importlib.import_module("financial")

# Профилируем вызов main()
cProfile.runctx("financial.main()", globals(), locals(), "profiling-sleep.stats")

# Читаем .stats и сохраняем как текст
with open("profiling-sleep.txt", "w") as f:
    output = StringIO()
    with redirect_stdout(output):
        p = pstats.Stats("profiling-sleep.stats")
        p.sort_stats("tottime").print_stats()
    f.write(output.getvalue())

