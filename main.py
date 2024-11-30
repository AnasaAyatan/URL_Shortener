from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
import string, secrets, logging
from datetime import datetime, timedelta
from urllib.parse import urlparse

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)
logging.basicConfig(filename='access.log', level=logging.INFO)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    short_code = db.Column(db.String(6), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=True)

def generate_short_code():
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(6))

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def is_safe_url(url):
    blacklist = ["malicious.com", "phishing.com"]
    return urlparse(url).netloc not in blacklist

def shorten_url(original_url):
    if not is_valid_url(original_url):
        return "Invalid URL format."
    if not is_safe_url(original_url):
        return "URL is potentially malicious."
    short_code = generate_short_code()
    expires_at = datetime.utcnow() + timedelta(days=7)
    new_url = URL(original_url=original_url, short_code=short_code, expires_at=expires_at)
    with app.app_context():
        db.session.add(new_url)
        db.session.commit()
    logging.info(f"{datetime.now()} - Shortened: {original_url} -> {short_code}")
    return f"Shortened URL: http://localhost:5000/{short_code} (Expires on: {expires_at})"

@app.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first_or_404()
    if url_entry.expires_at and datetime.utcnow() > url_entry.expires_at:
        return jsonify({'error': 'This URL has expired'}), 410
    logging.info(f"{datetime.now()} - Redirected: {short_code} -> {url_entry.original_url}")
    return redirect(url_entry.original_url)

def main():
    with app.app_context():
        db.create_all()
    print("Welcome to the URL Shortener!")
    while True:
        user_input = input("Enter a URL to shorten (or type 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        short_url = shorten_url(user_input)
        print(short_url)

if __name__ == '__main__':
    from threading import Thread

    def run_flask():
        app.run(debug=True, use_reloader=False)

    Thread(target=run_flask).start()
    main()
