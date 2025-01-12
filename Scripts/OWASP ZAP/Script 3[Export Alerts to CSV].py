import requests
import csv

def export_alerts_to_csv():
    """
    Export all OWASP ZAP alerts to a CSV file.

    Returns:
    None
    """
    zap_api_url = "http://localhost:8080"
    alerts_url = f"{zap_api_url}/JSON/alert/view/alerts/"

    response = requests.get(alerts_url)
    alerts = response.json()['alerts']

    with open('zap_alerts.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Alert', 'Risk', 'URL', 'Description'])

        for alert in alerts:
            writer.writerow([alert['alert'], alert['risk'], alert['url'], alert['description']])
    
    print("Alerts exported to zap_alerts.csv")

# Example usage
export_alerts_to_csv()
