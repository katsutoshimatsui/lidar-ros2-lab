# CSV Data Analysis Pipeline (DAY6-DAY7)

## Overview
This project demostrates a simple but practical **data analysis pipeline**
using Python, focusing on **file I/O, data validation, and pipeline execution**.

The pipline reads CSV sensor data, analyzes missing values and unique counts,
and outputs structured JSON results.

This project is designed as a **portfolio artifact** to demonstrate:

- Python file I/O
- Pandas-based data inspection
- CLI design
- Script-to-script pipeline execution
-Reproducible local execution

---

## Directory Structure
```text

day6_fileio/
 |--analyze_cs.py       # CSV analysis script
 |--sample.csv          # Sample LiDAR-like sensor data
 |--result.json         # Generated analysis result

day7_pipeline/
 |--run.pipeline.py     # Pipeline script calling analyze_csv.py


## What This Project Demonstrate
- Handling missing values in CSV sensor data
- Structured JSON output for downstream systems
- CLI-driven scripts suitable for automation
- Clear separation between analysis logic and pipeline logic


## Next Steps
- Extend pipeline to support multiple input files
- Add logging and error handling
- Connect output to visualization or cloud storage
