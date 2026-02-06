# Linux Log SnapShot & Analytics Pipeline

## Archtecture

[Data Source]
(log file / csv/ json )
	|
	|
	V
[Collector & Snapshot]
-bash script
-timestamp naming
	|
	|
	V
[Compression & Rotation]
-gzip
-retention (N days / N files)
	|
	|
	V
[Storage]
- /var/log/snapshots/ YYYY/MM/DD
	|
	+
	|
	V
[Search / Investigation]	[Aggregation / Report]
-zgrep / zcat			-Python (pandas)
-incident 			-daily summary csv
