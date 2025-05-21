import os
import pytest
from app.tag_classifier import QueryTagger

@pytest.fixture(scope="module")
def tagger():
    return QueryTagger(model_dir=os.path.join(os.path.dirname(__file__), "../tagger_model"))

def test_basic_prediction(tagger):
    tags = tagger.predict("I want a spicy low-carb lunch")
    assert isinstance(tags, list)
    assert "spicy" in tags or "low-carb" in tags

def test_empty_query(tagger):
    tags = tagger.predict("")
    assert tags == []

def test_noise_query(tagger):
    tags = tagger.predict("nonsensicalwordzz")
    assert isinstance(tags, list)  # should still return a list
