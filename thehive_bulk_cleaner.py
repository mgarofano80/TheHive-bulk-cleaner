import requests

# TheHive API details
api_url = "http://thehive_url:9000/api/v1"
api_key = "thehive_superadmin_api_key"

# Set up the headers for the requests
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Function to get all alert IDs
def get_all_alert_ids():
    response = requests.post(f"{api_url}/query", headers=headers, json={"query": [{"_name": "listAlert"}]})
    if response.status_code == 200:
        return [alert['_id'] for alert in response.json()]
    else:
        print(f"Failed to retrieve alerts, status code: {response.status_code}")
        return []

# Function to get observables for an alert
def get_observables_for_alert(alert_id):
    query = {
        "query": [
            {
                "_name": "getAlert",
                "idOrName": alert_id
            },
            {
                "_name": "observables"
            }
        ]
    }
    response = requests.post(f"{api_url}/query", headers=headers, json=query)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve observables for alert {alert_id}, status code: {response.status_code}")
        return []

# Function to delete an observable by ID
def delete_observable(observable_id):
    response = requests.delete(f"{api_url}/observable/{observable_id}", headers=headers)
    return response.status_code

# Function to delete all observables in alerts
def delete_all_observables():
    alert_ids = get_all_alert_ids()
    if not alert_ids:
        print("No alerts found.")
        return
    
    for alert_id in alert_ids:
        observables = get_observables_for_alert(alert_id)
        for observable in observables:
            observable_id = observable["_id"]
            status = delete_observable(observable_id)
            if status == 204:
                print(f"Successfully deleted observable with ID: {observable_id}")
            else:
                print(f"Failed to delete observable with ID: {observable_id}, Status code: {status}")

# Function to delete all alerts
def delete_all_alerts():
    alert_ids = get_all_alert_ids()
    if not alert_ids:
        print("No alerts found.")
        return
    
    for alert_id in alert_ids:
        status = delete_alert(alert_id)
        if status == 204:
            print(f"Successfully deleted alert with ID: {alert_id}")
        else:
            print(f"Failed to delete alert with ID: {alert_id}, Status code: {status}")

# Function to delete an alert by ID
def delete_alert(alert_id):
    response = requests.delete(f"{api_url}/alert/{alert_id}?force=1", headers=headers)
    return response.status_code

# Function to get all custom tags
def get_all_custom_tags():
    query = {
        "query": [
            {
                "_name": "listTag"
            }
        ]
    }
    response = requests.post(f"{api_url}/query", headers=headers, json=query)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve custom tags, status code: {response.status_code}")
        return []

# Function to delete a tag by ID
def delete_tag(tag_id):
    response = requests.delete(f"{api_url}/tag/{tag_id}", headers=headers)
    return response.status_code

# Function to delete all custom tags
def delete_all_custom_tags():
    tags = get_all_custom_tags()
    if not tags:
        print("No custom tags found.")
        return
    
    for tag in tags:
        tag_id = tag["_id"]
        status = delete_tag(tag_id)
        if status == 204:
            print(f"Successfully deleted tag with ID: {tag_id}")
        else:
            print(f"Failed to delete tag with ID: {tag_id}, Status code: {status}")

def main():
    print("Choose an option:")
    print("1. Delete all alerts")
    print("2. Delete all custom tags")
    print("3. Delete all observables in alerts")
    choice = input("Enter 1, 2, or 3: ")
    
    if choice == '1':
        delete_all_alerts()
    elif choice == '2':
        delete_all_custom_tags()
    elif choice == '3':
        delete_all_observables()
    else:
        print("Invalid choice, exiting.")

if __name__ == "__main__":
    main()