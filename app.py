from flask import Flask, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    os.makedirs("public", exist_ok=True)
    subprocess.run(["scrapy", "crawl", "termekek", "-o", "public/termekek.json"])
    return "Scraper sikeresen lefutott és elmentette a JSON-t."

@app.route('/json')
def serve_json():
    return send_file("public/termekek.json", mimetype='application/json')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host='0.0.0.0', port=port)        
