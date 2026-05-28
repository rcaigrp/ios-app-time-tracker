import argparse
import sys
from datetime import datetime
import requests

# Mock Data for Jira API Simulation
def get_mock_projects():
    return [
        {"id": "PROJ1", "name": "JiraTime Dev"},
        {"id": "PROJ2", "name": "Client Work"}
    ]

def fetch_projects():
    """Fetch projects from Jira API. Returns list of dicts."""
    try:
        # In a real app, this would call Jira API
        # For simulation, we return mock data
        return get_mock_projects()
    except Exception as e:
        print(f"Error fetching projects: {e}")
        return []

def start_timer():
    print("Timer started at " + datetime.now().isoformat())

def stop_timer():
    print("Timer stopped at " + datetime.now().isoformat())

def list_entries():
    print("[CSV Entry] Project,Description,Hours,Date")

def main():
    parser = argparse.ArgumentParser(description='JiraTime CLI - Time Tracking Tool')
    parser.add_argument('action', choices=['start', 'stop', 'list', 'fetch-projects', 'export'])
    
    args = parser.parse_args()

    if args.action == 'fetch-projects':
        projects = fetch_projects()
        for p in projects:
            print(f"- {p['name']} ({p['id']})")
    
    elif args.action == 'start':
        start_timer()
    
    elif args.action == 'stop':
        stop_timer()
    
    elif args.action == 'list':
        list_entries()

if __name__ == '__main__':
    main()
