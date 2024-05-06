import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))

# Create the app title
st.title('Song Hit Predictor')

# Create sliders for input features
# TODO: Make these to scale rather than just min max
danceability = st.slider('Danceability', 0.05, 0.99, 0.54)
energy = st.slider('Energy', 0.0, 1.0, 0.69)
key = st.slider('Key', 0, 11, 5)
loudness = st.slider('Loudness', -47.33, 1.14, -7.45)
mode = st.slider('Mode', 0, 1, 1)
speechiness = st.slider('Speechiness', 0.02, 0.95, 0.09)
acousticness = st.slider('Acousticness', 0.0, 0.996, 0.21)
instrumentalness = st.slider('Instrumentalness', 0.0, 0.998, 0.15)
liveness = st.slider('Liveness', 0.02, 0.99, 0.20)
valence = st.slider('Valence', 0.0, 0.98, 0.48)
tempo = st.slider('Tempo', 46.76, 213.23, 121.61)
duration_ms = st.slider('Duration (ms)', 15920, 4170227, 258170)
time_signature = st.slider('Time Signature', 0, 5, 4)
chorus_hit = st.slider('Chorus Hit', 0.0, 262.62, 40.73)
sections = st.slider('Sections', 1, 169, 11)

if st.button('Predict Hit'):
    # Collect features into an array
    input_features = np.array([[danceability, energy, key, loudness, mode, speechiness,
                                acousticness, instrumentalness, liveness, valence,
                                tempo, duration_ms, time_signature, chorus_hit, sections]])
    
    # Make prediction
    prediction = model.predict(input_features)
    result = 'Hit' if prediction[0] == 1 else 'Not a Hit'
    
    # Display the result
    st.write(f'The song is a: {result}')
