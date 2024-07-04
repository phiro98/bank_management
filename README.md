# Bank Management System

## Overview

The Bank Management System is a secure and efficient web application
built using Flask and MongoDB, designed to streamline banking operations
for customers and bankers. It provides robust features such as user
authentication, balance checks, deposits, withdrawals, and transaction
history views, all protected by JWT-based authentication. The
application follows the MVC architecture to ensure clean code separation
and maintainability, with a focus on security and error handling.
Additionally, optional banker features allow for account management and
transaction oversight, making it a comprehensive solution for modern
banking needs.

## Features

### Customer Features

-   **User Authentication**: Secure login using username and password
    with JWT-based authentication.

-   **Account Management**:

    -   Check account balance.
    -   Deposit funds.
    -   Withdraw funds.
    -   View transaction history.

### Banker Features (Optional)

-   **Account List**: Access a list of all customer accounts.
-   **Transaction History**: View transaction history of all customer
    accounts.

## Architecture

The application is structured using the MVC (Model-View-Controller)
architecture:

-   **Models**: Interact with MongoDB to perform CRUD operations and
    define data structures for users and transactions.
-   **Views**: Handle HTTP requests and responses, rendering JSON
    responses for API endpoints.
-   **Controllers**: Implement business logic for banking operations,
    validate input data, and ensure secure transactions.

## Security and Error Handling

-   **Authentication**: Secure user authentication using JWT tokens and
    password hashing.
-   **Input Validation**: Validate input data to prevent security
    vulnerabilities, ensuring proper error handling and returning
    meaningful error messages.
-   **Exception Handling**: Implement try-except blocks to handle
    exceptions gracefully and log errors for debugging and monitoring.

## Technology Stack

-   **Backend**: Flask (Python)
-   **Database**: MongoDB
-   **Authentication**: JWT (JSON Web Tokens)
-   **Security**: Password hashing, input validation, error handling

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/phiro98/bank_management.git
   cd bank-management-system
2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
4.  **Configure Environment Variables**:

  -   Create a *.env* file in the root directory.

  -   Add the following variables:

   ```makefile
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=<your_secret_key>
   MONGO_URI=<your_mongodb_uri>
   ```
5.  **Run the Application**:

    ```bash
    flask run

## Usage

-   Use Postman or a similar tool to interact with the API endpoints.
-   Securely log in to obtain a JWT token for accessing protected
    routes.
-   Perform banking operations such as checking balance, depositing, and
    withdrawing funds.

## API Endpoints

1.  **User Authentication**:
    -   *POST /auth/register*: User registration with username & password.
    -   *POST /auth/login*: User login to obtain JWT token.

2.  **Customer Operations**:

    -   *GET /balance*: Check account balance.
    -   *POST /deposit*: Deposit funds into account.
    -   *POST /withdraw*: Withdraw funds from account.
    -   *GET /transactions*: View transaction history.

3.  **Banker Operations (Optional)**:

    -   *GET /banker/accounts*: List all customer accounts.
    -   *GET /banker/transactions*: View all transaction histories.

## Future Enhancements

-   Implement frontend interface for better user experience.
-   Add more advanced features such as fund transfers between accounts.
-   Improve reporting and analytics for banking operations.











