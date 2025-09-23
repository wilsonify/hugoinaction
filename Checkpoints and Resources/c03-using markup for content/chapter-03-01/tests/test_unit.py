import os
import re
import subprocess
from pathlib import Path
from xml.etree import ElementTree as ET

BASE_DIR = Path(__file__).resolve().parent.parent
PUBLIC_DIR = BASE_DIR / "public"


def build_site():
    """Run Hugo build before tests (only once)."""
    if PUBLIC_DIR.exists():
        subprocess.run(["make", "clean"], cwd=BASE_DIR, check=True)
    subprocess.run(["make", "build"], cwd=BASE_DIR, check=True)


def test_hugo_build():
    """Ensure Hugo builds the site successfully."""
    result = subprocess.run(["make", "build"], cwd=BASE_DIR, capture_output=True)
    assert result.returncode == 0, f"Build failed: {result.stderr.decode()}"


def test_config_yaml_exists():
    """Verify config file contains required fields."""
    config_file = BASE_DIR / "config.yaml"
    assert config_file.exists()

    content = config_file.read_text()
    assert "baseURL:" in content
    assert "title:" in content
    


def test_rss_feed_titles():
    """Ensure RSS feeds have correct titles."""
    rss_files = [
        PUBLIC_DIR / "index.xml",
        PUBLIC_DIR / "tags/index.xml",
        PUBLIC_DIR / "categories/index.xml",
    ]
    for f in rss_files:
        assert f.exists()
        tree = ET.parse(f)
        title = tree.find(".//channel/title").text
        assert "My New Hugo Site" in title or "Tags" in title or "Categories" in title


def test_robots_txt():
    """Ensure robots.txt disallows all crawling (for now)."""
    robots = PUBLIC_DIR / "robots.txt"
    assert robots.exists()
    content = robots.read_text().strip()
    assert "User-agent: *" in content
    assert "Disallow: /" in content
