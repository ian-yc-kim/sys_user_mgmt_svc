"""
This file serves as the entry point for the application.
It contains only the initialization logic for setting up the app.
Additional functionality should be implemented elsewhere.

Main Responsibilities:
1. Load configuration settings (from environment, config files, etc.).
2. Initialize application components (e.g., database, cache, services).
3. Start the application.
"""

import logging
from sys_user_mgmt_svc.config import settings
from sys_user_mgmt_svc.app import create_app

# Set up logging for the application
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """
    Main function that initializes and starts the application.

    This function should only contain logic related to:
    - Loading configuration settings
    - Initializing services (e.g., database, cache)
    - Starting the application

    Any additional business logic should be implemented in separate modules and called from the app's routing or service layers.
    """

    # Step 1: Load configuration settings (can be environment-specific)
    config = settings
    logger.info("Configuration loaded successfully")

    # Step 2: Initialize the app with the loaded configuration
    app = create_app()
    logger.info("Application initialized successfully")

    # Step 3: Start the app (This could be a web server, CLI tool, etc.)
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    logger.info("Application started successfully")


if __name__ == "__main__":
    # Entry point for the application
    main()
