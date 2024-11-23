# Setup Database Schema for User Management Service

### Core Logic
- Define the PostgreSQL database schema for the User Management Service.
- Create tables: `users`, `tokens` (if token blacklisting is implemented).
- Define relationships and constraints (e.g., unique email).

### Implementation Requirements
- Use SqlAlchemy to define ORM models for `users` and `tokens`.
- Implement Alembic migration scripts to create the initial database schema.
- Ensure all fields have appropriate data types and constraints.
- Integrate the database module with the FastAPI application.

### Success Criteria
- Database tables are created as per the defined schema.
- Migration scripts run without errors and reflect the intended schema changes.
- ORM models correctly represent the database tables.
- Database connection is established successfully within the application.


# Implement User Signup API Endpoint

### Core Logic
- Allow users to create an account by providing email, full name, country, state/province, and a secure password.
- Validate that the email is not already registered.
- Ensure the password meets security requirements.
- Save the new user with `is_active` set to false.
- Initiate email verification process.

### Implementation Requirements
- Define the `POST /signup` API endpoint using FastAPI.
- Implement input validation for all required fields.
- Hash the user's password securely before storing.
- Use SqlAlchemy to interact with the PostgreSQL database.
- Integrate with the Email Service Module to send verification emails.

### Success Criteria
- API successfully creates a new user with valid input.
- Duplicate emails are rejected with appropriate error messages.
- Passwords that do not meet security criteria are rejected.
- Verification email is sent upon successful signup.


# Implement Email Verification for User Signup

### Core Logic
- Send a verification email to the user after successful signup.
- Include a unique verification token/link in the email.
- Activate the user's account upon successful verification.
- Handle token expiration and invalidation.

### Implementation Requirements
- Create a mechanism to generate and store verification tokens.
- Define an API endpoint (e.g., `GET /verify-email`) to handle verification requests.
- Integrate with the Email Service Module to send verification emails.
- Update the user's `is_active` status upon successful verification.
- Implement error handling for expired or invalid tokens.

### Success Criteria
- Verification emails are sent with correct token/link.
- Users can successfully verify their email and activate their account.
- Invalid or expired tokens are handled gracefully with appropriate feedback.


# Implement User Login API Endpoint

### Core Logic
- Allow users to log in by providing their registered email and password.
- Authenticate user credentials.
- Issue a JWT token upon successful authentication.
- Handle failed login attempts and provide appropriate feedback.

### Implementation Requirements
- Define the `POST /login` API endpoint using FastAPI.
- Implement input validation for email and password.
- Use SqlAlchemy to retrieve user information from the database.
- Verify the provided password against the stored password hash.
- Generate JWT tokens for authenticated sessions.
- Implement rate limiting to prevent brute-force attacks.

### Success Criteria
- Users can successfully log in with valid credentials and receive a JWT token.
- Invalid credentials are rejected with clear error messages.
- Rate limiting effectively restricts excessive login attempts.


# Implement User Logout API Endpoint

### Core Logic
- Allow users to securely log out by invalidating their active JWT tokens.
- Ensure that logged-out tokens cannot be used for further authentication.

### Implementation Requirements
- Define the `POST /logout` API endpoint using FastAPI.
- Implement a mechanism to invalidate JWT tokens (e.g., token blacklisting).
- Update the token management system to recognize and reject invalidated tokens.
- Ensure that the logout process securely terminates the user session.

### Success Criteria
- Users can successfully log out, and their JWT tokens are invalidated.
- Invalidated tokens are rejected in subsequent authentication attempts.
- The logout process does not introduce security vulnerabilities.


# Implement Account Termination API Endpoint

### Core Logic
- Allow users to terminate their accounts, preventing further logins.
- Mark the user's account as terminated in the database.
- Ensure that terminated accounts cannot be reactivated without proper authorization.

### Implementation Requirements
- Define the `POST /terminate` API endpoint using FastAPI.
- Implement input validation to confirm account termination requests.
- Update the user's `is_terminated` status in the PostgreSQL database.
- Ensure that terminated accounts are excluded from authentication processes.
- Handle any necessary cleanup or data archiving related to account termination.

### Success Criteria
- Users can successfully terminate their accounts through the API.
- Terminated accounts are marked appropriately and cannot be used to log in.
- The termination process handles all edge cases and maintains data integrity.


# Implement Password Reset Request API Endpoint

### Core Logic
- Allow users to request a password reset by providing their registered email address.
- Send a password reset link to the user's email.
- Generate a secure, single-use reset token with an expiration time.

### Implementation Requirements
- Define the `POST /password-reset-request` API endpoint using FastAPI.
- Implement input validation for the email address.
- Generate and store password reset tokens securely.
- Integrate with the Email Service Module to send password reset emails.
- Ensure that reset tokens are single-use and have a limited validity period.

### Success Criteria
- Users can successfully request a password reset with a valid email address.
- Password reset emails are sent with correct reset tokens/links.
- Reset tokens expire after the defined period and cannot be reused.


# Implement Password Reset API Endpoint

### Core Logic
- Allow users to reset their password using the reset token provided in the password reset email.
- Validate the reset token and ensure it has not expired or been used.
- Update the user's password in the database with the new secure hash.

### Implementation Requirements
- Define the `POST /password-reset` API endpoint using FastAPI.
- Implement input validation for the reset token and new password.
- Verify the authenticity and validity of the reset token.
- Hash the new password securely before updating it in the database.
- Invalidate the reset token after successful password reset.

### Success Criteria
- Users can successfully reset their passwords with a valid reset token.
- Invalid or expired reset tokens are rejected with appropriate error messages.
- Passwords are updated securely and stored as hashed values in the database.
