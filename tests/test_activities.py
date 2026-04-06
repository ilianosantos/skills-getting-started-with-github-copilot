def test_activities_get_returns_all_activities(client):
    # Arrange
    expected_activity_names = {
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Basketball Team",
        "Soccer Club",
        "Art Studio",
        "Drama Club",
        "Robotics Club",
        "Science Club",
    }

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert set(activities.keys()) == expected_activity_names


def test_activities_get_returns_expected_activity_shape(client):
    # Arrange
    expected_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    chess_club = activities["Chess Club"]
    assert set(chess_club.keys()) == expected_keys
    assert isinstance(chess_club["participants"], list)
    assert "michael@mergington.edu" in chess_club["participants"]
