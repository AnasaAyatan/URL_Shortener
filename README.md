URL Shortener
This project provides a URL shortener tool built with Python. It offers two versions: a lightweight version with minimal features for basic use and a full main version with enhanced capabilities. Both versions use Flask for web hosting and SQLAlchemy for database management.

Lightweight Version
Description
The lightweight version is a simple URL shortener designed for basic functionality. It takes long URLs, generates a unique short code, and stores them in a SQLite database. Users can retrieve the original URL by accessing the short code.

Features
Generates 6-character random short codes for valid URLs.
Stores URLs and short codes in a SQLite database.
Redirects users to the original URL via a simple Flask endpoint.
Includes basic validation to ensure the URL is properly formatted.
How to Run
Install Python and the required packages:
bash
Copy code
pip install flask sqlalchemy
Start the application:
bash
Copy code
python lightweight.py
Enter URLs in the terminal to generate shortened links or use the provided Flask endpoint.
Full Main Version
Description
The full main version extends the lightweight version by adding advanced features such as expiration dates, URL safety checks, and action logging. This version is suitable for production use or integration into larger projects.

Features
URL Shortening: Generates unique 6-character short codes for valid URLs.
Expiration Dates: Shortened URLs expire after 7 days by default.
Malicious URL Detection: Uses a basic blacklist to block known malicious domains.
Redirection: Redirects users to the original URL if the short link is still valid.
Logging: Logs all URL shortening and redirection activities to an access.log file.
Command-Line and Web Interface: Provides both a CLI and a Flask-powered web server for flexibility.
How to Run
Install Python and the required packages:
bash
Copy code
pip install flask flask_sqlalchemy
Start the application:
bash
Copy code
python full_main.py
Use the command-line interface to input URLs and receive shortened links, or visit the web server (http://localhost) to interact via a browser.

plaintext
Copy code
Enter a URL to shorten: https://example.com
Shortened URL: http://localhost:5000/abc123 (Expires on: 2024-12-07)
Visit the short URL:

Go to http://localhost:5000/abc123 to be redirected to the original URL.
Access logs:

View logs in the access.log file for monitoring and debugging.
Future Enhancements
Add analytics for tracking the number of clicks on shortened URLs.
Implement user accounts for managing and tracking personal URLs.
Expand malicious URL detection with an external API or service.
Support custom expiration dates and custom short codes.
Enjoy using the URL Shortener!
