import argparse
import json
import os
import sys
from datetime import datetime

DATA_FILE = "time_tracker.json"

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"projects": [], "logs": []}
    return {"projects": [], "logs": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def main():
    parser = argparse.ArgumentParser(description="Jira Time Tracker CLI")
    parser.add_argument("--start", help="Start timer for project")
    parser.add_argument("--stop", help="Stop timer")
    parser.add_argument("--list", action="store_true", help="List logs")
    parser.add_argument("--config", help="Set Jira URL and Token")
    parser.add_argument("--sync", action="store_true", help="Sync to Jira")

    args = parser.parse_args()

    data = load_data()

    if args.start:
        entry = {"project": args.start, "start": datetime.now().isoformat(), "status": "running"}
        data["logs"].append(entry)
        save_data(data)
        print(f"Timer started for {args.start}")
    elif args.stop:
        # Find last running log and stop it
        for log in reversed(data["logs"]):
            if log.get("status") == "running":
                log["end"] = datetime.now().isoformat()
                log["status"] = "stopped"
                break
        save_data(data)
        print("Timer stopped.")
    elif args.list:
        print(json.dumps(data["logs"], indent=2))
    elif args.config:
        print(f"Config set for Jira API")
    elif args.sync:
        print("Syncing with Jira API...")

if __name__ == "__main__":
    main()