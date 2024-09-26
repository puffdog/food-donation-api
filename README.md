# Food Donation API

The **Food Donation API** is a simple and efficient platform designed to help individuals and organizations donate surplus food to those in need. By facilitating food donations, the API aims to reduce food waste and provide food to NGOs and communities that need it.

## Features
- **Donate Food**: Users can donate surplus food through the API.
- **View Donations**: List all available food donations.
- **Manage Donations**: Edit or delete existing donations easily.

## Technologies Used
- **Python**
- **Flask** (Framework)
- **SQLite** (Database)
- **Git** (Version Control)

## API Endpoints
1. **Welcome**
   - **URL**: `/`
   - **Method**: `GET`
   - **Description**: Returns a welcome message from the API.

2. **List Donations**
   - **URL**: `/donations`
   - **Method**: `GET`
   - **Description**: Fetches all available donations in the system.

3. **Create Donation**
   - **URL**: `/donations`
   - **Method**: `POST`
   - **Description**: Allows users to submit a new food donation.
   - **Request Body Example**:
     ```json
     {
       "food_item": "Rice",
       "quantity": 50,
       "expiration_date": "2024-12-15"
     }
     ```

4. **Update Donation**
   - **URL**: `/donations/<id>`
   - **Method**: `PUT`
   - **Description**: Updates an existing donation by its ID.
   - **Request Body Example**:
     ```json
     {
       "food_item": "Pasta",
       "quantity": 100,
       "expiration_date": "2025-01-01"
     }
     ```

5. **Delete Donation**
   - **URL**: `/donations/<id>`
   - **Method**: `DELETE`
   - **Description**: Deletes a food donation by its ID.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/puffdog/food-donation-api.git
   cd food-donation-api
   ```

2. **Install dependencies**: 
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the API**: 
   Open your browser and go to `http://127.0.0.1:5000` to view the welcome message.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the **MIT License**. See the LICENSE file for more details.

## Contact
For any inquiries, please contact:
- **Author**: Mabasa Gift
```

### Further Reading:
- [Flask Official Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Python Requests Documentation](https://docs.python-requests.org/en/latest/)

This README provides all the key details in one page. Let me know if you need any other details or further assistance!
