#!/usr/bin/env python3
import json
import argparse
import os
import requests
from datetime import datetime

DATA_FILE = 'time_entries.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_data(entries):
    with open(DATA_FILE, 'w') as f:
        json.dump(entries, f, indent=2)

class JiraService:
    def __init__(self, base_url, api_token):
        self.base_url = base_url
        self.token = api_token

    def get_projects(self):
        url = f"{self.base_url}/rest/api/2/search"
        headers = {'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get('issues', [])
        return []

class TimeTracker:
    def __init__(self):
        self.entries = load_data()

    def add(self, project, hours, date):
        entry = {'project': project, 'hours': hours, 'date': date}
        self.entries.append(entry)
        save_data(self.entries)
        print(f"Entry added: {project} - {hours}h ({date})")

    def list_entries(self):
        for entry in self.entries:
            print(f"- {entry['project']}: {entry['hours']}h on {entry['date']}")

    def sync_with_jira(self, base_url, api_token):
        jira_projects = JiraService(base_url, api_token).get_projects()
        print(f"Synced {len(jira_projects)} projects from Jira.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple Time Tracker')
    subparsers = parser.add_subparsers(dest='command')
    
    # Add command
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('project')
    add_parser.add_argument('hours', type=float)
    add_parser.add_argument('date', default=datetime.now().strftime('%Y-%m-%d'))
    add_parser.set_defaults(func=lambda args: TimeTracker().add(args.project, args.hours, args.date))

    # List command
    subparsers.add_parser('list').set_defaults(func=lambda args: TimeTracker().list_entries())

    # Sync command
    sync_parser = subparsers.add_parser('sync')
    sync_parser.add_argument('--url')
    sync_parser.add_argument('--token')
    sync_parser.set_defaults(func=lambda args: TimeTracker().sync_with_jira(args.url, args.token))

    args = parser.parse_args()
    if args.command:
        args.func(args)
