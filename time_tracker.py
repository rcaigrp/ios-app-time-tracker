import json
import os
import click

DATA_FILE = "projects.json"

click.group()
def cli():
    """Simple CLI to manage time tracker projects."""
    pass

@cli.command()
@click.argument('name')
def new(name):
    """Create a new time tracker project."""
    if not name:
        click.echo("Error: Project name is required.")
        return

    # Check if file exists
    projects = []
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                projects = json.load(f)
        except (json.JSONDecodeError, IOError):
            projects = []

    # Check for duplicates
    if any(p['name'] == name for p in projects):
        click.echo(f"Error: Project '{name}' already exists.")
        return

    # Add new project
    projects.append({"name": name, "date": None})
    
    # Save to file
    with open(DATA_FILE, 'w') as f:
        json.dump(projects, f)
    
    click.echo(f"Project '{name}' created successfully.")

@cli.command()
def list_projects():
    """List all existing projects."""
    if not os.path.exists(DATA_FILE):
        click.echo("No projects found.")
        return

    with open(DATA_FILE, 'r') as f:
        projects = json.load(f)

    if not projects:
        click.echo("No projects found.")
        return

    for p in projects:
        click.echo(f"- {p['name']}")

if __name__ == '__main__':
    cli()