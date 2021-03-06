import numpy as np
import pandas as pd

def extract_sleep_data():
    questionnaire_path = 'Questionnaire.csv'
    sleep_path = 'Sleep.csv'

    questionnaire = pd.read_csv(questionnaire_path)
    # sleep = questionnaire.iloc[:, 1:9]
    # sleep.to_csv(sleep_path)
    sleep_label = ['Unnamed: 0', 'SLQ300', 'SLQ310', 'SLD012', 'SLQ030', 'SLQ040', 'SLQ050', 'SLQ120']
    
    questionnaire = questionnaire.drop(sleep_label, 1)
    questionnaire.to_csv('Questionnaire_clean.csv')

def remove_sleep_data():
    paths = ['Demographics.csv', 'Examination.csv', 'Laboratory.csv']
    sleep_label = ['Unnamed: 0', 'SLQ300', 'SLQ310', 'SLD012', 'SLQ030', 'SLQ040', 'SLQ050', 'SLQ120']

    for path in paths: 
        csv = pd.read_csv(path)
        csv = csv.drop(sleep_label, 1)
        csv.to_csv(path)

def clean(path):
    csv = pd.read_csv(path)
    labels = csv.columns

    for label in labels:
        try:
            valid = csv[label][~np.isnan(csv[label])]
            if min(valid) < 1e-20:
                csv[label][~np.isnan(csv[label])] = csv[label][~np.isnan(csv[label])].astype(int)

        except Exception as e:
            print(e)
            continue
    
    csv.to_csv(path)
    
def main():
    paths = ['Questionnaire.csv', 'Demographics.csv', 'Examination.csv', 'Laboratory.csv']
    for path in paths:
        csv = pd.read_csv(path)
        csv = csv.drop(['Unnamed: 0', 'Unnamed: 0.1'], 1)
        csv.to_csv(path)
        
if __name__ == '__main__':
    main()