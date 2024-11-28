import yaml
import requests

REQUIRED_FIELDS = ["name", "repo_url", "package_name", "entry_point_group"]

def validate_plugins_yaml(file_path):
    with open(file_path, 'r') as f:
        plugins = yaml.safe_load(f)
    
    errors = []
    for plugin in plugins.get("plugins", []):
        for field in REQUIRED_FIELDS:
            if field not in plugin:
                errors.append(f"Missing required field '{field}' in plugin: {plugin.get('name', 'unknown')}")

        if "repo_url" in plugin:
            try:
                response = requests.head(plugin["repo_url"], timeout=5)
                if response.status_code >= 400:
                    errors.append(f"Invalid URL '{plugin['repo_url']}' for plugin: {plugin['name']}")
            except requests.RequestException:
                errors.append(f"URL check failed for '{plugin['repo_url']}' in plugin: {plugin['name']}")
    
    if errors:
        for error in errors:
            print(error)
        return False
    print("Validation passed!")
    return True

if __name__ == "__main__":
    import sys
    file_path = sys.argv[1] if len(sys.argv) > 1 else "plugins.yaml"
    if not validate_plugins_yaml(file_path):
        exit(1)
