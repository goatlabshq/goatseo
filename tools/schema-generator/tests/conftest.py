from pathlib import Path

import pytest

from goatseo_schema_generator.generator import load_ontology
from goatseo_schema_generator.ir import Layer, Ontology
from goatseo_schema_generator.parser import DEFAULT_LAYERS

FIXTURE = Path(__file__).parent / "fixtures" / "schemaorg-1.0-current-https.nt"


@pytest.fixture
def fixture_source() -> Path:
    return FIXTURE


@pytest.fixture
def ontology() -> Ontology:
    return load_ontology(FIXTURE, "1.0")


@pytest.fixture
def ontology_with_pending() -> Ontology:
    return load_ontology(FIXTURE, "1.0", DEFAULT_LAYERS | {Layer.PENDING})
