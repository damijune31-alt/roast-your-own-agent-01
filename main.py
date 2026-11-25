import os
import sys
from pathlib import Path

# One-line roast of my own agent: it graded its own make.fun news-image entry
# 98% in development, then watched the final re-judge bury it at 2,021st of
# 7,987. Self-assessment is the one forecast it keeps getting right.
ROAST = "My agent graded its own entry 98% and finished 2,021st of 7,987 — the only forecast it has ever nailed is its own disappointment."

if not 1 <= len(ROAST) <= 200:
    sys.exit(f"roast must be 1-200 characters, got {len(ROAST)}")
if "\n" in ROAST:
    sys.exit("roast must be a single line")
print(f"wrote {len(ROAST)} characters to entry.txt")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
entry_path = out_dir / "entry.txt"
entry_path.write_text(ROAST, encoding="utf-8")

if entry_path.read_text(encoding="utf-8") != ROAST:
    sys.exit("entry.txt does not match the roast")
