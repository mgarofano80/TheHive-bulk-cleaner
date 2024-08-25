# The Hive Management Script

This Python script provides a set of functions to manage alerts, observables, and custom tags within The Hive, an open-source incident response platform. The script allows you to delete all alerts, all custom tags, or all observables associated with alerts in bulk.

## Prerequisites

Before using the script, ensure you have the following:

1. **Python 3.x** installed on your system.
2. The `requests` library. If not installed, you can add it using:
   ```bash
   pip install requests
   ```
3. Access to The Hive API with sufficient permissions to delete alerts, observables, and tags.

## Configuration

Update the following variables in the script to match your The Hive instance:

- `api_url`: The base URL of your The Hive instance.
- `api_key`: The API key with super admin permissions.

## Usage

The script provides three main functionalities:

1. **Delete all alerts**: Removes all alerts from The Hive.
2. **Delete all custom tags**: Removes all custom tags from The Hive.
3. **Delete all observables in alerts**: Removes all observables associated with each alert.

### Running the Script

To run the script:

1. Clone or download the script to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using Python:
   ```bash
   python script_name.py
   ```
   Replace `script_name.py` with the actual name of your script file.

### Options

When the script is executed, you will be prompted to choose one of the following options:

1. **Delete all alerts**: Deletes all alerts in The Hive.
2. **Delete all custom tags**: Deletes all custom tags in The Hive.
3. **Delete all observables in alerts**: Deletes all observables associated with each alert, and then deletes the alerts.

## Functions Overview

- **get_all_alert_ids**: Retrieves the IDs of all alerts in The Hive.
- **get_observables_for_alert**: Retrieves all observables for a specific alert.
- **delete_observable**: Deletes a specific observable by its ID.
- **delete_all_observables**: Deletes all observables associated with each alert.
- **delete_alert**: Deletes a specific alert by its ID.
- **delete_all_alerts**: Deletes all alerts in The Hive.
- **get_all_custom_tags**: Retrieves all custom tags in The Hive.
- **delete_tag**: Deletes a specific tag by its ID.
- **delete_all_custom_tags**: Deletes all custom tags in The Hive.

## Logging

The script prints out messages to the console indicating the success or failure of each deletion operation. If an operation fails, the status code returned by The Hive API is displayed to help diagnose the issue.

## License

This script is open-source and can be modified as per your needs. Make sure to review and understand the code before running it in a production environment.
