#!/usr/bin/env python3
"""Validate the generated SKOS taxonomy."""

import sys
from pathlib import Path
from rdflib import Graph
from rdflib.namespace import SKOS, RDF

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"


def validate(g):
    errors = []
    warnings = []

    concepts = set(g.subjects(RDF.type, SKOS.Concept))
    schemes = set(g.subjects(RDF.type, SKOS.ConceptScheme))

    if not schemes:
        errors.append("No ConceptScheme found")

    for concept in concepts:
        uri = str(concept)

        # Must have prefLabel
        labels = list(g.objects(concept, SKOS.prefLabel))
        if not labels:
            errors.append(f"Missing prefLabel: {uri}")

        # Must have definition
        defs = list(g.objects(concept, SKOS.definition))
        if not defs:
            warnings.append(f"Missing definition: {uri}")

        # Must be in a scheme
        in_scheme = list(g.objects(concept, SKOS.inScheme))
        if not in_scheme:
            warnings.append(f"Not in any scheme: {uri}")

        # Top concepts should not have broader
        is_top = any(g.triples((concept, SKOS.topConceptOf, None)))
        has_broader = any(g.triples((concept, SKOS.broader, None)))
        if is_top and has_broader:
            errors.append(f"Top concept has broader: {uri}")

        # Non-top concepts should have broader
        if not is_top and not has_broader:
            warnings.append(f"Non-top concept without broader: {uri}")

    # Check for cycles in broader
    for concept in concepts:
        visited = set()
        current = concept
        while True:
            broaders = list(g.objects(current, SKOS.broader))
            if not broaders:
                break
            current = broaders[0]
            if current in visited:
                errors.append(f"Cycle detected involving: {uri}")
                break
            visited.add(current)

    return errors, warnings


def main():
    ttl_path = DIST / "taxonomy.ttl"
    if not ttl_path.exists():
        print(f"ERROR: {ttl_path} not found. Run convert.py first.")
        sys.exit(1)

    g = Graph()
    g.parse(str(ttl_path), format="turtle")

    concepts = set(g.subjects(RDF.type, SKOS.Concept))
    top_concepts = set(g.subjects(SKOS.topConceptOf, None))

    print(f"Loaded {len(g)} triples")
    print(f"Found {len(concepts)} concepts ({len(top_concepts)} top-level)")

    errors, warnings = validate(g)

    for w in warnings:
        print(f"  WARNING: {w}")
    for e in errors:
        print(f"  ERROR: {e}")

    if errors:
        print(f"\nValidation FAILED with {len(errors)} error(s)")
        sys.exit(1)
    else:
        print(f"\nValidation PASSED ({len(warnings)} warning(s))")


if __name__ == "__main__":
    main()
