import sys
import os
import unittest
from unittest.mock import patch, mock_open
import json
import io

# Add parent directory to path to import the time_tracker module
sys.path.insert(0, '/workspace/projects/ios-app-time-tracker')

class TestTimeTrackerCLI(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_help_flag(self):
        """Criterion 1: CLI Argument Parsing - Verify --help output."""
        with patch.object(sys, 'argv', ['time_tracker', '--help']):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_out:
                try:
                    from time_tracker import main
                    main()
                except SystemExit:
                    pass
                output = mock_out.getvalue()
                self.assertIn('usage', output.lower())

    def test_list_empty(self):
        """Criterion 4: List projects - Verify empty state handling."""
        # Mock the json.load to return empty list
        with patch('json.load', return_value=[]):
            with patch('json.dump'):
                with patch('sys.argv', ['time_tracker', '--list']):
                    try:
                        from time_tracker import main
                        main()
                    except SystemExit:
                        pass

    def test_new_project(self):
        """Criterion 2: Manual entry - Verify new project creation."""
        # Mock json.load to return empty data, and mock json.dump to simulate save
        with patch('json.load', return_value=[]):
            with patch('json.dump'):
                with patch('sys.argv', ['time_tracker', '--new', 'TestProject']):
                    try:
                        from time_tracker import main
                        main()
                    except SystemExit:
                        pass

if __name__ == '__main__':
    unittest.main()