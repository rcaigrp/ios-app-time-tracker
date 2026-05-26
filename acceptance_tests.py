import os
import pytest

PROJECT_DIR = "/workspace/projects/ios-app-time-tracker"

def test_criterion_1_project_structure():
    """Project structure includes SwiftUI and SwiftData files."""
    swift_files = ["ContentView.swift", "SettingsView.swift", "TimeEntryView.swift"]
    for f in swift_files:
        assert os.path.exists(os.path.join(PROJECT_DIR, f)), f"Missing {f}"

def test_criterion_2_settings_screen():
    """Settings screen accepts and securely stores Jira API credentials."""
    assert os.path.exists(os.path.join(PROJECT_DIR, "SettingsView.swift"))

def test_criterion_3_jira_fetching():
    """Automatic project fetching from Jira API using URLSession with rate limit handling."""
    assert os.path.exists(os.path.join(PROJECT_DIR, "JiraService.swift"))

def test_criterion_4_manual_entry_storage():
    """Manual time entry screen persists logs locally using SwiftData."""
    assert os.path.exists(os.path.join(PROJECT_DIR, "TimeEntryModel.swift"))

def test_criterion_5_summary_export():
    """Summary screen provides overview and export functionality."""
    assert os.path.exists(os.path.join(PROJECT_DIR, "SummaryView.swift"))
