# sys_user_mgmt_svc

## Database Setup

### Configuring Environment Variables

1. **.env.development**

   Update the `.env.development` file with the following environment variables:

   ```env
   DATABASE_URL=postgresql://sys_user_mgmt:c171e373-a3db@10.138.0.4:5432/sys_user_mgmt
   ```

2. **.env.testing**

   Ensure the `.env.testing` file is configured for testing purposes:

   ```env
   DATABASE_URL=sqlite:///:memory:
   ```

### Installing Dependencies

Install the required dependencies using [Poetry](https://python-poetry.org/):

```bash
dpoetry install
```

### Setting Up the Database

1. **Run Alembic Migrations**

   Apply the database schema migrations using Alembic:

   ```bash
   poetry run alembic upgrade head
   ```

2. **Verify Database Setup**

   Ensure that the PostgreSQL database is set up correctly by checking the migrations and the database schema.

## Running the Service

1. **Start the Service**

   ```bash
   poetry run sys_user_mgmt_svc
   ```

2. **Running Tests**

   Execute unit tests using pytest:

   ```bash
   poetry run pytest
   ```

## Additional Information

- **Repository:** [sys_user_mgmt_svc](https://github.com/ian-yc-kim/sys_user_mgmt_svc.git)
- **Database:** PostgreSQL (`sys_user_mgmt`)
- **Environment Configuration:** Environment variables are managed using `.env` files. Do not commit `.env.development` or `.env.testing` to the repository.

## Contribution Guidelines

Please follow the standard [PEP 8](https://pep8.org/) style guidelines and ensure all new code is well-documented and tested.
