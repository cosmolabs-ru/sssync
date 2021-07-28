# sssync
Minimal time sync server for sssecond time unit system <br><br>

Stack: Python 3.9/Flask<br>
Output format: json<br>
Deployment: just launch main.py<br>
Usage: Get HTTP content from http://<yourhostname>:864 and sync your ss clock with received data<br>
Example output:<br>
<code>
{"year": 2020, "month": 2, "date": 62, "ss": 59943.28703703704}
</code>
