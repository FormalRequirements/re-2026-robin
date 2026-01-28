# test_pegs_structure.py
import re
from pathlib import Path
import pytest

# ============================================================
# Configuration
# ============================================================

BASE_DIR = Path(__file__).parent
MARKDOWN_FILE = BASE_DIR / "REQUIREMENTS.md"

PEGS_NAMES = ["PROJECT", "ENVIRONMENT", "GOALS", "SYSTEM"]

PEGS_HEADER_PATTERN = re.compile(
    r"^##\s+(\d+)\.\s+(PROJECT|ENVIRONMENT|GOALS|SYSTEM)(?:\s*\(.*\))?\s*$",
    re.MULTILINE
)


# ============================================================
# Lecture
# ============================================================

def read_markdown(path: Path) -> str:
    """Lit le contenu du Markdown"""
    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {path.resolve()}")
    return path.read_text(encoding="utf-8")


# ============================================================
# Analyse PEGS
# ============================================================

def extract_pegs_headers(md: str) -> list[tuple[int, str]]:
    """
    Retourne [(numero, nom)]
    ex: [(1, "PROJECT"), (2, "ENVIRONMENT")]
    """
    return [(int(num), name) for num, name in PEGS_HEADER_PATTERN.findall(md)]


def validate_pegs_structure(md: str) -> list[str]:
    """
    Vérifie la structure PEGS et retourne une liste d'erreurs
    """
    errors = []
    found = extract_pegs_headers(md)

    if not found:
        return ["Aucune section PEGS détectée (## X. NAME)"]

    found_numbers = [num for num, _ in found]
    found_names = [name for _, name in found]

    # 1) Présence exacte des 4 PEGS
    missing = set(PEGS_NAMES) - set(found_names)
    if missing:
        errors.append("Sections PEGS manquantes : " + ", ".join(sorted(missing)))

    # 2) Unicité
    for name in PEGS_NAMES:
        if found_names.count(name) > 1:
            errors.append(f"Section PEGS dupliquée : {name}")

    # 3) Ordre PEGS strict
    if found_names != PEGS_NAMES:
        errors.append(
            "Ordre PEGS invalide : "
            + " -> ".join(found_names)
            + " (attendu "
            + " -> ".join(PEGS_NAMES)
            + ")"
        )

    # 4) Numéros strictement croissants
    if found_numbers != sorted(found_numbers):
        errors.append("Les numéros de sections PEGS doivent être strictement croissants")

    # 5) Pas d'autres titres H2
    all_h2 = re.findall(r"^##\s+(.+)$", md, re.MULTILINE)
    if len(all_h2) != len(found):
        errors.append("Des titres H2 non autorisés existent "
                      "(seuls les PEGS sont autorisés au niveau ##)")

    return errors


# ============================================================
# Pytest Tests
# ============================================================

@pytest.fixture
def markdown_content():
    """Charge le Markdown depuis le fichier"""
    return read_markdown(MARKDOWN_FILE)


def test_pegs_sections_exist(markdown_content):
    """Vérifie que les 4 sections PEGS principales sont présentes"""
    errors = validate_pegs_structure(markdown_content)
    missing = [e for e in errors if "manquantes" in e]
    assert not missing, f"Sections PEGS manquantes: {missing}"


def test_pegs_unique(markdown_content):
    """Vérifie qu'aucune section PEGS n'est dupliquée"""
    errors = validate_pegs_structure(markdown_content)
    duplicates = [e for e in errors if "dupliquée" in e]
    assert not duplicates, f"Sections PEGS dupliquées: {duplicates}"


def test_pegs_order(markdown_content):
    """Vérifie que l'ordre des sections PEGS est correct"""
    errors = validate_pegs_structure(markdown_content)
    order_errors = [e for e in errors if "Ordre PEGS invalide" in e]
    assert not order_errors, f"Ordre PEGS incorrect: {order_errors}"


def test_pegs_h2_only(markdown_content):
    """Vérifie qu'aucun H2 autre que PEGS n'existe"""
    errors = validate_pegs_structure(markdown_content)
    h2_errors = [e for e in errors if "titres H2 non autorisés" in e]
    assert not h2_errors, f"H2 non autorisés détectés: {h2_errors}"


def test_pegs_numbers_increasing(markdown_content):
    """Vérifie que les numéros de sections PEGS sont croissants"""
    errors = validate_pegs_structure(markdown_content)
    number_errors = [e for e in errors if "numéros de sections PEGS" in e]
    assert not number_errors, f"Numéros de sections PEGS non croissants: {number_errors}"
