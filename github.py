import requests
import json

# GitHub username to retrieve repositories from
github_username = 'NowshadRuhan'


# 1. Go to your GitHub account settings.
# 2. Click on "Developer settings" > "Personal access tokens" > "Generate new token."
# 3. Select the required scopes (at least 'public_repo' if accessing public repositories).
# 4. Generate the token.
# Personal access token for GitHub API
access_token = 'YOUR_ACCESS_TOKEN'

# GitHub API endpoint for user's repositories
api_url = f'https://api.github.com/users/{github_username}/repos'

# Set headers with authorization using access token
headers = {
    'Authorization': f'token {access_token}',
    'Accept': 'application/vnd.github.v3+json'
}

try:
    # Send GET request to fetch repositories
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        # Extract repository names
        repositories = response.json()
        repo_names = [repo['name'] for repo in repositories]

        # Create a dictionary with repository names
        repo_dict = {"repositories": repo_names}

        # Save repository names to a JSON file
        with open('git.json', 'w') as json_file:
            json.dump(repo_dict, json_file, indent=4)

        print("Repository names saved to 'git.json' file.")
    else:
        print(f"Failed to fetch repositories. Status code: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
