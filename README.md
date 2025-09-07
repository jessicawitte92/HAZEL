# Supplementary materials for the HAZEL pilot chatbot 
paper under review (preprint available [here](http://dx.doi.org/10.13140/RG.2.2.19093.18401))

## 1. "Interview" with ChatGPT: supplementary transcripts (/transcripts)
### Overview
The transcripts included in this folder document a series of interactions with OpenAI’s ChatGPT (built on the GPT-3.5 model), conducted as part of our research to assess the model's ability to meet Historic England’s (HE) writing standards for heritage guidance. This "interview" aimed to evaluate the chatbot's performance in key areas such as:

* adhering to British English spelling and grammar conventions
* revising text for clarity and consistency
* estimating text readability using common formulas (Flesch-Kincaid and Flesch Readability Ease)
* demonstrating memory and contextual understanding across multiple prompts

The interviews were conducted over several sessions between May and July 2024. Each transcript in this folder includes the corresponding input provided to ChatGPT and its output. The logs provide insight into the model's strengths, weaknesses, and occasional errors that arose during the qualitative assessment.

### /transcripts contents
This folder contains a log of inputs and outputs from the interviews with ChatGPT, including detailed examples where the model performed successfully and where it encountered issues. 

Notable issues include:
* generating misleading or false information including bibliographic references
* inconsistent application of British spelling and grammar conventions
* memory loss and breakdowns in context between conversational turns ("conversational amnesia")
* inaccurate readability assessments based on common formulas
* difficulty with basic numerical or mathematical processes such as counting

### Limitations
While the transcripts provide a glimpse of ChatGPT’s performance in responding to a series of zero-shot prompts, the record here should not be taken to be fully representative of ChatGPT's performance. The responses were generated using ChatGPT 3.5, which was available to 'free' users in mid-2024. 

## 2. Code for Fine-Tuning GPT-3.5 for HAZEL (/code)
The code in this folder was developed to fine-tune OpenAI’s GPT-3.5 model. The following files cover the steps involved in the process, from data preparation to fine-tuning and testing the model:

* /format_training_data.py: a script to prepare training and validation datasets in JSON Lines format, used for fine-tuning the model
* /fine_tuning.py: a script for fine-tuning a GPT model through the OpenAI API using pre-processed data
* /example_with_ft_model.py: using the fine-tuned model behind HAZEL

### Notes
**API key**: ensure that your OpenAI API key is correctly added to the script before running. Do not share your API key publicly for security purposes. The code contains placeholders where the API key should be inserted (e.g., 'key_here').
**Data privacy**: we established a zero-data retention (ZDR) agreement with OpenAI before beginnign development to ensure that no input data would be stored, reused, or accessed by OpenAI during the training process. 
**Token costs**: OpenAI charges based on token usage, which includes both input and output tokens. At the time of development, ine tuning and working with fine-tuned models cost more than using base models.

## 3. User guide for HAZEL (/other/user_guide.md)
An overview of HAZEL and tips for working with it. The user guide, which was written for internal use, also points users to additional resources about GenAI and LLMs.
