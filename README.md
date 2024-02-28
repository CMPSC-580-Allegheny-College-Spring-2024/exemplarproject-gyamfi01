[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Y4rZMh1t)
# Junior Seminar (CMPSC 580) Exemplar Project Repository

## Semester: Spring 2024

This repository contains student project materials, including project report, data, code, and references to literature for this departmentally-sponsored project. __As you complete each of the below sections in this document, please be sure to remove the preamble text so that it does not appear in your work.__ Please work with your first reader to answer any questions or concerns that you may have.

## GitHub Handle: gyamfi01

## Name: Jason Gyamfi

## Major: Data Science

## Project Name: Fact or Cap Checker

---

## Overview

The goal of the "Corpus Fact-Checking Dashboard" project is to create a simple tool for finding and verifying information in an XML file corpus. As evidenced by the increasing amount of research content available in digital formats, the project is in line with the department's goals by addressing the growing need for effective information retrieval and verification tools in the field of academic literature. The project entails developing a simple dashboard that allows users to enter textual information for fact-checking. The dashboard uses machine learning, natural language toolkits, and computational automation to verify concepts found in scientific literature by utilizing a corpus of scientific papers from PubMed. The output gives users precise details about where confirmed facts are located in the corpus. In order to create an interactive user interface, the project includes essential components including XML parsing, text preprocessing, and integration with the Streamlit framework. The amount of digital content in academic settings has grown, which calls for effective information retrieval and fact-checking. Current technologies might not be designed with academic corpus in mind, or they might not have user-friendly interfaces. By filling in these gaps, my project offers the academic community a focused solution.To conclude, the "Corpus Fact-Checking Dashboard" project provides academics with a specific tool to verify material found in an established corpus, therefore addressing a gap in the existing environment. The project's importance derives from its ability to improve the effectiveness of fact-checking and scholarly research procedures.


Literature Review

The intersection of natural language processing (NLP), information retrieval, and fact-checking has garnered substantial attention in recent years. As we delve into the existing body of literature, several key themes and contributions emerge that provide a foundation for the "Corpus Fact-Checking Dashboard" project.

1. NLP in Information Retrieval:
Researchers have explored the application of NLP techniques to enhance information retrieval processes. Khurana et al. (2023) present a comprehensive overview of the state of NLP, emphasizing its role in extracting meaningful information from textual data. Leveraging tools such as NLTK and Spacy, these approaches have shown promise in discerning patterns and sentiments from large corpora.

2. Fact-Checking and NLP:
The synergy between NLP and fact-checking has been a subject of interest. Das et al. (2023) specifically focus on human-centered NLP technology for fact-checking. Their work highlights the challenges and advancements in utilizing NLP to verify information, shedding light on the potential of such technologies in addressing misinformation.

3. Text Analysis in Academic Literature:
Text analysis in academic literature has been explored for various purposes. Min et al. (2023) discuss recent advances in NLP through large pre-trained language models. Their survey touches upon the evolving landscape of text analysis, showcasing its relevance in understanding and processing vast amounts of textual information.

4. Automated Dashboard for Fact-Checking:
While various studies discuss NLP and fact-checking independently, there is a noticeable gap in the literature regarding the development of automated dashboards for streamlined fact-checking processes. Capuano et al. (2023) touch upon content-based fake news detection, but a dedicated exploration of dashboards for academic fact-checking is notably absent.

5. Handling Large Corpus:
The challenge of managing extensive corpora, such as those found in PubMed, has been acknowledged. The need for effective storage and retrieval mechanisms is highlighted by Bharadiya (2023), who emphasizes the importance of considering methods for handling large volumes of textual data.

The "Corpus Fact-Checking Dashboard" project is noteworthy because it attempts to fill the hole in the literature by offering a targeted and simple to operate tool for fact-checking inside a particular corpus of scholarly articles. Although NLP, fact-checking, and text analysis are all mentioned in previous works, the integration of these ideas into an interactive dashboard for academic corpus fact-checking is a new development. The project provides a thorough solution for academics and researchers by addressing the real-world issues related to fact-checking and information retrieval in academic settings.

To summarize, the body of research highlights the value of natural language processing (NLP) in information retrieval and fact-checking, which opens doors for creative initiatives like the "Corpus Fact-Checking Dashboard" to meaningfully impact the developing field.

## Methods

### 1. Data Preprocessing

The project began with data preprocessing to prepare the textual content extracted from XML files for efficient searching.

- **Tokenization and Lowercasing:** The NLTK library was used to tokenize the text into words, and all words were converted to lowercase to ensure uniformity.

- **Stopword Removal:** Common English stopwords were removed to focus on meaningful content and enhance search accuracy.

### 2. Searching for Phrases in XML Files

The primary task was to search for user-specified phrases within a directory of XML files.

- **XML Parsing:** The `xml.etree.ElementTree` module facilitated parsing XML files to extract relevant text content.

- **Phrase Matching:** A function was developed to check for the existence of a given phrase in the preprocessed text using exact matching.

### 3. Streamlit User Interface

To make the project accessible and user-friendly, a Streamlit dashboard was implemented.

- **Dashboard Components:** The Streamlit framework was employed to create an interactive dashboard. Key components included:
  - Title display using `st.title`.
  - User input field for queries with `st.text_input`.
  - Button for triggering the fact-checking process with `st.button`.
  - Results display using `st.write`.

### 4. Special Setup Procedures

Specific setup procedures were required to ensure proper execution of the project.

- **NLTK Data Download:** The NLTK datasets ('punkt' and 'stopwords') were downloaded using `nltk.download` to support tokenization and stopwords removal.

- **XML Parsing:** Verification of the presence of necessary XML files in the specified corpus directory (`CORPUS_DIRECTORY`) was crucial for successful execution.

### 5. Source Code Organization

The source code was structured into functions to enhance modularity and readability. Each function had a specific role in the fact-checking process, contributing to code maintainability.

### 6. Running the Artifact

To execute the project, follow these steps:

1. Ensure NLTK datasets are available by running `nltk.download('punkt')` and `nltk.download('stopwords')`.

2. Verify the presence of XML files in the specified corpus directory (`CORPUS_DIRECTORY`).

3. Run the script containing the provided code.

The user will interact with the Streamlit dashboard, entering queries for fact-checking and receiving results dynamically.

By following this comprehensive methodology, the project achieved a reliable and replicable framework for fact-checking within a corpus of XML files, with a user-friendly interface provided by the Streamlit dashboard.

## Using the Artifact

**Setting Up the Initial Conditions:**

1. **Clone the Repository:**
   ```bash
   git clone git@github.com:CMPSC-580-Allegheny-College-Spring-2024/exemplarproject-gyamfi01.git
   cd src
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**
   - **For Windows:**
     ```bash
     .\venv\Scripts\activate
     ```
   - **For Unix/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Download and Extract PubMed Corpus:**
   - Download the corpus file, e.g., [oa_noncomm_xml.PMC001xxxxxx.baseline.2023-12-18.tar.gz](https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_noncomm/xml/oa_noncomm_xml.PMC001xxxxxx.baseline.2023-12-18.tar.gz)
   - Extract the file using:
     ```bash
     tar -xvf oa_noncomm_xml.PMC001xxxxxx.baseline.2023-12-18.tar.gz
     ```

6. **Set Up Local Database:**
   - Create a local database for efficient data retrieval during fact-checking.
   - Update database configuration in the project settings.

**Executing the Corpus Fact-Checking Dashboard:**

1. **Run the Dashboard:**
   ```bash
   streamlit fact_checker.py
   ```

2. **Access the Dashboard:**
   - Open a web browser and go to [http://localhost:8501](http://localhost:8501).

3. **Input Queries:**
   - Enter textual details for fact-checking in the provided field.

4. **Check Results:**
   - The dashboard will display messages confirming or denying the existence of the inputted facts in the corpus.

By following these steps, users can set up and execute the "Corpus Fact-Checking Dashboard" artifact. Ensure that all initial conditions, including virtual environment activation and database setup, are completed for a smooth execution experience.

## Results and Outcomes

If executed successfully, the output of the "Corpus Fact-Checking Dashboard" will provide results in the following format:

```
Phrase 'FISH' found in PMC1802627.xml
Phrase 'FISH' found in PMC1807950.xml
Phrase 'FISH' found in PMC1876603.xml
Phrase 'FISH' found in PMC1942175.xml
Phrase 'FISH' found in PMC1920257.xml
Phrase 'FISH' found in PMC1998876.xml
```

This output briefly displays the times the query phrase "FISH" appears in various XML files in the corpus. Users receive a concise and comprehensive summary of the fact-checking findings with each line corresponding to a separate file containing the term in question. It is easy for the user to comprehend and browse through the results, which makes it easier to comprehend where in the corpus the information that was searched is supported.

---

## Exemplar Projects Discussions

The department's project descriptions can be found at [https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects](https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects)

## Schedule

The schedule for this work can be found at [https://github.com/CMPSC-580-Allegheny-College-Spring-2024/classDocs?tab=readme-ov-file#schedule](https://github.com/CMPSC-580-Allegheny-College-Spring-2024/classDocs?tab=readme-ov-file#schedule)