from flask import Flask, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def run_scraper():
    os.makedirs("public", exist_ok=True)
    subprocess.run([
        "scrapy", "crawl", "termekek", "-o", "public/termekek.json"
    ])
    return "Scraper lefutott és termekek.json létrejött."

@app.route('/json')
def serve_json():
    return send_file("public/termekek.json", mimetype='application/json')
