import pytest
import os
from click.testing import CliRunner
from time_tracker import cli

data_file = "time_tracker_data.json"

runner = CliRunner()

def test_add_entry():
    """Test adding a new time entry."""
    # Ensure clean state
    if os.path.exists(data_file):
        os.remove(data_file)

    # Test help
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert 'Time Tracker' in result.output

    # Test add command
    result = runner.invoke(cli, ['add', 'TestProject', '10:00', '11:00'])
    assert result.exit_code == 0
    assert "Entry added" in result.output
    assert os.path.exists(data_file)

def test_list_entries():
    """Test listing all entries."""
    # Clean state first
    if os.path.exists(data_file):
        os.remove(data_file)

    # Add an entry
    runner.invoke(cli, ['add', 'ProjectA', '09:00', '10:00'])

    # List entries
    result = runner.invoke(cli, ['--list'])
    assert result.exit_code == 0
    assert "ProjectA" in result.output
    assert "--- Time Entries ---" in result.output

def test_help_flag():
    """Test that the --help flag works."""
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert '--help' in result.output
    assert 'List all time entries' in result.output
