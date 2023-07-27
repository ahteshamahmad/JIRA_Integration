
import requests
import os


            def get_jira_project_info(base_url, access_token):
                # Set up the headers with the OAuth 2.0 access token
                headers = {
                    "Authorization": f"Bearer {access_token}",
                    "Content-Type": "application/json"
                }

                try:
                    # Make the API request to fetch project information
                    response = requests.get(base_url, headers=headers, verify=False)

                    # Check if the request was successful (status code 200)
                    if response.status_code == 200:
                        project_info = response.json()
                        return project_info
                    else:
                        print(f"Failed to get project info. Status code: {response.status_code}")
                        return None

                except requests.exceptions.RequestException as e:
                    print(f"Error occurred: {e}")
                    return None

            if __name__ == "__main__":
                # Replace these variables with your actual values
                with open("access_token.txt", "r") as f:
                    access_token = f.read().strip()
                base_url = "https://api.atlassian.com/ex/jira/b7ca1f0f-e1f1-434a-97f8-74f5ce43b6a9/rest/api/3/issue/KAN-1"
                # access_token = os.environ.get("JIRA_ACCESS_TOKEN")
                project_info = get_jira_project_info(base_url, access_token)
                if project_info:
                    print(project_info)
                    print(".............")
                    print("Project Info:")
                    print("Project Name:", project_info.get("name"))
                    print("project id:", project_info.get("id"))
                    print("Project Key:", project_info.get("key"))
                    print("Project Description:", project_info.get("description"))
                    # Add more project information as needed
                else:
                    print("Failed to fetch project information.")
                
