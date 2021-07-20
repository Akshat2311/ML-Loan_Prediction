#%%writefile app.py
import pickle
import streamlit as st

# Load trained model
pickle_in = open("./classifier.pkl", 'rb')
classifier = pickle.load(pickle_in)


@st.cache()
def prediction(loan_amnt, int_rate, annual_inc, dti, fico_range_low, pub_rec, revol_bal,
               revol_util, total_acc, mths_since_rcnt_il, mort_acc,
               mths_since_recent_bc, mths_since_recent_inq):
    prediction = classifier.predict([[loan_amnt, int_rate, annual_inc, dti, fico_range_low, pub_rec, revol_bal,
                                      revol_util, total_acc, mths_since_rcnt_il, mort_acc,
                                      mths_since_recent_bc, mths_since_recent_inq]])
    if prediction == 0:
        pred = "Charged Off"
    else:
        pred = "Fully Paid"
    return pred


# Main function:
def main():
    # Front end Elements:
    html_temp = """
    <div style ="background-color:black;padding:13px">
    <h1 style ="color:white;text-align:center;">Lending Club Loan Prediction ML App</h1>
    </div>
    """
    # Display aspect of front end
    st.markdown(html_temp, unsafe_allow_html=True)
    Loan_Amount = st.number_input("Loan Amount")
    Interest_Rate = st.number_input("Interest Rate")
    Annual_Income = st.number_input("Annual Income")
    Debt_To_Income_Ratio = st.number_input("Debt To Income Ratio")
    fico_range_low = st.number_input("FICO Range(Low)")
    Number_of_Derogatory_Public_Records = st.number_input("Number of derogatory public records")
    Total_credit_revolving_balance = st.number_input("Total Credit Revolving Balance")
    Revolving_line_utilization_rate = st.number_input("Revolving Line Utilization Rate")
    total_number_of_credit_lines = st.number_input("Total Number of Credit lines")
    Months_since_most_recent_installment_accounts_opened = st.number_input(
        "Months Since Most Recent Installment Accounts Opened")
    Number_of_mortgage_accounts = st.number_input("Number of Mortgage Accounts")
    Months_since_most_recent_bankcard_account_opened = st.number_input(
        "Months Since Most Recent Bankcard Account Opened")
    Months_since_most_recent_inquiry = st.number_input("Months Since Most Recent Inquiry")
    result = ""

    # When Predict is clicked:
    if st.button("Predict"):
        result = prediction(Loan_Amount, Interest_Rate, Annual_Income, Debt_To_Income_Ratio, fico_range_low,
                            Number_of_Derogatory_Public_Records, Total_credit_revolving_balance,
                            Revolving_line_utilization_rate,
                            total_number_of_credit_lines, Months_since_most_recent_installment_accounts_opened,
                            Number_of_mortgage_accounts, Months_since_most_recent_bankcard_account_opened,
                            Months_since_most_recent_inquiry)
        st.success(f"Your Loan is {result}")
        print(Loan_Amount)


if __name__ == '__main__':
    main()





