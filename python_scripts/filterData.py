
# coding: utf-8

# In[1]:


import pandas as pd


# In[27]:


# Loading the cervical cancer data set
# The data set can be found at http://archive.ics.uci.edu/ml/machine-learning-databases/00383/
# More information about the dataset can be found at http://archive.ics.uci.edu/ml/datasets/Cervical+cancer+%28Risk+Factors%29#
data = pd.read_csv('risk_factors_cervical_cancer_working_dataset.csv')


# In[28]:


data.head()


# #  Cleaning up the data


# Removing Error prone columns.
# STDs: Time since first diagnosis
# STDs: Time since last diagnosis
# Reason they contain a large set of NaN values and this is hard to work with.
data = data.dropna(axis=1, how='all')


# Removing unwanted columns
# First sexual intercourse
# IUD
# IUD (years)
# STDs:cervical condylomatosis
# STDs:vaginal condylomatosis
# STDs:vulvo-perineal condylomatosis
# STDs:syphilis
# STDs:genital herpes
# STDs:Hepatitis B
# STDs: Number of diagnosis
# Dx
# Hinselmann
# Schiller
# Biopsy
# STDs: Time since first diagnosis
# STDs: Time since last diagnosis

data = data.drop(['First sexual intercourse','IUD', 'IUD (years)', 'STDs (number)', 'Smokes (years)', 'Smokes (packs/year)',
           'STDs:cervical condylomatosis', 'STDs:vaginal condylomatosis', 
           'STDs:vulvo-perineal condylomatosis', 'STDs:syphilis',
           'STDs:genital herpes', 'STDs:Hepatitis B', 'STDs: Number of diagnosis', 'STDs: Time since first diagnosis', 'STDs: Time since last diagnosis',
           'Dx', 'Hinselmann', 'Schiller', 'Biopsy'],axis=1)



# We are left with
# - Age
# - Smoking 
# - Sexual partners
# - Hormonal contraceptives [bool & int)
# - STDs [bool & int ]
# - STDs : cervical condylomatosis 
# - (bool) STDs : pelvic inflammatory disease
# -(bool) STDs:molluscum contagiosum 
# - (bool) STDs:AIDS 
# - (bool) STDs:HIV 
# - (bool) STDs:HPV 
# - (bool) Dx:Cancer 
# - (bool) Dx:CIN 
# - (bool) Dx:HPV 
# - (int) Num of pregnancies 

# Our Target variable is 
# - (bool) Cytology





# drop rows with now values


data = data.dropna()



data.head()



# saved filtered csv
data.to_csv('filtered_01_cervical_cancer_dataset.csv')

