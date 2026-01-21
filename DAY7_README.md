# DAY7: Pipeline orchestration

## Overview
This day focuses on building a simple data processing pipeline
by orchestating independent Python scripts.

## Components
- day6_fileio/analyze_csv.py
 -> CSV analysis script (standalone,reusable)

- day7_pipeline/run_pipeline.py
 ->Orchestrator script using subprocess


## Design Points
- Loose coupling between scrips
- Use of subprocess instead of direct imports
- Exit code and stderr based error handling
- JSON output used as an interface between steps

## Why subprocess
- Enables Unix-like pipeline design
- Scripts remain independently executable
- Failures are easy to detect and isolte

## Outcome
- CSV file is analyzed
- Results are passed as JSON
- Selected fields are extracted and printed
