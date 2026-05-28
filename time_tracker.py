import argparse
import sys
import os
import json
from datetime import datetime

# Add current directory to path to import modules if needed
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def fetch_projects(jira_url, api_token):
    '''Simulates fetching projects from Jira API.'''
    # In a real app, this would use requests
    return [
        {"id": "PROJ-1", "name": "Project A"},
        {"id": "PROJ-2", "name": "Project B"}
    ]

def save_to_local_storage(entries):
    '''Saves time entries to a local file.'''
    filename = 'time_entries.json'
    with open(filename, 'w') as f:
        json.dump(entries, f)
    print(f"Saved {len(entries)} entries to {filename}")

def load_from_local_storage():
    '''Loads time entries from local storage.'''
    filename = 'time_entries.json'
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def main():
    parser = argparse.ArgumentParser(description='Jira Time Tracker CLI')
    subparsers = parser.add_subparsers(dest='command')

    # 'sync' command
    sync_parser = subparsers.add_parser('sync')
    sync_parser.add_argument('--url', required=True, help='Jira Base URL')
    sync_parser.add_argument('--token', required=True, help='Jira API Token')

    # 'add' command
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('--project', required=True, help='Project Name')
    add_parser.add_argument('--time', type=float, required=True, help='Time in seconds')

    args = parser.parse_args()

    if args.command == 'sync':
        print(f"Syncing with Jira at {args.url}...")
        projects = fetch_projects(args.url, args.token)
        print(f"Fetched {len(projects)} projects")
        save_to_local_storage([]) # Simulate saving sync result

    elif args.command == 'add':
        entry = {
            'project': args.project,
            'time': args.time,
            'timestamp': datetime.now().isoformat()
        }
        entries = load_from_local_storage()
        entries.append(entry)
        save_to_local_storage(entries)
        print(f"Added entry: {args.project} ({args.time}s)")

if __name__ == '__main__':
    main()