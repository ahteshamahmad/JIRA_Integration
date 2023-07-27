import requests
import os


            # Replace these with your actual client credentials from the OAuth provider
            client_id = "Wwq8AIgTXkD69jFY7B78d9vTlf6CYUg1"
            client_secret = "ATOA4L9yrz3UoZjY0KzYh28NmErwoYXvMJi0SeSilwRwkmIlU3utQ9F4Z1_hUEKKw6c71D2D611E"

            # The token endpoint URL provided by the OAuth provider
            token_endpoint = "https://auth.atlassian.com/oauth/token"

            # Request an access token using client credentials
            data = {
                "grant_type": "client_credentials",
                "client_id": client_id,
                "client_secret": client_secret
            }

            response = requests.post(token_endpoint, data=data)

            if response.status_code == 200:
                # Access token obtained successfully
                access_token = response.json()["access_token"]
                print(f"::set-env name=JIRA_ACCESS_TOKEN::{access_token}")
            else:
                print("Error obtaining access token:", response.json())
