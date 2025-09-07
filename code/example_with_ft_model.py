#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#a programme for establishing the ground truth of gpt 3.5-turbo's performance in revising a sample of sentences from the HE guidance corpus.

#import packages
import pandas as pd
import os
from openai import OpenAI
import re


#initiate new openai session with api key
os.environ['OPENAI_API_KEY'] = 'key_here'

client=OpenAI()

#upload training data file
df=pd.read_csv('path_to_file')


#set system instructions 
system_message = {
    "role": "system",
    "content": "You are HAZEL, an AI assistant desiged to support authors of heritage guidance with writing clear, accesible content for a general audience in the UK."
}

#select model
gpt_model='gpt-3.5-turbo'
#gpt_model='gpt-4-0613'

#function for calling gpt 3.5-turbo
def revise_sentence(sentence):
    completion = client.chat.completions.create(
        model=gpt_model,
        messages=[
            system_message,
            {"role": "user", "content": f"Hi, HAZEL! Can you help me revise the following sentence for guidance I am working on? {sentence}"}
        ],
        temperature=0.5  # balance between precision and creativity
    )
    return completion.choices[0].message.content

#apply the function to each sentence in the training data and save the results in a new column
df['GPT Revision'] = df['Original'].apply(revise_sentence)

#clean the data in the GPT Revision column to only include the revised sentences
df['Clean Revision']=df['GPT Revision'].apply(lambda x: re.sub(".*:", "", x))


#save the dataframe as a .csv file
df.to_csv('path_to_save_file')
