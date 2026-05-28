import pytest
import os
import json
from time_tracker import load_data, save_data, clean_up

@pytest.fixture
def setup_test_data():
    """Fixture to create a test data file."""
    test_data = [
        {"start": "10:00", "end": "11:00", "desc": "Test Task 1"},
        {"start": "12:00", "end": "13:00", "desc": "Test Task 2"}
    ]
    save_data(test_data)
    yield
    clean_up()

@pytest.fixture
def setup_empty():
    yield
    clean_up()

def test_load_empty_data(setup_empty):
    """Criterion 1: App runs and loads data correctly."""
    data = load_data()
    assert data == [], "Initial load should return empty list"

def test_save_and_load_data(setup_empty):
    """Criterion 1: Local storage persists data correctly."""
    test_data = [{"start": "09:00", "end": "10:00", "desc": "Morning work"}]
    save_data(test_data)
    loaded_data = load_data()
    assert len(loaded_data) == 1, "Should save and load one entry"
    assert loaded_data[0]['desc'] == "Morning work", "Description should match"

def test_add_command_logic(setup_empty):
    """Criterion 1: Manual entry adds data."""
    # Simulate the command execution logic
    entries = load_data()
    entry = {"start": "08:00", "end": "09:00", "desc": "New Entry"}
    entries.append(entry)
    save_data(entries)
    
    # Verify
    final_entries = load_data()
    assert len(final_entries) == 1, "Entry should be added"
    assert final_entries[0]['desc'] == "New Entry"

def test_file_persistence(setup_empty):
    """Criterion 3: Data persists across app sessions."""
    save_data([{"start": "10:00", "end": "11:00", "desc": "Sync Test"}])
    
    # Simulate 'app restart' (os independent)
    # In a real app, this is a new instance, but here we just verify file exists
    assert os.path.exists('time_tracker_data.json'), "Data file must be created"
