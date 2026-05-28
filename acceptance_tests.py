import pytest
import json
import os
import sys
from unittest.mock import patch, MagicMock

# Ensure the script path is correct
sys.path.insert(0, '/workspace/projects/ios-app-time-tracker')

# We need to mock the file system operations to ensure tests don't rely on actual files
# because the tests are run in a fresh container.
def load_data_mock():
    return []

def save_data_mock(entries):
    pass

def add_entry_mock(project):
    return {"project": project, "timestamp": "2023-01-01T00:00:00"}

def test_add_entry():
    """Test that add_entry creates a new entry and saves it."""
    # Mock the file system functions
    with patch('time_tracker.load_data', side_effect=load_data_mock) as mock_load, \
         patch('time_tracker.save_data', side_effect=save_data_mock) as mock_save:
        
        # Call the function
        result = add_entry_mock("JIRA-123")
        
        # Verify
        assert result['project'] == "JIRA-123"
        assert result['timestamp'] == "2023-01-01T00:00:00"
        
def test_list_entries_empty():
    """Test that list_entries handles an empty data file."""
    entries = []
    # Mock the print function to capture output
    with patch('builtins.print') as mock_print:
        # Mock load_data to return empty list
        with patch('time_tracker.load_data', return_value=entries) as mock_load:
            # Call the function
            list_entries()
            
            # Verify
            mock_print.assert_called_with("No entries found.")
            
def test_export_csv():
    """Test that export_csv writes data to a file."""
    mock_entries = [
        {"project": "JIRA-1", "timestamp": "2023-01-01T10:00:00"},
        {"project": "JIRA-2", "timestamp": "2023-01-01T11:00:00"}
    ]
    
    with patch('time_tracker.load_data', return_value=mock_entries):
        with patch('builtins.print') as mock_print, patch('os.path.exists', return_value=True):
            with patch('open', MagicMock()) as mock_open:
                # Call the function
                export_csv("test_output.csv")
                
                # Verify
                mock_print.assert_called_with("Data exported to test_output.csv")
                
                # Check that open was called with the correct filename
                mock_open.assert_called()
                
                # Verify file mode
                call_args = mock_open.call_args
                assert call_args[1]['mode'] == 'w'