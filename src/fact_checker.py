"""Corpus Fact-Checking Dashboard: Search for phrases in a directory of XML files and display results in a Streamlit UI."""

import os
import re
import xml.etree.ElementTree as ET
import streamlit as st
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Ensure NLTK datasets are available
nltk.download('punkt')
nltk.download('stopwords')

# Hardcoded path to your corpus directory
CORPUS_DIRECTORY = '/Users/jasongyamfi/Desktop/Comp_Sci_203/exemplarproject-gyamfi01/data/corpus/PMC001xxxxxx'

def preprocess_text(text, remove_stopwords=True):
    """Preprocess text for searching."""
    words = word_tokenize(text.lower())
    if remove_stopwords:
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word not in stop_words]
    words = [re.sub(r'\W+', '', word) for word in words]
    words = [word for word in words if word]  # Filter out empty strings
    return ' '.join(words)

def search_for_phrase(phrase, text):
    """Check if a phrase is in the text."""
    processed_phrase = preprocess_text(phrase, remove_stopwords=False)
    processed_text = preprocess_text(text, remove_stopwords=False)
    return processed_phrase in processed_text

def parse_xml_and_search(query, directory=CORPUS_DIRECTORY):
    """Search for a query in XML files within a directory."""
    results = []
    for filename in os.listdir(directory):
        if filename.endswith('.xml'):
            path = os.path.join(directory, filename)
            try:
                tree = ET.parse(path)
                root = tree.getroot()
                text_content = ' '.join(element.text for element in root.iter() if element.text)
                if search_for_phrase(query, text_content):
                    results.append(f"Phrase '{query}' found in {filename}")
            except ET.ParseError as e:
                results.append(f"Error parsing {filename}: {e}")
    return results

# Streamlit UI components remain the same
st.title('Corpus Fact-Checking Dashboard')

query = st.text_input('Enter your query for fact-checking:', '')

if st.button('Check Facts'):
    if query:
        with st.spinner('Searching the corpus...'):
            results = parse_xml_and_search(query)
            if results:
                for result in results:
                    st.write(result)
            else:
                st.write('No matching facts found in the corpus.')
    else:
        st.error('Please enter a query to check facts.')
