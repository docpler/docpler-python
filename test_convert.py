import sys
from docpler.hwp import convert

if len(sys.argv) < 2:
    print(f"Usage: python {sys.argv[0]} <file.hwp>")
    sys.exit(1)

print(convert(sys.argv[1]))
