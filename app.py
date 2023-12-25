import streamlit as st
import pandas as pd
import pickle as pk

model = pk.load(open('model.pkl','rb'))
scaler = pk.load(open('scaler.pkl','rb'))

st.header('Loan Predcition App')

no_of_dep = st.slider('Choose No of dependents', 0, 5)
grad = st.selectbox('Choose Education',['Graduated','Not Graduated'])
self_emp = st.selectbox('Self Emoployed ?',['Yes','No'])
Annual_Income = st.slider('Choose Annual Income', 0, 10000000)
Loan_Amount = st.slider('Choose Loan Amount', 0, 10000000)
Loan_Dur = st.slider('Choose Loan Duration', 0, 20)
Credit_History = st.slider('Choose Cibil Score', 0, 1)
Property_Area = st.selectbox('Choose Property_Area',['Rural','Semiurban','Urban'])

if grad =='Graduated':
    grad_s = 0
else:
    grad_s = 1

if self_emp =='No':
    emp_s = 0
else:
    emp_s = 1

if Property_Area =='Rural':
    Area_s = 0
elif Property_Area =='Semiurban':
    Area_s = 1
else:
    Area_s = 2


if st.button("Predict"):
    pred_data = pd.DataFrame([[no_of_dep,grad_s,emp_s,Annual_Income,Loan_Amount,Loan_Dur,Credit_History,Area_s]],
                         columns=['Dependents','Education','Self_Employed','ApplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area'])
    
    #pred_data = scaler.transform(pred_data)
    predict = model.predict(pred_data)
    if predict[0] == 1:
        st.markdown('Loan Is Approved')
    else:
        st.markdown('Loan Is Rejected')