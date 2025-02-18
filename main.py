"""
This file is deprecated. Please use api/main.py instead.
The server has been moved to the api/ directory for better organization.
"""

from api import app

if __name__ == "__main__":
    print("Warning: Using deprecated entry point. Please run 'python api/main.py' instead.")
    app.run(host="0.0.0.0", port=5000, debug=True)