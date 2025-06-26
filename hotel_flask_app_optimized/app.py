#!/usr/bin/env python3
"""
Hotel Booking Management System - Main Application Entry Point
Production PostgreSQL Version (Google Sheets Removed)
"""

# Import the PostgreSQL app as the main application
from app_postgresql import app, db

if __name__ == '__main__':
    # Development server
    import os
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)