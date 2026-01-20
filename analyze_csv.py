#! /usr/bin/env python3
import argparse
import json
from pathlib import Path

import pandas as pd

def summarize_csv(csv_path: Path, unique_col: str | None = None) -> dict:
    df = pd.read_csv(csv_path)

    summary= {
            "input_file": str(csv_path),
            "rows": int(df.shape[0]),
            "cols": int(df.shape[1]),
            "columns": list(df.columns),
            "missing_values_total": int(df.isna().sum().sum()),
            "missing_by_column": {c: int(df[c].isna().sum()) for c in df.columns},
    }

    if unique_col and unique_col in df.columns:
        summary["unique_count"]={unique_col: int(df[unique_col].nunique(dropna=True))}
        summary["top_values"]={
                unique_col: df[unique_col].value_counts(dropna=True).head(5).to_dict()
        }

    return summary

def main() -> int:
    parser = argparse.ArgumentParser(description="CSV summary -> JSON output")
    parser.add_argument("--in", dest="input_csv", required=True, help="input CSV path")
    parser.add_argument("--out", dest="output_json", required=True, help="output JSON path")
    parser.add_argument("--unique-col",dest="unique_col", default=None, help="column name to count uniques")
    args=parser.parse_args()

    in_path=Path(args.input_csv)
    out_path=Path(args.output_json)

    if not in_path.exists():
        raise FileNotFoundError(f"Input CSV not found: {in_path}")

    summary = summarize_csv(in_path, unique_col=args.unique_col)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    
    print("WRITE_TO:", out_path.resolve())

    with out_path.open("w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())


