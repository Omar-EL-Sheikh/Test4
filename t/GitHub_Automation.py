import requests
import os

def generate_readme(title, description, languages, written_in, hardware, additional_sections=None):
    readme_content = f"# {title}\n\n"

    # Description section
    readme_content += "## Description\n"
    readme_content += f"{description}\n\n"

    # Languages section
    readme_content += "## Languages\n"
    readme_content += f"The project is primarily written in {languages}.\n\n"

    # Hardware section
    readme_content += "## Hardware Implementation and Target MCU\n"
    readme_content += f"{hardware}\n\n"

    # Additional sections
    if additional_sections:
        for section_title, section_content in additional_sections.items():
            readme_content += f"## {section_title}\n{section_content}\n\n"

    return readme_content

def save_to_readme(content, filename="README.md"):
    with open(filename, "w", encoding="utf-8") as readme_file:
        readme_file.write(content)


# Example usage
title = "Test-Test"
description = "A brief description of my awesome project."
languages = "Python, JavaScript"
written_in = "Python"
hardware = "Arduino Uno"
additional_sections = {
    "Usage": "Provide instructions on how to use the project.",
    "Contributing": "Explain how others can contribute to the project.",
    "License": "Specify the project's license.",
}

readme_content = generate_readme(title, description, languages, written_in, hardware, additional_sections)

# Save the generated content to a README.md file
save_to_readme(readme_content)

def create_github_repo(repo_name, github_token):
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": repo_name,
        "private": False,
        "auto_init": True
    }

    response = requests.post("https://api.github.com/user/repos", headers=headers, json=data)

    if response.status_code == 201:
        print(f"GitHub repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create GitHub repository. Status code: {response.status_code}")
        print(response.text)


# GitHub authentication token - replace with your personal access token
github_token = "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"

# Create a GitHub repository with the same project name
create_github_repo(title, github_token)

# Assuming all files in the current directory need to be added
# This assumes you have Git installed and configured on your machine
os.system("git init")
os.system("git add .")
os.system("git commit -m 'Initial commit'")
os.system(f"git remote add origin https://github.com/Omar-EL-Sheikh/{title}.git")  # replace YOUR_USERNAME
os.system(f"git push -u origin master -v -u {github_token}")