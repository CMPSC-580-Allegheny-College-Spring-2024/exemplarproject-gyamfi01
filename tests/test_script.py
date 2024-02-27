import sys
# Append the directory, not the path to the .py file
sys.path.append('/Users/jasongyamfi/Desktop/Comp_Sci_203/exemplarproject-gyamfi01/src')
from fact_checker import preprocess_text, search_for_phrase

# Test for preprocess_text function
def test_preprocess_text():
    # Basic processing with stopword removal
    assert preprocess_text("This is, indeed, a test!", True) == "indeed test"
    # Processing without stopword removal
    assert preprocess_text("This is a test.", False) == "this is a test"

# Test for search_for_phrase function
def test_search_for_phrase():
    text = "this is a simple test"
    # Phrase found
    assert search_for_phrase("simple test", text) == True
    # Phrase not found
    assert search_for_phrase("complex test", text) == False
    # Case insensitivity
    assert search_for_phrase("This IS", text) == True
