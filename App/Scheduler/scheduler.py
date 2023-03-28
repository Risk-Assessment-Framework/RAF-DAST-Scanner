from datetime import datetime, timedelta
import sqlite3
import time
import requests

DB_NAME = 'schedule.db'
API_URL = 'http://localhost:5000/scan'

def create_database():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE schedules
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 url TEXT NOT NULL,
                 scan_time TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_schedule(url, scan_time):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO schedules (url, scan_time) VALUES (?, ?)", (url, scan_time))
    conn.commit()
    conn.close()

def get_schedules():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM schedules")
    schedules = c.fetchall()
    conn.close()
    return schedules

def run_scan(url):
    data = {'url': url}
    response = requests.post(API_URL, json=data)
    return response

def scan_scheduler():
    while True:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        schedules = get_schedules()
        for schedule in schedules:
            schedule_id, url, scan_time = schedule
            if scan_time <= now:
                response = run_scan(url)
                if response.status_code == 200:
                    print(f'Scan completed for {url} at {now}')
                    remove_schedule(schedule_id)
                else:
                    print(f'Scan failed for {url} at {now}')
        time.sleep(60)

if __name__ == '__main__':
    create_database()
    scan_scheduler()
