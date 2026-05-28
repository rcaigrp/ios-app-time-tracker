#!/usr/bin/env python3

import json
import csv
import argparse
from datetime import datetime
from pathlib import Path

class TimeTracker:
    def __init__(self, storage_path="time_entries.json"):
        self.storage_path = Path(storage_path)
        if not self.storage_path.exists():
            self.storage_path.write_text(json.dumps([]))

    def add_entry(self, project, date, duration_hours, notes=""):
        """Add a new time entry."""
        entries = self._load_entries()
        entry = {
            "id": len(entries),
            "project": project,
            "date": date,
            "duration_hours": duration_hours,
            "notes": notes
        }
        entries.append(entry)
        self._save_entries(entries)
        return entry

    def list_entries(self):
        """Return all stored entries."""
        return self._load_entries()

    def export_json(self, output_path):
        """Export entries to JSON file."""
        entries = self.list_entries()
        with open(output_path, 'w') as f:
            json.dump(entries, f, indent=2)

    def export_csv(self, output_path):
        """Export entries to CSV file."""
        entries = self.list_entries()
        if not entries:
            return
        
        fieldnames = ['id', 'project', 'date', 'duration_hours', 'notes']
        with open(output_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for entry in entries:
                writer.writerow(entry)

    def _load_entries(self):
        """Load entries from storage."""
        try:
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_entries(self, entries):
        """Save entries to storage."""
        with open(self.storage_path, 'w') as f:
            json.dump(entries, f, indent=2)


def main():
    parser = argparse.ArgumentParser(description='Time Tracker CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Add entry command
    add_parser = subparsers.add_parser('add', help='Add a new time entry')
    add_parser.add_argument('--project', required=True, help='Project name')
    add_parser.add_argument('--date', required=True, help='Date in YYYY-MM-DD format')
    add_parser.add_argument('--duration', type=float, required=True, help='Duration in hours')
    add_parser.add_argument('--notes', default='', help='Optional notes')

    # List entries command
    list_parser = subparsers.add_parser('list', help='List all time entries')

    # Export command
    export_parser = subparsers.add_parser('export', help='Export entries to file')
    export_parser.add_argument('--format', choices=['json', 'csv'], required=True)
    export_parser.add_argument('--output', required=True, help='Output file path')

    args = parser.parse_args()

    tracker = TimeTracker()

    if args.command == 'add':
        entry = tracker.add_entry(args.project, args.date, args.duration, args.notes)
        print(f"Added entry: {entry}")
    elif args.command == 'list':
        entries = tracker.list_entries()
        for entry in entries:
            print(entry)
    elif args.command == 'export':
        if args.format == 'json':
            tracker.export_json(args.output)
        elif args.format == 'csv':
            tracker.export_csv(args.output)
        print(f"Exported to {args.output}")

if __name__ == '__main__':
    main()