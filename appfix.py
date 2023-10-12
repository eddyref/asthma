#import library
import streamlit as st
#import joblib
#load saved models
import pickle

#make choice box
AGE = {0: '0-9', 1: '10-19', 2: '20-24', 3: '25-59', 4: '60+'}
CHOICES = {0: "No", 1: "Yes"}
GENDER_CHOICE = {0: "Male", 1: "Female"}

st.title('Please Insert The Informations')

def gender_func(option):
    return GENDER_CHOICE[option]

def format_func(option):
    return CHOICES[option]

def age_func(option):
    return AGE[option]


tiredness = st.selectbox(
    'Tiredness', 
    options=list(CHOICES.keys()), format_func=format_func)

dry_cough = st.selectbox(
    'Dry Cough', 
    options=list(CHOICES.keys()), format_func=format_func)

difficulty_in_breathing = st.selectbox(
    'Difficulty in Breathing', 
    options=list(CHOICES.keys()), format_func=format_func)

sore_throat = st.selectbox(
    'Sore Throat', 
    options=list(CHOICES.keys()), format_func=format_func)

#none_sympton = st.selectbox(
#    'None Sympton', 
#    options=list(CHOICES.keys()), format_func=format_func)

pains = st.selectbox(
    'Pains', 
    options=list(CHOICES.keys()), format_func=format_func)

nasal_congestion = st.selectbox(
    'Nasal Congestion', 
    options=list(CHOICES.keys()), format_func=format_func)

runny_nose = st.selectbox(
    'Runny Nose', 
    options=list(CHOICES.keys()), format_func=format_func)

#none_experiencing = st.selectbox(
#    'None Experiencing', 
#    options=list(CHOICES.keys()), format_func=format_func)

age_range = st.selectbox(
    'Age Range', 
    options=list(AGE.keys()), format_func=age_func)

gender = st.selectbox(
    'Gender', 
    options=list(GENDER_CHOICE.keys()), format_func=gender_func)

#with open('model.pkl', 'rb') as model_file:
    model = pickle.load(open('modelas.sav', 'rb'))

# Create a Streamlit UI
predict_button = st.button('Predict')

if predict_button:
    #criteria = [tiredness, dry_cough, difficulty_in_breathing, sore_throat, none_sympton, pains, nasal_congestion, runny_nose, none_experiencing, age_range, gender]
    criteria = [tiredness, dry_cough, difficulty_in_breathing, sore_throat, pains, nasal_congestion, runny_nose, age_range, gender]
    prediction = model.predict([criteria])[0]  # Assuming model.predict takes a list of criteria

    if prediction == 0:
        label_text = 'None'
    elif prediction == 1:
        label_text = 'Mild'
    else:
        label_text ='Moderate'

    # Display the prediction
    st.write(f'Severity: {label_text}')
