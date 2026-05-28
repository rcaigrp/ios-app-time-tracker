import argparse
import json
import os
import sys
import requests
from datetime import datetime

# --- Configuration ---
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'time_entries.json')

# --- Data Management ---
class DataStore:
    def __init__(self):
        self._data = []
        self.load()

    def load(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as f:
                    self._data = json.load(f)
            except json.JSONDecodeError:
                print("Warning: Corrupted data file, starting fresh.")
                self._data = []
        return self._data

    def save(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self._data, f, indent=2)

    def add_entry(self, project, description, duration):
        entry = {
            "id": len(self._data) + 1,
            "project": project,
            "description": description,
            "duration": duration,
            "date": datetime.now().isoformat()
        }
        self._data.append(entry)
        self.save()
        print(f"[SUCCESS] Entry added: {project} ({duration}h)")

    def list_entries(self):
        if not self._data:
            print("No time entries found.")
            return
        print("\nID\tProject\tDescription\tDuration\tDate")
        print("-" * 60)
        for entry in self._data:
            print(f"{entry['id']}\t{entry['project']}\t{entry['description']}\t{entry['duration']}\t{entry['date']}")

# --- CLI Logic ---
def main():
    parser = argparse.ArgumentParser(description='Jira Time Tracker CLI')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Add Command
    add_parser = subparsers.add_parser('add', help='Add a time entry')
    add_parser.add_argument('project', help='Project name')
    add_parser.add_argument('--description', default='No description', help='Description')
    add_parser.add_argument('--duration', required=True, help='Duration in hours')
    add_parser.set_defaults(func=lambda args: DataStore().add_entry(args.project, args.description, args.duration))

    # List Command
    list_parser = subparsers.add_parser('list', help='List all entries')
    list_parser.set_defaults(func=lambda args: DataStore().list_entries())

    # Sync Command
    sync_parser = subparsers.add_parser('sync', help='Sync projects from Jira API')
    sync_parser.set_defaults(func=lambda args: DataStore().sync_projects())

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()