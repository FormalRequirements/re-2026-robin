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

def test_terminology_no_should(markdown_content):
    """Vérifie que le mot 'should' (devrait) n'est pas utilisé. """
    errors = []
    for i, line in enumerate(markdown_content.splitlines()):
        if re.search(r'\bshould\b', line, re.IGNORECASE):
            errors.append(f"Ligne {i+1}: {line.strip()}")
    assert not errors, (
        f"Le mot-clé 'should' (ambigu) a été détecté. " f"Détails: {errors}")

def test_id_format_compliance(markdown_content):
    """Vérifie que tous les IDs respectent strictement le format X.Y-ZZ."""
    pattern = re.compile(r'\*\*([PEGS]\.\d+-\d+)\*\*')
    found_ids = pattern.findall(markdown_content)
    assert found_ids, "Aucun ID valide trouvé (le format attendu est **X.Y-ZZ**)."
    
    bad_pattern = re.compile(r'\*\*([PEGS][\.\-]\d+[\.\-]\d+)\*\*')
    potential_bad_ids = bad_pattern.findall(markdown_content)
    
    real_errors = [pid for pid in potential_bad_ids if pid not in found_ids]
    
    assert not real_errors, f"IDs mal formatés détectés : {real_errors}. Format attendu : P.X-YY"

def test_cross_references_integrity(markdown_content):
    """Vérifie que si une exigence fait référence à une autre (ex: "Voir [S.1-02]")"""

    defined_ids = set(re.findall(r'\*\*([PEGS]\.\d+-\d+)\*\*', markdown_content))
    cited_ids = set(re.findall(r'[\[\(]([PEGS]\.\d+-\d+)[\]\)]', markdown_content))
    
    broken_links = [cite for cite in cited_ids if cite not in defined_ids]
    
    assert not broken_links, (
        f"Liens morts détectés ! Vous faites référence à des IDs qui n'existent pas :\n" f"{broken_links}"
    )

def test_no_placeholders(markdown_content):
    """Vérifie qu'il ne reste pas de mentions temporaires comme 'TODO', 'TBD', 'FIXME' ou '???'."""
    forbidden_terms = ['TODO', 'TBD', 'FIXME', '???', 'TO DO', 'TO DEFINED']
    errors = []
    
    for i, line in enumerate(markdown_content.splitlines()):
        upper_line = line.upper()
        for term in forbidden_terms:
            if term in upper_line:
                errors.append(f"Ligne {i+1}: Terme interdit '{term}' trouvé -> {line.strip()[:40]}...")

    assert not errors, f"Le document contient encore des zones en chantier :\n" + "\n".join(errors)

def test_unique_titles(markdown_content):
    """Vérifie qu'aucun titre d'exigence n'est utilisé deux fois."""
    lines = markdown_content.splitlines()
    titles_seen = {} #
    duplicates = []
    
    for line in lines:
        if "**" in line and "|" in line:
            parts = line.split("|")
            if len(parts) >= 3:
                current_id = parts[1].replace('*', '').strip()
                current_title = parts[2].replace('*', '').strip()
                
                if re.match(r'[PEGS]\.\d+-\d+', current_id):
                    if current_title in titles_seen:
                        prev_id = titles_seen[current_title]
                        duplicates.append(f"Titre '{current_title}' dupliqué (utilisé par {prev_id} et {current_id})")
                    else:
                        titles_seen[current_title] = current_id

    assert not duplicates, "\n".join(duplicates)
