import argparse
import json
import csv
import os
from datetime import datetime

DATA_FILE = "tracker.json"

def load_data():
    """Load time entries from JSON file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_data(entries):
    """Save entries to JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(entries, f)

def add_entry(project):
    """Create a new time entry."""
    entries = load_data()
    entry = {
        "project": project,
        "timestamp": datetime.now().isoformat()
    }
    entries.append(entry)
    save_data(entries)
    print(f"Entry added: {project}")

def list_entries():
    """Display all time entries."""
    entries = load_data()
    if not entries:
        print("No entries found.")
        return
    for e in entries:
        print(f"{e['project']} - {e['timestamp']}")

def export_csv(filename):
    """Export entries to a CSV file."""
    entries = load_data()
    if not entries:
        print("No entries to export.")
        return
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Project', 'Timestamp'])
        for e in entries:
            writer.writerow([e['project'], e['timestamp']])
    
    print(f"Data exported to {filename}")

def main():
    parser = argparse.ArgumentParser(description='Simple Time Tracker CLI')
    subparsers = parser.add_subparsers(dest='command')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new time entry')
    add_parser.add_argument('project', help='Project ID (e.g., JIRA-123)')
    
    # List command
    subparsers.add_parser('list', help='List all entries')
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Export entries to CSV')
    export_parser.add_argument('output', nargs='?', default='time_log.csv', help='Output CSV file')
    
    args = parser.parse_args()
    
    if args.command == 'add':
        add_entry(args.project)
    elif args.command == 'list':
        list_entries()
    elif args.command == 'export':
        export_csv(args.output)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
