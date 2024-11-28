import os
import yaml
import requests

# Change to the directory of the script to ensure relative paths work
os.chdir(os.path.dirname(os.path.abspath(__file__)))

REQUIRED_FIELDS = ["name", "repo", "pypi", "author", "description"]

def validate_plugins_yaml(file_path):
    """
    Validate the structure and URLs in a plugins.yaml file.
    """
    with open(file_path, 'r') as f:
        plugins = yaml.safe_load(f)

    errors = []

    for category, plugin_list in plugins.items():
        if not isinstance(plugin_list, list):
            errors.append(f"Category '{category}' must contain a list of plugins.")
            continue

        for plugin in plugin_list:
            for field in REQUIRED_FIELDS:
                if field not in plugin:
                    errors.append(
                        f"Missing required field '{field}' in plugin: {plugin.get('name', 'unknown')} under category '{category}'"
                    )

            # Validate repo URL
            if "repo" in plugin:
                try:
                    response = requests.head(plugin["repo"], timeout=5)
                    if response.status_code >= 400:
                        errors.append(f"Invalid repo URL '{plugin['repo']}' for plugin: {plugin['name']} under category '{category}'")
                except requests.RequestException:
                    errors.append(f"Repo URL check failed for '{plugin['repo']}' in plugin: {plugin['name']} under category '{category}'")

            # Validate PyPI URL
            if "pypi" in plugin:
                try:
                    response = requests.head(plugin["pypi"], timeout=5)
                    if response.status_code >= 400:
                        errors.append(f"Invalid PyPI URL '{plugin['pypi']}' for plugin: {plugin['name']} under category '{category}'")
                except requests.RequestException:
                    errors.append(f"PyPI URL check failed for '{plugin['pypi']}' in plugin: {plugin['name']} under category '{category}'")

    if errors:
        for error in errors:
            print(error)
        return False

    print("Validation passed!")
    return True

if __name__ == "__main__":
    import sys
    file_path = sys.argv[1] if len(sys.argv) > 1 else "plugins.yaml"
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found!")
        exit(1)
    if not validate_plugins_yaml(file_path):
        exit(1)
