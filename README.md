# About

Developed for internal use, HAZEL supports authors with writing, editing and updating Historic England's guidance literature. 

In its current form, HAZEL runs on a GPT 3.5-turbo model that has been tailored to provide suggestions in accordance with HE's tone of voice and style requirements. 

In this repository, you can find out more about the project. We have also created a user manual and prompt library that you may wish to consult while working with HAZEL. 

# Project team
<img src="/assets/images/HE.png" width="300" height="100" />
<img src="/assets/images/UoE.png" width="300" height="100" />

# User manual

## Tips for working with HAZEL
HAZEL is a **prototype**; in other words, you're working with a rough draft of a technology that may become the foundation for a fully-functional, scaled-up, bespoke chatbot. Some functions are currently limited, and aesthetic finishing touches may be absent or underwhelming.

We designed HAZEL specifically for **assisting authors with writing tasks** such as brainstorming, outlining, summarising, condensing and editing. Unlike other generative AI technologies you may have worked with, HAZEL will not, in most cases, assist you with other queries. 

HAZEL has been designed to be reliable and honest about its limitations. However, all generative AI systems are prone to hallucination or generating false information. **It's important to double-check all of HAZEL's outputs for accuracy.**

When asking a question, you'll want to emphasise HAZEL's identity by calling the model by name. You can find some examples of what we mean here in the prompt library.

User feedback is essential for ensuring HAZEL--and any future scaling up of the HAZEL assistant--can best support authors. If you have any comments, queries, suggestions or complaints, we'd love to hear from you. Please send Dr Jessica Witte (jessica.witte@ed.ac.uk) an email and, where possible, include screenshots or other records of the prompts you entered and HAZEL's responses.  

## Prompt library and examples
### Calling HAZEL by name can improve results. 

   **Input**: "Revise this sentence: The Grade I-listed Strawberry Hill Villa is of national and international importance, as the most significant Gothic revival example of   the 18th century, with significant influence on the architecture of the subsequent century."
   
   **Output**: "The Strawberry Hill Villa, a Grade I-listed building, is of global and national significance as the most significant example of Gothic revival architecture in the 18th century, with significant influence on the architecture of the subsequent century."

   **Input**: "HAZEL, revise this sentence: The Grade I-listed Strawberry Hill Villa is of national and international importance, as the most significant Gothic revival example of the 18th century, with significant influence on the architecture of the subsequent century."
   
   **Output**: "Strawberry Hill Villa, a Grade I-listed building, is of national and international importance as the most significant example of Gothic revival in the 18th century, with notable influence on the subsequent century's architectural styles."

### Including specific details in prompts can further improve the output.
**Input**: "HAZEL, please improve this paragraph: The remains of ships and boats which meet the criteria set out in the Protection of Wrecks Act 1973 can be protected, which helps prevent uncontrolled interference. The remains of some ships and boats may be protected through scheduling or listing. The record of each protected wreck site is hosted on the National Heritage List for England (known as the NHLE). The NHLE is a publicly available, searchable database that contains information on England’s protected heritage."

**Output**: "The Protection of Wrecks Act 1973 sets out the criteria that determine which wrecks can be legally protected in order to prevent unauthorized interference. Some protected wrecks may be safeguarded through 'scheduling' or 'listing', and each protected wreck site is recorded on the publicly-accessible National Heritage List for England (the NHLE). This searchable database contains key details about England's protected maritime heritage."

**Input**: "HAZEL, please improve the readability of this paragraph by rewriting it in the active voice and rephrasing any unclear wording: The remains of ships and boats which meet the criteria set out in the Protection of Wrecks Act 1973 can be protected, which helps prevent uncontrolled interference. The remains of some ships and boats may be protected through scheduling or listing. The record of each protected wreck site is hosted on the National Heritage List for England (known as the NHLE). The NHLE is a publicly available, searchable database that contains information on England’s protected heritage."

**Output**: "The Protection of Wrecks Act 1973 protects ships and boats that meet certain criteria. This legislation helps to prevent uncontrolled interference. Some ships and boats receive protection through scheduling or listing. The National Heritage List for England (known as the NHLE) hosts the record of each protected wreck site. The NHLE is a publicly available, searchable database that contains information about England’s protected heritage."


### Prompt-less inputs can generate unpredictable outputs.
   **Input**: "The Grade I-listed Strawberry Hill Villa is of national and international importance, as the most significant Gothic revival example of the 18th century, with significant influence on the architecture of the subsequent century."
   
   **Output**: "Constructed between 1749 and 1794 by Horace Walpole, the villa has a unique and distinctive architectural style that combines elements of Gothic, Renaissance, and Baroque design. Its ornate interiors, with intricately carved woodwork, stained glass windows, and painted ceilings, further demonstrate the villa's historical significance as a key example of the Gothic revival style.

   The villa was also home to Walpole's extensive collection of art and antiquities, which he displayed in a series of themed rooms that reflected his scholarly interests and literary background. These include a Library with a collection of rare books and manuscripts, a Gallery with paintings from Walpole's personal collection, and a Tribune with classical statues and sculptures.\n\nIn addition to its architectural and cultural significance, Strawberry Hill Villa has also played a key role in the history of English literature, as a meeting place for writers, artists, and intellectuals of the time. Walpole's own literary works, including the novel "The Castle of Otranto," were inspired by the villa's Gothic architecture and helped to popularize the Gothic style in literature.

   Today, the villa is open to the public as a museum and cultural heritage site, showcasing its unique architecture, interiors, and history to visitors from around the world. Its preservation and restoration efforts have ensured that this important example of Gothic revival architecture will continue to be enjoyed and appreciated for generations to come."
   
### In most cases, HAZEL won't address prompts outside the scope of its training.
**Input**: "HAZEL, do you like fried chicken?"
**Output**: "I'm not personally able to eat, but I understand that fried chicken is a popular food choice!"

### Off-topic prompts that *do not* call HAZEL by name should receive a similar canned reply, but the risk of hallucination or misleading output may be higher.
**Input**: "Can you write me a paragraph about the pivotal role of coffee in apprehending the vampires in Bram Stoker's Dracula?"
**Output**: "I'm sorry, I am an AI developed to provide support for writing guidance. How about I help you with some of the harder parts of that sentence you were just working on?"

### You might also consider including some examples in your prompts to help guide HAZEL. (In machine learning, we would call this approach *few-shot prompting*.)
**Input**: "HAZEL, I need help revising some guidance in the active voice and I'd like you to follow the structure of the examples below.

Input: Post-project reflections are useful for learning what could be done differently in the future. The nature of conservation often means that unforeseen dilemmas and situations arise and even the best planned projects require flexibility and adaptation to resolve them to produce appropriate outcomes.
Output: In conservation, unforeseen dilemmas and situations arise even during the best planned projects. A flexible and adaptable approach can help us resolve unexpected obstacles. Completing a post-project reflection can provide an opportunity to learn from past experience.

Input: Where a public body no longer has a use for an asset, it should consider how to dispose of it in a way that gives best available overall value for money. In the first instance, public bodies must ensure that e-PIMS (OGC’s Electronic Property Information Mapping Service)23 is updated. It may also require adding to the Register of Surplus Public Sector Land operated by the Homes and Communities Agency. This enables other public bodies to express an interest in acquiring the asset. If there is no interest, the asset should then be disposed of by the most appropriate method (see section 8).
Output: It is important to follow protocols when disposing of a heritage asset. First, confirm the accuracy of the asset’s e-PIMS (OGC’s Electronic Property Information Mapping Service. To enable other public bodies to express an interest in acquiring the asset, you may also need to update the Register of Surplus Public Sector Land, which is operated by the Homes and Communities Agency. If there is no interest, then you may proceed with disposing of the asset by the most appropriate method (see section 8).

Here is the guidance I need help with: Many public buildings contain items of artistic, historical, technical or scientific importance. Examples include furniture, books, paintings, machinery and memorabilia connected with the past use of a historic building. Expert advice should be sought to confirm their value, historical importance and measures for their protection. Such items may need to be inventoried and recorded in situ prior to the building being vacated. Consideration may need to be given to whether they can be retained in situ following disposal, and whether this can be secured by means of a legal agreement. Where this is not practicable, the most appropriate method of disposal will need to be considered. The Museums Association has published guidance on ethical disposal which is applicable to museums and other public institutions holding collections of artistic, historic or scientific importance. This guidance emphasises the importance of long-term public benefit and keeping collections in the public domain. It does not endorse the sale of collections."

**Output**: "Many public buildings contain items of artistic, historical, technical, or scientific importance. Examples include furniture, books, paintings, machinery, and memorabilia connected with the past use of a historic building. Seek expert advice to confirm their value, historical importance, and measures for their protection. Inventory and record these items in situ before the building is vacated. Consider whether they can be retained in situ following disposal, and whether this can be secured by means of a legal agreement. If this is not practicable, consider the most appropriate method of disposal. The Museums Association has published guidance on ethical disposal that is applicable to museums and other public institutions holding collections of artistic, historical, or scientific importance. This guidance emphasizes the importance of long-term public benefit and keeping collections in the public domain—rather than endorsing the sale of collections."

## Tips for working with HAZEL

1. When working with generative AI, there is always a potential for hallucination, or unexpected outputs. **Thoroughly examine all of HAZEL's responses** before proceeding to make any suggested revisions.
2. We designed HAZEL to provide suggestions to improve readability for non-specialist readers. If your intended audience includes specialists or experts, you may wish to include information about your readers in your prompt.
3. Similarly, in cases where you need to use field-specific terminology when writing guidance, you may wish to instruct HAZEL to retain certain phrases or words in suggested revisions.
4. HAZEL is an AI assistant designed to support your throughout the writing process, but **you are the expert.** You are free to question or override any of HAZEL's suggestions.
5. Emerging research suggests that generative AI chatbots possess an identifiable writing style. For instance, they may repeat certain words and phrases (perhaps most famously, 'As an AI language model...') and construct sentences in a formulaic manner. Historic England's guidance corpus showcases the unique voices of our authors, and we want to ensure that our published work retains this diversity in the future. **In cases where you accept HAZEL's revisions, we therefore encourage you to complete any additional edits required to reflect your own voice.**
6. **HAZEL cannot access the Internet or real-time information** and therefore should not be used for generating bibliographies, locating sources, or other research tasks.
   

## Frequently Asked Questions

*Why should I use HAZEL?*

We developed HAZEL specifically for supporting authors during the guidance writing process. You may find HAZEL's ability to provide tailored suggestions on your work beneficial to expediting the revision process, in turn freeing your time for creative and collaborative work. HAZEL can assist you around the clock, meaning it can provide support outside of working hours and at times when your colleagues are away.

*Will HAZEL one day replace me?*

In short, no. HAZEL is an AI *assistant* rather than an author, and is not an expert in your subject area. If you've worked with generative AI technologies before, you may have encountered some of their shortcomings, such as limited analytical, creative and collaborative abilities. 

*When can I use HAZEL?*

At any point during the writing process, particularly when revising or updating existing content. It's important to remember that HAZEL cannot access the Internet, and so we do not recommend using the assistant for research.

*What can't HAZEL do?*

At this time, HAZEL will not generate content for you. Additionally, HAZEL cannot perform research, discuss current events, or access the Internet. You might also find HAZEL's analytical or creative thinking abilities a bit lackluster. HAZEL is not an expert, and so we suggest consulting your colleagues for content-related queries.


## Further reading
Mark Riedl, ['A Very Gentle Introduction to Large Language Models without the Hype'](https://mark-riedl.medium.com/a-very-gentle-introduction-to-large-language-models-without-the-hype-5f67941fa59e) 

Google, [Video series on GenAI and LLMs](https://www.youtube.com/playlist?list=PLBgogxgQVM9sl-KnKywVEhkb3QtLHU4OK) 

Google Developer Program, [resources on language models](https://developers.google.com/machine-learning/resources/intro-llms) 

Mark Humphries, ['Practical AI for Historians (and the Arts)](https://generativehistory.substack.com/p/practical-ai-for-historians-and-the) 

Adrian Tam, ['A Gentle Introduction to Prompt Engineering'](https://machinelearningmastery.com/a-gentle-introduction-to-prompt-engineering/)



