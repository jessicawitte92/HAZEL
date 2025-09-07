# HAZEL
supplementary materials for the HAZEL pilot chatbot. paper under review.

prepint avaialble at: http://dx.doi.org/10.13140/RG.2.2.19093.18401
Generative AI in Heritage Practice: Improving the Accessibility of Heritage Guidance (Preprint)
authors: J. Witte, E. Lee, L. Brausem, V. Shillabeer, and C. Bonacchi


1. Interview with ChatGPT: Supplementary Transcripts
Overview
The transcripts included in this folder document a series of interactions with OpenAI’s ChatGPT (built on the GPT-3.5 model), conducted as part of our research to assess the model's ability to meet Historic England’s (HE) writing standards for heritage guidance. This "interview" aimed to evaluate the chatbot's performance in key areas such as:
Adhering to British English spelling and grammar conventions
Revising text for clarity and consistency
Estimating text readability using common formulas (Flesch-Kincaid and Flesch Readability Ease)
Demonstrating memory and contextual understanding across multiple prompts
The interviews were conducted over several sessions between May and July 2024. Each transcript in this folder includes the corresponding input provided to ChatGPT and its output. The logs provide insight into the model's strengths, weaknesses, and occasional errors that arose during the qualitative assessment.
Purpose of the Interview
The aim of the interview was to evaluate whether ChatGPT could reliably produce text that met the high standards required for HE’s heritage guidance documents. Specifically, we wanted to test if the model could generate:
Accurate bibliographies
Consistent application of British English spelling
Text revisions following clear instructions (e.g., converting passive to active voice)
Consistent performance across different writing tasks, such as readability assessments
The results of this qualitative assessment informed our decision to proceed with further fine-tuning of the model, as well as offering broader insights into the current limitations and capabilities of general-purpose language models (LLMs) like ChatGPT.
What’s in the Transcripts Folder
This folder contains a log of inputs and outputs from the interviews with ChatGPT, including detailed examples where the model performed successfully and where it encountered issues. Notable issues include:
The generation of false references and misleading information.
Inconsistent application of British spelling and grammar conventions.
Memory loss and breakdowns in context between conversational turns (referred to as "conversational amnesia").
Inaccurate readability assessments based on common formulas.
For example, one interaction tested ChatGPT’s ability to revise text into active voice while using British English spelling. While the model correctly changed the vocabulary ("zucchini" to "courgettes"), it failed to apply other British English terms like “shopping bag” or “suncream.” This inconsistency in applying British English conventions highlights a limitation in the model's performance.
How to Use the Transcripts
The logs are organized by date, with each entry representing a distinct interaction with ChatGPT. You can follow these steps to explore the material:
Open the relevant transcript file to view the input and output from a specific interaction.
Look for highlighted instances where ChatGPT's output deviated from expected standards or made errors.
Refer to the "Results and Discussion" sections of the paper for analysis on how these transcripts informed the overall findings.
For a deeper dive into the methodology and specific insights derived from these interactions, see Section 5.1 ("‘Interview’ with ChatGPT") and Section 4.2 ("Preliminary Assessment of ChatGPT") in the paper.
Limitations
While the transcripts provide a valuable record of ChatGPT’s performance, the analysis is based on a relatively small sample size and a single version of the model (GPT-3.5). The results presented here may not be fully representative of newer models or different configurations. Moreover, the transcripts reflect a single instance of prompt engineering, and further experimentation would be needed to refine the approach or improve results in other contexts.

Code for Fine-Tuning GPT-3.5 for HAZEL
Overview
The code in this folder was developed to fine-tune OpenAI’s GPT-3.5 model to meet the specific requirements of the HAZEL project, which aims to assist authors in revising heritage guidance documents in line with UK writing standards. The following files cover the steps involved in the process, from data preparation to fine-tuning and testing the model:
Data Preparation and Preprocessing: Includes the conversion of PDF guidance documents to machine-readable text, dataset creation, and formatting for fine-tuning.
Fine-Tuning GPT-3.5: This file contains the process for training the model using pre-processed data.
Formatting Training and Validation Data: A script to prepare training and validation datasets in JSON Lines format, used for fine-tuning the model.
Important Considerations
API Key: Please ensure that your OpenAI API key is correctly added to the script before running. Do not share your API key publicly for security purposes. The code contains placeholders where the API key should be inserted (e.g., 'key_here').
Data Privacy: For this project, we used OpenAI’s zero-data retention agreement to ensure that no input data would be stored, reused, or accessed by OpenAI during the training process. This measure is crucial to safeguard sensitive content.
Files in this Repository
Data Preparation Script (data_preparation.py)
Purpose: Converts the Historic England (HE) guidance documents from PDF images to machine-readable text files using OCR (Tesseract-OCR), extracts excerpts, and prepares them for fine-tuning.
Key Functions:
OCR processing of PDFs.
Cleaning of raw text.
Sampling of data into structured .csv files for further revisions.
Instructions for Use:
Make sure that the HE guidance corpus is available in PDF format.
Update the file paths for both the PDF documents and the location to save the processed files.
Fine-Tuning Script (fine_tuning.py)
Purpose: Initiates fine-tuning for GPT-3.5 using the pre-processed training data. This script uses OpenAI's API to create and manage fine-tuning jobs, upload training and validation data, and track the fine-tuning process.
Key Functions:
Uploading training and validation datasets.
Creating fine-tuning jobs with OpenAI’s API.
Checking the status of fine-tuning jobs.
Deleting models post-fine-tuning (optional).
Instructions for Use:
Ensure that the training and validation datasets are in JSONL format.
Update the file paths for the data and replace the placeholder for the API key.
Monitor fine-tuning progress via OpenAI’s API or your console.
Dataset Formatting Script (dataset_formatting.py)
Purpose: Converts the cleaned .csv dataset into JSON Lines format suitable for fine-tuning GPT-3.5, and prepares both training and validation sets.
Key Functions:
Splitting data into training and validation sets using train_test_split.
Generating prompt messages for training (ensuring they follow the desired guidelines for UK English and professional tone).
Formatting data into JSONL structure, ready for upload to OpenAI for fine-tuning.
Instructions for Use:
Replace the placeholder file paths with your own data file.
The code contains randomization features for question prompts; you can adjust this to control the consistency of training inputs.
Key Notes for Reproducibility
API Key Anonymization: For security reasons, the API key should never be shared or included in version-controlled code repositories. In the provided scripts, API keys have been removed and replaced with placeholders like 'key_here' and 'key_goes_here'. Ensure that you replace these with your own keys before running the scripts.
Dependencies: The following libraries are required to run the scripts:
openai: For interacting with OpenAI's API.
pandas: For handling CSV files and data manipulation.
os: For managing environment variables and file paths.
re: For cleaning and processing text.
json: For writing out data in JSON format.
random and sklearn.model_selection: For splitting datasets and randomizing inputs.
You can install these dependencies with the following:
pip install openai pandas sklearn

Data Integrity and Privacy: The guidance corpus used in this research was converted to text through Optical Character Recognition (OCR), which is a manual process that might introduce some errors. Ensure that the data you use for training is thoroughly cleaned before use.
Token Costs: OpenAI charges based on token usage, which includes both input and output tokens. The fine-tuning process and inference from the model will accumulate token usage, so ensure that you're mindful of potential costs when working with large datasets or high token usage.
Running the Code
Prepare the Data:
Use the data_preparation.py script to convert the PDF documents into machine-readable text.
Clean and format the data using the pre-processing steps provided.
Format the Dataset:
Run dataset_formatting.py to structure your dataset for fine-tuning. This script splits the data into training and validation sets and formats them into JSONL files.
Fine-Tune the Model:
Use the fine_tuning.py script to upload the datasets to OpenAI and initiate the fine-tuning job.
Track the fine-tuning job status to ensure that the model is trained successfully.
Test the Fine-Tuned Model:
Once the fine-tuning is complete, you can use the fine-tuned model for text revision tasks, as shown in the example code within fine_tuning.py.

