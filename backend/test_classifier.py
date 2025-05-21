import sys
import os

# Ensure 'backend/' is treated as the root module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app.tag_classifier import QueryTagger

@pytest.fixture(scope="module")
def tagger():
    return QueryTagger()

def test_basic_prediction(tagger):
    tags = tagger.predict("I want something spicy and low-carb")
    assert isinstance(tags, list)
    assert "spicy" in tags or "low-carb" in tags

def test_empty_query(tagger):
    tags = tagger.predict("")
    assert tags == []

def test_gibberish_query(tagger):
    tags = tagger.predict("asdlkjasd1234")
    assert isinstance(tags, list)  # Should be empty or near-empty, not crash
