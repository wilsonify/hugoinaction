from pathlib import Path

import yaml

BASE_DIR = Path(__file__).parent.parent
YAML_FILE = BASE_DIR / "config.yaml"


def test_footer_sections():
    """Ensure all footer sections are present and consistent."""
    with open(YAML_FILE) as f:
        yaml_data = yaml.safe_load(f)
    assert set(yaml_data.keys()) == set(['menu', 'baseURL', 'languageCode', 'title', 'theme', 'params'])
    assert yaml_data["title"] == 'Acme Corporation'
