# The Hive Bulk Cleaner

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
2. Run the script using Python:
   ```bash
   python3 thehive_bulk_cleaner.py
   ```

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

## Disclaimer

This script was created by me as an independent developer and is not associated with or endorsed by [The Hive Project](https://strangebee.com/thehive/) or its developers. The script is provided "as-is" without any representations or warranties, express or implied. I take no responsibility for any damage or issues that may arise from using this script with your The Hive installation. All API information utilized in this script was retrieved from the official documentation at [The Hive API Documentation](https://docs.strangebee.com/thehive/api-docs/)

## License

This script is licensed under the MIT License, which allows you to freely use, modify, and distribute the script. However, please review and understand the code before using it in a production environment, as it is provided "as-is" without any warranties.
