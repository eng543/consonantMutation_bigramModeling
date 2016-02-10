import numpy as np
import pandas as pd

# read in target corpus
rf = open('CEG.txt')
corpus = []
for line in rf:
    line = line.lower()
    corpus += line.rsplit()

rf.close()

# read in set of target words to investigate in the corpus
# target word restrictions:
# begin with /p, t, k/ (undergo each class of mutation below)
# nouns
# occurred at least once in CEG corpus and comparison corpus (analysis not shown here)
rf = open('wordlist.txt','r')
rf = rf.read()
targets = eval(rf)

# dictionary of targets used for numpy matrix
targets_d = {}
for i, line in enumerate(targets):
    line = line.rstrip()
    targets_d[line] = i

# same procedure for three bigram models
# one model for each mutation type (soft, aspirate, nasal)
# 1) read in triggering environments
# 2) enumerate dictionary of triggers
# 3) create numpy matrix for tracking bigram counts
# 4) build bigram model

## soft mutation
# triggering environments for soft mutation
rf = open('soft_environments.txt')
soft = []
for word in rf:
    word = word.rstrip('\n')
    soft += word.rsplit('\r')

rf.close()

# dictionary of triggers for numpy matrix
soft_d = {}
for i, line in enumerate(soft):
    line = line.rstrip()
    soft_d[line] = i

# matrix for counts of soft mutation
counts_soft = np.zeros((len(soft_d),len(targets_d)))

# bigrams for soft mutation
for i in range(len(corpus)-1):
    if corpus[i] in soft:
        if corpus[i+1] in targets:
            counts_soft[soft_d[corpus[i]],targets_d[corpus[i+1]]] += 1

## aspirate mutation
rf = open('aspirate_environments.txt')
aspirate = []
for word in rf:
    word = word.rstrip('\n')
    aspirate += word.rsplit('\r')

rf.close()

aspirate_d = {}
for i, line in enumerate(aspirate):
    line = line.rstrip()
    aspirate_d[line] = i

counts_aspirate = np.zeros((len(aspirate_d),len(targets_d)))

# bigrams for aspirate mutation
for i in range(len(corpus)-1):
    if corpus[i] in aspirate:
        if corpus[i+1] in targets:
            counts_aspirate[aspirate_d[corpus[i]],targets_d[corpus[i+1]]] += 1

## nasal mutation
rf = open('nasal_environments.txt')
nasal = []
for word in rf:
    word = word.rstrip('\n')
    nasal += word.rsplit('\r')

rf.close()

nasal_d = {}
for i, line in enumerate(nasal):
    line = line.rstrip()
    nasal_d[line] = i

counts_nasal = np.zeros((len(nasal_d),len(targets_d)))

# bigrams for nasal mutation
for i in range(len(corpus)-1):
    if corpus[i] in nasal:
        if corpus[i+1] in targets:
            counts_nasal[nasal_d[corpus[i]],targets_d[corpus[i+1]]] += 1


# questions of interest for the study:
# 1) Do qualitative differences across mutation classes (e.g., range of triggering 
# environments/consonants affected) lead to quantitative differences in the incidence
# of mutated vs. radical (i.e., unmutated) forms for each class?
# 2) Does the incidence of mutation differ for words that occur frequently in the language,
# compared to those that occur infrequently?

# question 1
# dictionary with counts of (soft) mutated vs. unmutated occurrences of each target
Ds = {}
for word in targets_d.keys():
    if word[0] in ['p','t','c'] and word[:2] not in ['ph','th','ch']:
        radOc = 0
        mutOc = 0
        for trigger in soft_d:
            radOc += counts_soft[soft_d[trigger],targets_d[word]]
            if word[0] == 'p':
                mutOc += counts_soft[soft_d[trigger],targets_d['b' + word[1:]]]
            if word[0] == 't':
                mutOc += counts_soft[soft_d[trigger],targets_d['d' + word[1:]]]
            if word[0] == 'c':
                mutOc += counts_soft[soft_d[trigger],targets_d['g' + word[1:]]]
        Ds[word] = {'radical': radOc, 'mutated': mutOc}

# dictionary with counts of (aspirate) mutated vs. unmutated occurrences of each target
Da = {}
for word in targets_d.keys():
    if word[0] in ['p','t','c'] and word[:2] not in ['ph','th','ch']:
        radOc = 0
        mutOc = 0
        for trigger in aspirate_d:
            radOc += counts_aspirate[aspirate_d[trigger],targets_d[word]]
            if word[0] == 'p' and word[:2] not in ['ch','th','ph']:
                mutOc += counts_aspirate[aspirate_d[trigger],targets_d['ph' + word[1:]]]
            if word[0] == 't' and word[:2] not in ['ch','th','ph']:
                mutOc += counts_aspirate[aspirate_d[trigger],targets_d['th' + word[1:]]]
            if word[0] == 'c' and word[:2] not in ['ch','th','ph']:
                mutOc += counts_aspirate[aspirate_d[trigger],targets_d['ch' + word[1:]]]
        Da[word] = {'radical': radOc, 'mutated': mutOc}

# dictionary with counts of (nasal) mutated vs. unmutated occurrences of each target
Dn = {}
for word in targets_d.keys():
    if word[0] in ['p','t','c'] and word[:2] not in ['ph','th','ch']:
        radOc = 0
        mutOc = 0
        for trigger in nasal_d:
            radOc += counts_nasal[nasal_d[trigger],targets_d[word]]
            if word[0] == 'p' and word[:2] not in ['mh','nh','ngh']:
                mutOc += counts_nasal[nasal_d[trigger],targets_d['mh' + word[1:]]]
            if word[0] == 't' and word[:2] not in ['mh','nh','ngh']:
                mutOc += counts_nasal[nasal_d[trigger],targets_d['nh' + word[1:]]]
            if word[0] == 'c' and word[:2] not in ['mh','nh','ngh']:
                mutOc += counts_nasal[nasal_d[trigger],targets_d['ngh' + word[1:]]]
        Dn[word] = {'radical': radOc, 'mutated': mutOc}

# answer to question 1
softMut = 0
softRad = 0
for i in Ds.keys():
    softMut += Ds[i]['mutated']
    softRad += Ds[i]['radical']

propSoft = softMut / (softMut + softRad)

aspMut = 0
aspRad = 0
for i in Da.keys():
    aspMut += Da[i]['mutated']
    aspRad += Da[i]['radical']

propAsp = aspMut / (aspMut + aspRad)

nasMut = 0
nasRad = 0
for i in Dn.keys():
    nasMut += Dn[i]['mutated']
    nasRad += Dn[i]['radical']

propNas = nasMut / (nasMut + nasRad)

allMut = softMut + aspMut + nasMut
allRad = softRad + aspRad + nasRad

# side question 1: proportion mutation in corpus collapsed across mutation type
propMut = allMut / (allMut + allRad)

# question 2
# read in target word lists divided into high vs. low frequency sets
rf = open('hiprobs.txt','r')
hifreq_targets = rf.read()
rf.close()
hifreq_targets = eval(hifreq_targets)

rf = open('lowprobs.txt','r')
lowfreq_targets = rf.read()
rf.close()
lowfreq_targets = eval(lowfreq_targets)

hifreqs = []
lowfreqs = []

for i in Ds.keys():
    if i in hifreq_targets:
        if Ds[i]['mutated'] > 0 or Ds[i]['radical'] > 0:
            j = Ds[i]['mutated']/float(sum(Ds[i].values()))
            hifreqs.append(j)
    elif i in lowfreq_targets:
        if Ds[i]['mutated'] > 0 or Ds[i]['radical'] > 0:
            k = Ds[i]['mutated']/float(sum(Ds[i].values()))
            lowfreqs.append(k)

for i in Da.keys():
    if i in hifreq_targets:
        if Da[i]['mutated'] > 0 or Da[i]['radical'] > 0:
            j = Da[i]['mutated']/float(sum(Da[i].values()))
            hifreqs.append(j)
    elif i in lowfreq_targets:
        if Da[i]['mutated'] > 0 or Da[i]['radical'] > 0:
            k = Da[i]['mutated']/float(sum(Da[i].values()))
            lowfreqs.append(k)

for i in Dn.keys():
    if i in hifreq_targets:
        if Dn[i]['mutated'] > 0 or Dn[i]['radical'] > 0:        
            j = Dn[i]['mutated']/float(sum(Dn[i].values()))
            hifreqs.append(j)
    elif i in lowfreq_targets:
        if Dn[i]['mutated'] > 0 or Dn[i]['radical'] > 0:
            k = Dn[i]['mutated']/float(sum(Dn[i].values()))
            lowfreqs.append(k)

hiFreqMean = np.mean(hifreqs)

lowFreqMean = np.mean(lowfreqs)

# create dataframes to output relevant results to each research question
q1 = {'mutation_class' : ['soft', 'aspirate', 'nasal'],
	  'mutation_proportion' : [propSoft, propAsp, propNas]}

q1_df = pd.DataFrame(q1)
q1_df.to_csv("proportionMutation_byClass.csv", index = False)

q2 = {'frequency' : ['high', 'low'],
	  'mean_mutation_proportion' : [hiFreqMean, lowFreqMean]}

q2_df = pd.DataFrame(q2)
q2_df.to_csv("proportionMutation_byFrequency.csv", index = False)

