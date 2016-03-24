Project: Bigram modeling of Welsh consonant mutation

# R script and materials for modeling

This project was designed as a collaborated final project for a computational linguistics 
course at Northwestern University. The materials included were those I was responsible for 
as part of the collaboration. The modeling done by my collaborator is not included.

The goal of this project was to investigate the incidence of a phenomena called consonant 
mutation in Welsh. In this process, the initial consonants of words change (are mutated) 
depending on the characteristics of the word that precedes it. For example, the word 'caneuon' 
(meaning: songs) is pronounced as 'ganeuon' (c sound changes to g sound) when preceded by 
the word 'am' (meaning: about).

This project considered differences in the incidence of consonant mutation among the three 
classes of mutation in Welsh: soft, aspirate, and nasal (named according to the type of sound 
change they condition). Additionally, it considered whether the incidence of mutation differed 
across written and spoken corpora of Welsh. The current repository shows the modeling and results 
for the written corpus only (modeling of spoken corpus was done by collaborator). Finally, 
we considered whether the incidence of consonant mutation is sensitive to how likely any given word 
is to occur in the language (i.e., its frequency). 

The results indicated that:
* The incidence of consonant mutation differed across classes: soft > aspirate > nasal
* The incidence of consonant mutation did not differ according to frequency of the mutated 
word in the language
* Consonant mutation occurred a larger proportion of the time in written vs. spoken Welsh 
(results not shown)

# Materials

This repository contains:
* aspirate_environments.txt: a file containing the words that trigger aspirate mutation
* CEG_modeling.py: Python script, which builds bigram models
* CEG.txt: the target corpus of written Welsh
* hiprobs.txt: a file containing the high frequency target words
* lowprobs.txt: a file containing the low frequency target words
* nasal_environments.txt: a file containing the words that trigger nasal mutation
* proportionMutation_byClass.csv: output dataframe of incidence of mutation by class
* proportionMutation_byFrequency.csv: output dataframe of incidence of mutation by target frequency
* soft_environments.txt: a file containing the words that trigger soft mutation
* welshConsonantMutation.pdf: project writeup, including theoretical motivation, methods, results, and interpretation
* wordlist.txt: a file containing the target words selected for study