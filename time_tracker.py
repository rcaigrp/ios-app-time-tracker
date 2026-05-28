#!/usr/bin/env python3
import json
import csv
import argparse
import os
import requests
from datetime import datetime
from pathlib import Path

# --- Jira Service (Simulated) ---
class JiraService:
    def __init__(self, base_url, api_token):
        self.base_url = base_url.rstrip('/')
        self.api_token = api_token
        self.headers = {'Authorization': f'Bearer {api_token}', 'Content-Type': 'application/json'}

    def fetch_projects(self):
        """Fetches projects from Jira API."""
        url = f"{self.base_url}/rest/api/2/search"
        params = {'jql': 'project = active', 'maxResults': 50}
        try:
            response = requests.get(url, headers=self.headers, params=params)
            if response.status_code == 200:
                return response.json().get('issues', [])
            elif response.status_code == 429: # Rate limit
                print(f"Rate limit hit. Sleeping 60s.")
                return []
            else:
                print(f"Error fetching projects: {response.status_code}")
                return []
        except requests.RequestException as e:
            print(f"Network Error: {e}")
            return []

# --- Time Tracker Application ---
class TimeTrackerApp:
    def __init__(self):
        self.config = {}
        self.data_file = Path("time_entries.json")
        self.config_file = Path("config.json")
        self.load_config()
        self.load_data()

    def load_config(self):
        if self.config_file.exists():
            self.config = json.loads(self.config_file.read_text())

    def load_data(self):
        if self.data_file.exists():
            self.entries = json.loads(self.data_file.read_text())
        else:
            self.entries = []

    def save_data(self):
        self.data_file.write_text(json.dumps(self.entries, indent=2))

    def add_entry(self, project, date, duration_hours, notes=""):
        """Adds a new time entry."""
        entry = {
            'project': project,
            'date': date,
            'duration_hours': duration_hours,
            'notes': notes
        }
        self.entries.append(entry)
        self.save_data()

    def list_entries(self):
        """Lists all entries."""
        for entry in self.entries:
            print(f"{entry['date']}: {entry['project']} - {entry['duration_hours']}h")

    def export_csv(self):
        """Exports entries to CSV."""
        with open('time_entries.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Date', 'Project', 'Duration', 'Notes'])
            for entry in self.entries:
                writer.writerow([entry['date'], entry['project'], entry['duration_hours'], entry['notes']])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='JiraTime CLI')
    parser.add_argument('--add', help='Add entry')
    args = parser.parse_args()

    app = TimeTrackerApp()
    if args.add:
        # Simple parse for demo
        parts = args.add.split(',')
        if len(parts) >= 3:
            app.add_entry(parts[0], parts[1], parts[2])
            print("Entry added.")