# Food Donation API Documentation

## Overview
This API facilitates the donation of food to NGOs and individuals in need. It allows users to register, login, and manage food donations efficiently.

## Base URL
## Endpoints

### 1. Register a User
- **Method**: `POST`
- **Endpoint**: `/register`
- **Description**: Creates a new user account.
- **Parameters**:
    - **username** (string, required): The username for the new account.
    - **password** (string, required): The password for the new account.
- **Responses**:
    - **201 Created**: User successfully created.
    - **400 Bad Request**: Missing or invalid parameters.

### 2. Login a User
- **Method**: `POST`
- **Endpoint**: `/login`
- **Description**: Authenticates a user and returns an access token.
- **Parameters**:
    - **username** (string, required): The username of the account.
    - **password** (string, required): The password of the account.
- **Responses**:
    - **200 OK**: Access token returned.
    - **401 Unauthorized**: Invalid username or password.

### 3. Create a Donation
- **Method**: `POST`
- **Endpoint**: `/donations`
- **Description**: Allows a user to create a new food donation.
- **Parameters**:
    - **food_item** (string, required): The type of food being donated.
    - **quantity** (integer, required): The amount of food being donated.
    - **location** (string, required): The location where the food can be picked up.
- **Responses**:
    - **201 Created**: Donation successfully created.
    - **400 Bad Request**: Missing or invalid parameters.

### 4. Get All Donations
- **Method**: `GET`
- **Endpoint**: `/donations`
- **Description**: Retrieves a list of all food donations.
- **Responses**:
    - **200 OK**: List of donations in JSON format.

### 5. Delete a Donation
- **Method**: `DELETE`
- **Endpoint**: `/donations/<donation_id>`
- **Description**: Deletes a specific donation by its ID.
- **Parameters**:
    - **donation_id** (string, required): The ID of the donation to delete.
- **Responses**:
    - **204 No Content**: Donation successfully deleted.
    - **404 Not Found**: Donation with specified ID does not exist.
