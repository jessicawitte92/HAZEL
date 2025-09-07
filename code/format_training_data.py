#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:21:12 2024

"""
#from a .csv file of 129 sentences and their revisions, format a training and validating file for fine-tuning GPT-4 
#for the HAZEL pilot project

import pandas as pd
import json
import random
from sklearn.model_selection import train_test_split


#import dataset
df=pd.read_csv("import_file_path")

#split into training/testing files
df_train, df_val = train_test_split(df, test_size=0.2, random_state=13)


#define introductory text for user:content 

train_prompt=['Please revise this sentence. Use UK English spelling and grammar. Use a professional tone of voice. Use clear, concise language accessible to non-specialists. Also, use active voice, avoid nominalization and contractions, use numerals for numbers, % for percentages. Double quotes for speech, single for emphasis. Avoid the Oxford comma. Where possible, use simple clauses and short sentences. Keep punctuation outside quotations.']

question_list=['Can you revise this sentence? Use UK English and aim for a professional tone. Use clear, concise language accessible to non-specialists.',
'Revise this to use active voice, avoid nominalization and contractions. Use numerals for numbers, % for percentages. Double quotes for speech, single for emphasis. Avoid the Oxford comma, semicolons, use simple clauses and short sentences. Punctuation outside quotations.',
'Please rephrase this sentence to make it more concise and clear. Follow UK spelling/grammar.',
'Can you rewrite this sentence in clear, professional tone for non-specialist audiences using active voice and UK English.',
'Could you revise this sentence?',
'Please rephrase this sentence to avoid any ambiguity.',
'Use UK English spelling and grammar. Aim for a professional tone, clear, concise language accessible to non-specialists.',
'Could you revise this sentence for me according to style and tone guidelines?'] 

#format training file
def train_data(df):

    new_data = []

    for index, row in df.iterrows():
        new_entry = {
            "messages": [
                {"role": "user", "content": ' '.join(train_prompt) + str(row["Original"])},
                {"role": "assistant", "content": row["Revised"]}
            ]
        }
        new_data.append(new_entry)
    
    return new_data


training_data=train_data(df_train)

#format validation file

def val_data(df, randomize_questions=False):
    def add_context(original, question_list):
        question = random.choice(question_list) if randomize_questions else question_list[0]
        return f"{question} {original}"

    formatted_data = []

    for index, row in df.iterrows():
        original_with_context = add_context(row["Original"], question_list)
        revised_with_context = row["Revised"]

        new_entry = {
            "messages": [
                {"role": "user", "content": original_with_context},
                {"role": "assistant", "content": revised_with_context}
            ]
        }
        formatted_data.append(new_entry)

    return formatted_data

    def add_context(original, revised):
        question = "Could you revise this sentence for me according to style and tone guidelines? "
        answer = "Sure, here's the corrected sentence: "
        return f"{question} {original}", f"{answer} {revised}"

    new_data = []
    
    for index, row in df.iterrows():
        original_with_context, revised_with_context = add_context(row["Original"], row["Revised"])
        
        new_entry = {
            "messages": [
                {"role": "user", "content": original_with_context},
                {"role": "assistant", "content": revised_with_context}
            ]
        }
        new_data.append(new_entry)
    
    intro_message = {
        "messages": [
            {"role": "user", "content": "I am working on guidance for a heritage organisation and all of the text needs to follow specific style and tone of voice guidelines. First, we are using British or UK English spellings and grammatical conventions, rather than US. Second, we are using a professional tone of voice and aim to write in clear, concise language that is accessible to non-specialist audiences."},
            {"role": "assistant", "content": "Great! I can help you revise text according to these specifications. Let me know if there's anything else I should keep in mind to better assist you."}
        ]
    }
    new_data.append(intro_message)
    
    intro_message_2 = {
        "messages": [
            {"role": "user", "content": "Here are some additional specifications: Use active voice over passive voice. Avoid nominalization. Avoid contractions, especially negative contractions. Use numerals, not letters, for numbers below the millions. Use % for percentages instead of 'percent'. Use double quotations for actual quoted speech, and single quotations to provide emphasis. Do not use the Oxford comma. Where possible, avoid using semicolons and other punctuation and choose simple clauses and shorter sentences. Finally, following UK style, punctuation will be outside of single or double quotations."},
            {"role": "assistant", "content": "Great, thank you for the additional information. I'm happy to asisst you with your writing, so feel free to ask for help at any point!"}
        ]
    }
    new_data.append(intro_message_2)
    
    return new_data
validating_data=val_data(df_val)


#save files
with open('file_path', 'w') as file:
    for entry in training_data:
        file.write(json.dumps(entry) + '\n')
        
with open('file_path', 'w') as file:
    for entry in validating_data:
        file.write(json.dumps(entry) + '\n')
    
