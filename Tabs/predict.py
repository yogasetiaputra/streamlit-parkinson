import streamlit as st

from web_functions import predict


def app(df, x, y):

    st.title('Halaman Prediksi')

    col1, col2, col3 = st.columns(3)

    with col1:
        Fo = st.number_input('Input Nilai Fo')
    with col1:
        Fhi = st.number_input('Input Nilai Fhi')
    with col1:
        Flo = st.number_input('Input Nilai Flo')
    with col1:
        Jitter = st.number_input('Input Nilai Jitter')
    with col1:
        Abs = st.number_input('Input Nilai Abs')
    with col1:
        RAP = st.number_input('Input Nilai RAP')
    with col1:
        PPQ = st.number_input('Input Nilai PPQ ')
    with col1:
        DDP = st.number_input('Input Nilai DDP ')
    with col2:
        Shimmer = st.number_input('Input Nilai Shimmer')
    with col2:
        dB = st.number_input('Input Nilai dB')
    with col2:
        APQ3 = st.number_input('Input Nilai APQ3')
    with col2:
        APQ5 = st.number_input('Input Nilai APQ5')
    with col2:
        APQ = st.number_input('Input Nilai APQ')
    with col2:
        DDA = st.number_input('Input Nilai DDA')
    with col2:
        NHR = st.number_input('Input Nilai NHR')
    with col3:
        HNR = st.number_input('Input Nilai HNR')
    with col3:
        RPDE = st.number_input('Input Nilai RPDE')
    with col3:
        DFA = st.number_input('Input Nilai GFA')
    with col3:
        spread1 = st.number_input('Input Nilai spread1')
    with col3:
        spread2 = st.number_input('Input Nilai spread2')
    with col3:
        D2 = st.number_input('Input Nilai D2')
    with col3:
        PPE = st.number_input('Input Nilai PPE')

    features = [Fo, Fhi, Flo, Jitter, Abs, RAP, PPQ, DDP, Shimmer, dB,
                APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

    # tombol prediksi
    if st.button('Prediksi'):
        prediction, score = predict(x, y, features)
        score = score
        st.info('Prediksi Sukses...')

        if (prediction == 0):
            st.warning('Orang tersebut rentang terkena penyakit Parkinson')
        else:
            st.success('Orang tersebut sehat walafiat')

        st.write('Model yang digunakan memiliki tingkat akurasi ',
                 (score*100), '%')
