import requests
import base64
import os

# Configuration
ORG = "gh-workflows"  # Change this to your organization name
REQUIRED_FILES = ["README.md", "LICENSE"]
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Ensure this is set in your environment variables

# Headers for GitHub API requests
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def check_and_generate_files(repo):
    for file in REQUIRED_FILES:
        # Check if file exists in the repository
        response = requests.get(f"https://api.github.com/repos/{ORG}/{repo}/contents/{file}", headers=HEADERS)
        if response.status_code != 200:
            print(f"{file} is missing in {repo}. Auto-generating...")
            # Auto-generate file content
            content = f"This is an auto-generated {file}."
            encoded_content = base64.b64encode(content.encode()).decode()
            # Prepare the payload for creating the file
            payload = {
                "message": f"Auto-generate missing {file}",
                "content": encoded_content,
                "branch": "main"  # Adjust branch name as necessary
            }
            # Commit the file to the repository
            put_response = requests.put(f"https://api.github.com/repos/{ORG}/{repo}/contents/{file}", json=payload, headers=HEADERS)
            if put_response.status_code in [200, 201]:
                print(f"{file} auto-generated and committed to {repo}.")
            else:
                print(f"Failed to auto-generate {file} in {repo}.")
        else:
            print(f"{file} exists in {repo}.")

def main():
    # Fetch all repositories in the organization
    repos_response = requests.get(f"https://api.github.com/orgs/{ORG}/repos", headers=HEADERS)
    if repos_response.status_code == 200:
        repos = repos_response.json()
        for repo in repos:
            repo_name = repo["name"]
            print(f"Checking {repo_name}...")
            check_and_generate_files(repo_name)
    else:
        print("Failed to fetch repositories.")

if __name__ == "__main__":
    main()
