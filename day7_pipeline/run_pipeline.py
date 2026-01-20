#!/usr/bin/env python3

import argparse
import json
import subprocess
import sys
from pathlib import Path

ANALYZER = Path("../day6_fileio/analyze_csv.py").resolve()
INPUT_CSV=Path("../day6_fileio/sample.csv").resolve()

def run(cmd: list[str]) -> subprocess.CompletedProcess:
    """Run command and capture stdout/stderr."""
    return subprocess.run(cmd, capture_output=True, text=True)

def main() -> int:
    p=argparse.ArgumentParser(description="DAY7: run analyze_csv.py as a subprocesws and filter output")
    p.add_argument("--in", dest="input_csv", required=True, help="input CSV")
    p.add_argument("--unique-col", default="device_id")
    args=p.parse_args()

    input_csv=Path(args.input_csv)


    #1) Run analyze_csv.py (subprocess)
    cmd=[
            sys.executable, #use venv python
            str(ANALYZER),
            "--in", str(INPUT_CSV),
            "--out", "result.json",
            "--unique-col", args.unique_col,
    ]

    cp=run(cmd)

    if cp.returncode !=0:
        print("ERROR: analyze_csv.py failed", file=sys.stderr)
        print(cp.stderr, file=sys.stderr)
        return cp.returncode

    # 2) Parse stdout (pipe-like: take stdout -> json -> extract fields)
    data = json.loads(cp.stdout)

    # Minimal summary for console
    filtered={
            "rows": data.get("rows"),
            "cols": data.get("cols"),
            "missing_values_total": data.get("missing_values_total"),
            "unique_count": data.get("unique_count"),
            "top_values": data.get("top_values"),
    }

    print(json.dumps(filtered,ensure_ascii=False, indent=2))
    return 0


if __name__=="__main__":
    raise SystemExit(main())


