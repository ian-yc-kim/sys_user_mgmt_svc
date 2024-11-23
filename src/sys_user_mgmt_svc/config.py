"""
This module handles the configuration of the application.

It loads environment variables from the `.env` file, and can be customized
to load different configurations based on the environment (development, testing, production).

testing: used for unittests
development: used for integration tests and manual tests
production: used for production
"""

import os
from dotenv import load_dotenv

# Load environment-specific .env file
# Default is `.env.development`, but can be overridden by setting the ENVIRONMENT variable
environment = os.getenv('ENVIRONMENT', 'development')
dotenv_file = f'.env.{environment}'
load_dotenv(dotenv_file)

# Configuration class to hold the settings


class Config:
    """
    Configuration settings loaded from environment variables.
    """
    ENVIRONMENT = environment
    DEBUG = os.getenv("DEBUG", "False") == "True"
    # Add more configuration settings as needed

    # example database config: uncomment it when database is used
    # DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///:memory:")


def load_config():
    """
    Returns an instance of the Config class with the environment variables loaded.
    """
    config = Config()
    return config