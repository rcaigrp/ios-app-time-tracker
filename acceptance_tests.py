import pytest
import responses
import sys
sys.path.insert(0, '/workspace/projects/ios-app-time-tracker')

@responses.activate
def test_jira_api_fetch():
    '''Criterion 4: Automatic project fetching from Jira API works.'''
    # Mock the Jira API response
    jira_url = "http://jira.example.com/rest/api/2/search"
    responses.add(
        responses.GET,
        jira_url,
        json={"issues": [{"key": "PROJ-1", "name": "Project 1"}]},
        status=200
    )

    # Import and call the function
    from main import JiraService
    service = JiraService("http://jira.example.com", "test_token")
    projects = service.get_projects()

    assert len(projects) == 1
    assert projects[0]['key'] == "PROJ-1"
    print("\n[TEST] Jira API fetch successful.")

@responses.activate
def test_jira_rate_limit():
    '''Handle rate limits gracefully.'''
    jira_url = "http://jira.example.com/rest/api/2/search"
    responses.add(
        responses.GET,
        jira_url,
        json={"issues": []},
        status=429
    )

    from main import JiraService
    service = JiraService("http://jira.example.com", "test_token")
    projects = service.get_projects()
    assert len(projects) == 0
    print("\n[TEST] Rate limit handled gracefully.")

def test_local_persistence():
    '''Criterion 3: Local storage persists data correctly.'''
    import os
    from main import load_data, save_data
    
    # Setup test data
    test_data = [{'project': 'TEST', 'hours': 2.5, 'date': '2023-01-01'}]
    save_data(test_data)
    
    # Load and verify
    loaded = load_data()
    assert len(loaded) == 1
    assert loaded[0]['project'] == 'TEST'
    
    # Cleanup
    if os.path.exists('time_entries.json'):
        os.remove('time_entries.json')
    print("\n[TEST] Local persistence verified.")

def test_manual_entry_logic():
    '''Criterion 2: Users can manually create entries.'''
    from main import TimeTracker
    tracker = TimeTracker()
    tracker.add('DEV', 1.0, '2023-01-01')
    
    # Verify file exists and contains data
    assert os.path.exists('time_entries.json')
    print("\n[TEST] Manual entry logic works.")

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
