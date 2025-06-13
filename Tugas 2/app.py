from flask import Flask, request, render_template_string
import pandas as pd

app = Flask(__name__)

UPLOAD_HTML = """
<!doctype html>
<title>Upload CSV File</title>
<h1>Upload CSV File for Analysis</h1>
<form action="/" method=post enctype=multipart/form-data>
  <input type=file name=file>
  <input type=submit value=Upload>
</form>
{% if summary %}
  <h2>Data Summary:</h2>
  {{ summary | safe }}
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def upload_file():
    summary = ""
    if request.method == "POST":
        file = request.files['file']
        if file.filename.endswith('.csv'):
            df = pd.read_csv(file)
            summary = df.describe().to_html()
        else:
            summary = "Please upload a CSV file."
    return render_template_string(UPLOAD_HTML, summary=summary)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)