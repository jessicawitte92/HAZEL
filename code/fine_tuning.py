#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#basic fine-tuning process for gpt models using pre-created training and validation datasets.

#import packages
import os
from openai import OpenAI


#initiate new openai session with api key:
os.environ['OPENAI_API_KEY'] = 'key_goes_here'

client=OpenAI()

#open a jsonl object for fine tuning. must contain at least 10 examples
client.files.create(
  file=open('training_data_file.jsonl', 'rb'),
  purpose="fine-tune"
)
#take note of the output of training_file and copy into the training_file field on line 36

#upload validation file (optional; should be 10-20% of training data, ideally with similar--but not identical!--prompts)
client.files.create(
  file=open('validation_data_file.jsonl', 'rb'),
  purpose="fine-tune"
)
#take note of the output of validation_file and copy into the validation_file field on line 37

#create a new fine tuning job
#additional arguments outlined in the documentation: https://platform.openai.com/docs/api-reference/fine-tuning
client.fine_tuning.jobs.create(
  training_file='file-name',
  validation_file='file-name',
  model="gpt-4-0613" 
)


#check status of a fine-tuning job:
#when the fine-tuning has finished, the output of the fine_tuned_model field will change from 'None' to the model's name
#(n.b. I have not found a way around running this line of code at 5-10 min. intervals until complete)
client.fine_tuning.jobs.retrieve('ftjob-name')

#cancel afine-tuning job:
#client.fine_tuning.jobs.cancel("...")

client.models.delete("ft:gpt-3.5-turbo:name")

#call the model
completion = client.chat.completions.create(
  model="ft:gpt-4-0613:name",
  messages=[
    {"role": "user", "content": "How would you correct this sentence: We had a conversation about the topic."}
  ]
)
print(completion.choices[0].message)
