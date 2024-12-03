import requests
import json

def create_uptime_check(url, name, interval=60):
  """
  Creates an uptime check in Kuma.

  Args:
    url: The URL to monitor.
    name: The name of the uptime check.
    interval: The check interval in seconds (default: 60).
  """

  kuma_api_url = "http://localhost:5681/v1/config/upstreams"  # Replace with your Kuma API URL
  headers = {"Content-Type": "application/json"}

  data = {
      "name": name,
      "type": "http",
      "http": {
          "url": url,
          "interval": interval,
          "timeout": 10,  # Optional: request timeout in seconds
          "healthyThreshold": 1,  # Optional: number of consecutive successes
          "unhealthyThreshold": 3  # Optional: number of consecutive failures
      }
  }

  response = requests.post(kuma_api_url, headers=headers, data=json.dumps(data))

  if response.status_code == 201:
      print(f"Uptime check '{name}' created successfully.")
  else:
      print(f"Error creating uptime check: {response.status_code} - {response.text}")

# Example usage
create_uptime_check(url="https://www.example.com", name="example-website-check")
