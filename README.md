# ios-app-time-tracker

A native iOS application for tracking time spent on development projects.

## Features

- **Main Dashboard**: Displays active timer and project list
- **Manual Time Entry**: Create custom project entries with start/stop functionality
- **Jira Integration**: Settings screen for Jira API credentials (base URL, API token)
- **Automatic Project Fetching**: Retrieve projects from Jira API
- **Local Storage**: Persist time logs locally on device
- **Summary/Export**: Generate reports and export functionality

## Technical Approach

This project simulates an iOS app using Python CLI tools since direct iOS development is not possible in containerized environment. The implementation will focus on core functionality:

1. Command-line interface for all operations
2. Mock Jira API integration with rate limiting
3. Local data storage simulation
4. Export functionality to CSV/JSON

## Requirements

- Python 3.8+
- No external dependencies (except standard library)

## Usage

```bash
python time_tracker.py --help
```

## Testing

Run acceptance tests:

```bash
pytest acceptance_tests.py -v
```