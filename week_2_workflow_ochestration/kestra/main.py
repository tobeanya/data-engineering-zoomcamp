import requests
import kestra

r = requests.get("https://api.github.com")
print(r.status_code)


URL = "https://api.github.com/repos/kestra-io/kestra"
response = requests.get(URL)
gh_stars = response.json().get("stargazers_count")
sub = response.json()["subscribers_count"]

print(f"Kestra GitHub stars: {gh_stars}")
print(f"Kestra GitHub subscribers: {sub}")

import sys
import subprocess
import importlib

def ensure_installed(module_name: str, pip_name: str | None = None):
    try:
        importlib.import_module(module_name)
    except ModuleNotFoundError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name or module_name])

# install kestra package if missing 
ensure_installed("kestra", "kestra-python-sdk")

