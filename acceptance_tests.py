import unittest
import json
import sys
import os

# Add current directory to path to import the module
sys.path.insert(0, '/workspace/projects/ios-app-time-tracker')

# Mock the module before importing
from unittest.mock import patch, MagicMock, call

# Mock the module to avoid path issues
class MockTimeTracker:
    DATA_FILE = "time_tracker.json"
    
    def __init__(self):
        self.data = {"projects": [], "logs": []}
    
    def load_data(self):
        return self.data
    
    def save_data(self, data):
        self.data = data

# Patch the module imports
sys.modules['time_tracker'] = MockTimeTracker

from time_tracker import main

class TestTimeTrackerCLI(unittest.TestCase):
    
    @patch('sys.argv')
    @patch('builtins.open', create=True)
    def test_start_timer(self, mock_open, mock_argv):
        """Test that --start flag creates a new log entry."""
        mock_argv = ['time_tracker', '--start', 'ProjectA']
        
        # Mock json.load to return empty data initially
        # Mock json.dump to capture what gets written
        with patch('json.load') as mock_load, patch('json.dump') as mock_dump:
            mock_load.return_value = {"projects": [], "logs": []}
            
            # Mock open to return a dummy file object
            mock_open.return_value.__enter__.return_value.read.side_effect = ['[]', '']
            mock_open.return_value.__exit__.return_value = None
            
            main()
            
            # Verify json.dump was called (data was written)
            mock_dump.assert_called_once()
            
    @patch('sys.argv')
    def test_list_logs(self, mock_argv):
        """Test that --list flag prints logs."""
        mock_argv = ['time_tracker', '--list']
        
        # Patch stdout to capture print output
        with patch('builtins.print') as mock_print:
            main()
            
            # Verify print was called
            mock_print.assert_called()

    @patch('sys.argv')
    @patch('builtins.open', create=True)
    def test_stop_timer(self, mock_open, mock_argv):
        """Test that --stop flag stops the last running timer."""
        mock_argv = ['time_tracker', '--stop']
        
        # Setup initial state with a running log
        initial_data = {"projects": [], "logs": [{"project": "Test", "start": "2023-01-01", "status": "running"}]}
        
        with patch('json.load') as mock_load, patch('json.dump') as mock_dump:
            mock_load.return_value = initial_data
            
            mock_open.return_value.__enter__.return_value.read.side_effect = ['[...]', '']
            mock_open.return_value.__exit__.return_value = None
            
            main()
            
            # Verify save was called
            mock_dump.assert_called_once()

if __name__ == '__main__':
    unittest.main()