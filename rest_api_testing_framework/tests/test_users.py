import os


def test_register_user_with_existing_email(notes_service, email, password):
    existing_user_data = {
        "name": "NewUser",
        "email": email,
        "password": password
    }
    response = notes_service.post_users_register(existing_user_data, expected_status_code=409)
    assert response["message"] == "An account already exists with the same email address"


def test_login(notes_service, email, password):
    response = notes_service.post_users_login(email, password)
    assert response["data"]["token"] is not None


def test_login_invalid_email(notes_service, password):
    response = notes_service.post_users_login("invalid@email.com", password, expected_status_code=401)
    assert response["message"] == "Incorrect email address or password"


def test_profile_unauthenticated(notes_service):
    response = notes_service.get_users_profile(expected_status_code=401)
    assert response["message"] == "No authentication token specified in x-auth-token header"


def test_profile(authenticated_notes_service, email):
    response = authenticated_notes_service.get_users_profile()
    assert response["message"] == "Profile successful"
    assert response["data"]["email"] == email, "Email address is not correct"


def test_update_user_profile(authenticated_notes_service):
    name = os.getenv('NAME')
    phone = "1234567890",
    company = "New Company, Inc."
    response = authenticated_notes_service.patch_user_profile(name, phone, company)
    assert response.get("status") == 200
    assert "Profile updated successful" in response["message"]
    data = response.get("data", {})
    assert data.get("phone") == "1234567890"
    assert data.get("company") == "New Company, Inc."


def test_forgot_password(notes_service, email):
    response = notes_service.forgot_password(email)
    expected_message = f"Password reset link successfully sent to {email}. Please verify by clicking on the given link"
    assert response["message"] == expected_message


def test_verify_reset_password_token_with_invalid_token(authenticated_notes_service):
    invalid_token = "random_invalid_token_value"
    response = authenticated_notes_service.verify_reset_password_token(invalid_token, expected_status_code=401)
    assert response['status'] == 401
    assert "The provided password reset token is invalid or has expired" in response["message"]


def test_reset_password_with_invalid_token(authenticated_notes_service):
    invalid_token = "random_invalid_token_value"
    new_password = "NewPassword123"
    response = authenticated_notes_service.reset_password(invalid_token, new_password, expected_status_code=400)
    assert response.get("status") == 400
    assert "Token must be between 64 characters" in response.get("message")


def test_change_same_password(authenticated_notes_service, password):
    response = authenticated_notes_service.change_password(password, password, expected_status_code=400)
    assert response["status"] == 400
    assert response["message"] == "The new password should be different from the current password"


def test_change_invalid_password(authenticated_notes_service, password):
    new_password = "short"
    response = authenticated_notes_service.change_password(password, new_password, expected_status_code=400)
    assert response["status"] == 400
    assert "New password must be between 6 and 30 characters" in response["message"]


def test_logout(authenticated_notes_service):
    response = authenticated_notes_service.delete_users_logout()
    assert response["message"] == "User has been successfully logged out"


def test_delete_account(authenticated_notes_service, email):
    response = authenticated_notes_service.delete_user_account(email)
    assert response["message"] == "Account successfully deleted"
