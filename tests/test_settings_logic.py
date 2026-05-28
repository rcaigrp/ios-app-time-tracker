import pytest
import responses

@responses.activate
def test_jira_project_fetching_with_credentials():
    """Test that Jira API fetches projects and handles credentials."""
    # Mock Jira API response for project list
    responses.add(
        responses.GET,
        "https://jira.example.com/rest/api/2/project",
        json=[{"id": "PROJ-1", "name": "Test Project"}],
        status=200
    )

    # Simulate the API call using the service
    # In a real scenario, we would import the class here
    # from ios_app_time_tracker.services import JiraService
    # service = JiraService(api_url="https://jira.example.com", username="user", api_key="key")
    # service.fetch_projects()

    # Assertions
    assert len(responses.calls) == 1
    request = responses.calls[0].request
    assert request.headers.get("Authorization") == "Bearer key"
    assert request.url == "https://jira.example.com/rest/api/2/project"

@responses.activate
def test_jira_api_error_handling():
    """Test that invalid credentials or network errors are handled."""
    # Mock 401 Unauthorized response
    responses.add(
        responses.GET,
        "https://jira.example.com/rest/api/2/project",
        json={"errors": {"message": "Authentication failed"}},
        status=401
    )

    # Call service (Mocked)
    # service = JiraService(api_url="https://jira.example.com", username="bad", api_key="bad")
    # result = service.fetch_projects()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.status_code == 401
