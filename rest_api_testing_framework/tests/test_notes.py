import pytest


@pytest.mark.parametrize("category", ["Home", "Work", "Personal"])
def test_create_note(authenticated_notes_service, category):
    title = "Test note"
    description = "Test Description"

    response = authenticated_notes_service.post_notes(title, description, category)

    assert response["message"] == "Note successfully created"
    assert response["data"]["title"] == title
    assert response["data"]["description"] == description
    assert response["data"]["category"] == category
    assert response["data"]["id"] is not None


def test_create_note_invalid_category(authenticated_notes_service):
    title = "Test note"
    description = "Test Description"
    category = "Invalid"

    response = authenticated_notes_service.post_notes(title, description, category, expected_status_code=400)

    assert response["message"] == "Category must be one of the categories: Home, Work, Personal"


def test_get_all_notes(authenticated_notes_service, prepared_note):
    response = authenticated_notes_service.get_all_notes()
    assert response["status"] == 200
    assert "data" in response
    assert isinstance(response["data"], list)


def test_get_note_by_id(authenticated_notes_service, prepared_note):
    note_id = prepared_note["id"]
    response = authenticated_notes_service.get_note_by_id(note_id)
    assert response["status"] == 200
    assert "data" in response
    assert response["data"]["id"] == note_id


def test_get_note_by_invalid_id(authenticated_notes_service):
    invalid_note_id = "invalid_id"
    response = authenticated_notes_service.get_note_by_id(invalid_note_id, expected_status_code=400)
    assert response["status"] == 400


def test_update_note(authenticated_notes_service, prepared_note):
    note_id = prepared_note["id"]
    response = authenticated_notes_service.put_note(note_id)
    assert response.status_code == 200
    assert response.json()["message"] == "Note successfully Updated"


def test_update_the_completed_attribute(authenticated_notes_service, prepared_note):
    completed = False
    response = authenticated_notes_service.update_complete_attribute(prepared_note["id"], completed)
    assert response["message"] == "Note successfully Updated"
    assert response["data"]["completed"] == completed
    assert response["data"]["id"] == prepared_note["id"]


def test_delete_note_by_id(authenticated_notes_service, prepared_note):
    response = authenticated_notes_service.delete_note_by_id(prepared_note["id"])
    assert response["message"] == "Note successfully deleted"
