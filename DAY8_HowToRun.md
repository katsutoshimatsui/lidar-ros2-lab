# DAY8 How to run

1. Creat virtual enviroment

python3 -m venv .venv
source .venv/bin/activate
pip install pandas

2. Run CSV analysis directly
python analyze_csv.py --in sample.csv --out result.json --unique-col device_id

3. Run pipeline script
python run_pipeline.py --in sample.csv
