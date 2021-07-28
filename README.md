# sssync
Minimal time sync server for sssecond time unit system

Stack: Python 3.9/Flask
Output format: json
Deployment: just launch main.py
Usage: Get HTTP content from http://<yourhostname>:864 and sync your ss clock with received data
Example output:
<code>
{"year": 2020, "month": 2, "date": 62, "ss": 59943.28703703704}
</code>
