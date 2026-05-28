import click
import json
import os
from datetime import datetime

data_file = "time_tracker_data.json"

def load_data():
    """Load time entries from local storage."""
    if os.path.exists(data_file):
        try:
            with open(data_file, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_data(data):
    """Save time entries to local storage."""
    with open(data_file, 'w') as f:
        json.dump(data, f, indent=2)

@click.command()
@click.option('--list', is_flag=True, help='List all time entries')
@click.argument('entry', nargs=3, type=str, metavar='PROJECT START END')
def cli(list, entry):
    """Main entry point for the CLI."""
    if list:
        entries = load_data()
        if not entries:
            click.echo("No entries found.")
        else:
            click.echo("--- Time Entries ---")
            for e in entries:
                click.echo(f"- {e.get('project')}: {e.get('duration')} ({e.get('date')})")
    elif entry:
        project, start, end = entry
        entry_data = {
            "project": project,
            "start": start,
            "end": end,
            "date": datetime.now().strftime('%Y-%m-%d')
        }
        data = load_data()
        data.append(entry_data)
        save_data(data)
        click.echo(f"Entry added for project: {project}")

if __name__ == '__main__':
    cli()