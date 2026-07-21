#!/usr/bin/env python3
"""
GitHub Label Kurulum Scripti

Bu script, project'deki yaşam döngüsü etiketlerini GitHub reposuna yükler.
Kullanım: python scripts/setup_labels.py [owner/repo]

Gereksinimler: pip install PyGithub pyyaml
"""

import sys
import yaml
from pathlib import Path

try:
    from github import Github
except ImportError:
    print("PyGithub kurulu değil. Yükleyin: pip install PyGithub")
    sys.exit(1)


def load_labels(yaml_path: str) -> list[dict]:
    """YAML dosyasından etiketleri yükler."""
    with open(yaml_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def setup_labels(repo_name: str, token: str, yaml_path: str = ".github/labels.yml"):
    """Etiketleri GitHub reposuna yükler."""
    g = Github(token)
    repo = g.get_repo(repo_name)

    labels = load_labels(yaml_path)

    existing_labels = {label.name: label for label in repo.get_labels()}

    created = 0
    updated = 0
    skipped = 0

    for label_data in labels:
        name = label_data["name"]
        color = label_data["color"]
        description = label_data.get("description", "")

        if name in existing_labels:
            existing = existing_labels[name]
            if existing.color != color or existing.description != description:
                existing.edit(name=name, color=color, description=description)
                updated += 1
                print(f"  [GÜNCELLENDİ] {name}")
            else:
                skipped += 1
                print(f"  [ATLANDI] {name}")
        else:
            repo.create_label(name=name, color=color, description=description)
            created += 1
            print(f"  [OLUŞTURULDU] {name}")

    print(f"\nÖzet: {created} oluşturuldu, {updated} güncellendi, {skipped} atlandı")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python scripts/setup_labels.py owner/repo")
        print("Örnek: python scripts/setup_labels.py sirket/yazilim-github-ornek")
        sys.exit(1)

    repo_name = sys.argv[1]
    token = input("GitHub Token: ").strip()

    if not token:
        print("Token boş olamaz!")
        sys.exit(1)

    labels_path = Path(__file__).parent.parent / ".github" / "labels.yml"
    setup_labels(repo_name, token, str(labels_path))
