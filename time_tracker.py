import click
import json
import os
import sys

DATA_FILE = "time_tracker_data.json"

def load_data():
    """Load time entries from local storage."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []

def save_data(data):
    """Save time entries to local storage."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def clean_up():
    """Remove data file if exists."""
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

@click.group()
def cli():
    """Jira Time Tracker CLI - Manage time entries locally."""
    pass

@cli.command()
@click.option('--start', required=True, help='Start timestamp.')
@click.option('--end', required=True, help='End timestamp.')
@click.option('--desc', required=True, help='Description of the task.')
def add(start, end, desc):
    """Add a new time entry."""
    entries = load_data()
    entry = {
        "start": start,
        "end": end,
        "desc": desc
    }
    entries.append(entry)
    save_data(entries)
    click.echo(f"Added entry: {desc}")

if __name__ == '__main__':
    cli()