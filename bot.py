import sys
from bookworker import *

if len(sys.argv) != 2:
    print(
        f"Usage: {sys.argv[0]} <minutes between each post>", file=sys.stderr)
    sys.exit(1)

bookworker = BookWorker()
