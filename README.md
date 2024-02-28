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

## Literature Review

TODO: Conduct literature review by describing relevant work related to the project and hence providing an overview of the state of the art in the area of the project. This section serves to contextualize the study within the existing body of literature, presenting a thorough review of relevant prior research and scholarly contributions. In clear and meaningful language, this section aims to demonstrate the problems, gaps, controversies, or unanswered questions that are associated with the current understanding of the topic. In addition, this section serves to highlight the current study's unique contribution to the field. By summarizing and critiquing existing works, this section provides a foundation for readers to appreciate the novelty and significance of the study in relation to the broader academic discourse. The "Literature Review" section further contributes to the `why is the project important?` question. The number of scholarly work included in the literature review may vary depending on the project.

## Methods

TODO: Discuss the methods of the project to be able to answer the `how` question (`how was this project completed?`). The methods section in an academic research outlines the specific procedures, techniques, and methodologies employed to conduct the study, offering a transparent and replicable framework for the research. It details the resources behind the work, in terms of, for example, the design of the algorithm and the experiment(s), data collection methods, applied software libraries, required tools, the types of statistical analyses and models which are applied to ensure the rigor and validity of the study. This section provides clarity for other researchers to understand and potentially replicate the study, contributing to the overall reliability and credibility of the research findings.

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

TODO: Discuss the outcomes of your project in this section. Depending on the project type, the presented results and outcomes will vary. In some projects, you will be asked to present a theoretical analysis, and in others your experimental study and its results. In this section, you are also to demonstrate an enhanced version of your artifact by showing its capabilities and applications, in light of the evaluation metrics for assessing the artifact

---

## Exemplar Projects Discussions

The department's project descriptions can be found at [https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects](https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects)

## Schedule

The schedule for this work can be found at [https://github.com/CMPSC-580-Allegheny-College-Spring-2024/classDocs?tab=readme-ov-file#schedule](https://github.com/CMPSC-580-Allegheny-College-Spring-2024/classDocs?tab=readme-ov-file#schedule)