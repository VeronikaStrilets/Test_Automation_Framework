from typing import Dict, Any

from rest_api_testing_framework.rest.rest_client import RestClient


class NotesRest(RestClient):
    """
    Notes API service
    """
    BASE_URL = "https://practice.expandtesting.com/notes/api/"
    _token: str | None = None

    @property
    def _headers(self):
        return {"x-auth-token": self._token}

    def get_health_check(self):
        """
        Send a GET request to /health-check
        :return: response in JSON format
        """
        self._log.info("Checking health")
        response = self._get("health-check")
        return response

    def post_users_register(self, registration_data: Dict[str, Any], expected_status_code=201):
        """
        Register a new user with the provided registration data.
        :param registration_data: dictionary containing user registration data
        :param expected_status_code: expected status code
        :return: response from the API
        """
        path = "users/register"
        response = self._post(path, json=registration_data, expected_status_code=expected_status_code)
        return response

    def post_users_login(self, email=None, password=None, expected_status_code=200):
        """
        Send a POST request to /users/login
        :param email: email
        :param password: password
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Logging in as {email}")
        response = self._post("users/login",
                              json={"email": email, "password": password},
                              expected_status_code=expected_status_code)
        if response["status"] == 200:
            self._token = response["data"]["token"]
        return response

    def get_users_profile(self, expected_status_code=200):
        """
        Send a GET request to /users/profile
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info("Getting user profile")
        response = self._get("users/profile", expected_status_code=expected_status_code)
        return response

    def patch_user_profile(self, name=None, phone=None, company=None, expected_status_code=200):
        """
        Update user profile.
        :param name: user's name
        :param phone: user's phone
        :param company: user's company name
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"User profile was updated")
        data = {"name": name, "phone": phone, "company": company}
        response = self._patch(path="users/profile", data=data, expected_status_code=expected_status_code)
        return response

    def forgot_password(self, email, expected_status_code=200):
        """
        Initiate the password reset process for a user by providing their email.
        :param email: email of the user for whom the password reset is requested
        :param expected_status_code: expected status code
        :return: response from the API
        """
        path = "users/forgot-password"
        data = {
            "email": email
        }
        response = self._post(path, data=data, expected_status_code=expected_status_code)
        return response

    def verify_reset_password_token(self, token: str, expected_status_code=200):
        """
        Verify a reset password token.
        :param token: reset password token to verify
        :param expected_status_code: expected status code
        :return: response from the API
        """
        self._log.info("Verifying reset password token")
        data = {"token": token}
        response = self._post("users/verify-reset-password-token", json=data,
                              expected_status_code=expected_status_code)
        return response

    def reset_password(self, token: str, new_password: str, expected_status_code=200):
        """
        Reset the user's password using a reset password token.
        :param token: reset password token
        :param new_password: new password to set
        :param expected_status_code: expected status code
        :return: response from the API
        """
        self._log.info("Resetting password")
        data = {
            "token": token,
            "newPassword": new_password
        }
        response = self._post("users/reset-password", json=data, expected_status_code=expected_status_code)
        return response

    def change_password(self, current_password: str, new_password: str, expected_status_code=200):
        """
        Change user's password.
        :param current_password: current user's password
        :param new_password: new user's password
        :param expected_status_code: expected status code
        :return: response from the API
        """
        self._log.info("Changing user's password")
        data = {"currentPassword": current_password, "newPassword": new_password}
        response = self._post(
            "users/change-password", json=data, expected_status_code=expected_status_code
        )
        return response

    def delete_users_logout(self, expected_status_code=200):
        """
        Send a DELETE request to /users/logout
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info("Logging out")
        response = self._delete("users/logout", expected_status_code=expected_status_code)
        if response["status"] == 200:
            self._token = None
        return response

    def delete_user_account(self, email: str):
        """
        Delete a user account by email.
        :param email: email address associated with the user account to be deleted
        :return: response from the API
        """
        self._log.info(f"Account {email} has been deleted")
        response = self._delete(path="users/delete-account", headers=self._headers)
        return response

    def post_notes(self, title=None, description=None, category=None, expected_status_code=200):
        """
        Send a POST request to /notes
        :param title: title of the note
        :param description: description of the note
        :param category: category of the note (Home, Work, Personal)
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Creating note with title: {title}")
        response = self._post("notes",
                              data={"title": title, "description": description, "category": category},
                              expected_status_code=expected_status_code)
        return response

    def get_all_notes(self):
        """
        Retrieve a list of all notes.
        :return: response from the API containing a list of notes.
        """
        self._log.info(f"Retrieve a list of notes")
        response = self._get(path="notes", headers=self._headers)
        return response

    def get_note_by_id(self, note_id: str = None, expected_status_code: int = 200) -> Any:
        """
        Retrieve a note by its ID.
        :param note_id: ID of the note to retrieve
        :param expected_status_code: expected status code
        :return: response from the API
        """
        self._log.info(f"Retrieve note by {note_id}")
        response = self._get(path=f"notes/{note_id}", expected_status_code=expected_status_code)
        return response

    def put_note(self, note_id=None):
        """
        Update a note with the specified ID.
        :param note_id: ID of the note to update
        :return: response from the API
        """
        self._log.info(f"Update a note with id={note_id}")
        data = {
            "id": note_id,
            "title": "Some new test",
            "description": "Additional information",
            "completed": "false",
            "category": "Home"
        }
        response = self._put(path=f"notes/{note_id}", data=data, header=self._headers)
        return response

    def update_complete_attribute(self, note_id=None, completed=None, expected_status_code=200):
        """
        Send a PATCH request to /notes/{id}
        :param note_id: note's id
        :param completed: note's status, can be Tru or False
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Updating status of note with id: {note_id}")
        response = self._patch(
            f"notes/{note_id}",
            json={"completed": completed},
            expected_status_code=expected_status_code,
        )
        return response

    def delete_note_by_id(self, note_id=None, expected_status_code=200):
        """
        Send a DELETE request to /notes/{note_id}
        :param note_id: id of the note
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Deleting note with id: {note_id}")
        response = self._delete(f"notes/{note_id}", expected_status_code=expected_status_code)
        return response
