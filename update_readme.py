import os
import yaml
import re

# Change to the directory of the script to ensure relative paths work
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Function to update the README file
def update_readme():
    # Load the plugins.yaml content
    with open("plugins.yaml", "r") as f:
        plugins_data = yaml.safe_load(f)

    # Prepare the list of extractors and loaders
    extractors = []
    loaders = []

    # Extract the extractor and loader information
    for extractor in plugins_data.get("extractors", []):
        extractors.append(f"- [{extractor['name']}]({extractor['repo']})")

    for loader in plugins_data.get("loaders", []):
        loaders.append(f"- [{loader['name']}]({loader['repo']})")

    # Read the README.md template content
    readme_path = "README.md"
    with open(readme_path, "r") as f:
        readme_content = f.read()

    # Prepare the dynamic sections for Extractors and Loaders
    extractors_section = "\n".join(extractors) if extractors else "No extractors available."
    loaders_section = "\n".join(loaders) if loaders else "No loaders available."

    # Use regex to replace the "Extractors" section
    updated_readme = re.sub(
        r"#### Extractors.*?---",  # Matches everything from "#### Extractors" to the first "---"
        f"#### Extractors\n{extractors_section}\n---",  # Replace with new extractors section
        readme_content, 
        flags=re.DOTALL
    )

    # Use regex to replace the "Loaders" section
    updated_readme = re.sub(
        r"#### Loaders.*?---",  # Matches everything from "#### Loaders" to the first "---"
        f"#### Loaders\n{loaders_section}\n---",  # Replace with new loaders section
        updated_readme,
        flags=re.DOTALL
    )

    # Write the updated content back to README.md
    with open(readme_path, "w") as f:
        f.write(updated_readme)

    print("README.md updated successfully!")

if __name__ == "__main__":
    update_readme()
