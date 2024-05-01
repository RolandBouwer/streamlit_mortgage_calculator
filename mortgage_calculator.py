import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Mortgage Calculator')

# Input fields for property price and down payment
property_price = st.number_input('Property Price', value=545000)
down_payment = st.number_input('Down Payment (30% recommended)', value=163500)

# Slider for the duration of the loan
loan_duration = st.slider('Duration of the Loan (Years)', min_value=7, max_value=25, value=20, step=1)

# Slider for the interest rate
interest_rate = st.slider('Interest Rate (%)', min_value=0.1, max_value=10.0, value=4.79, step=0.01)

# Mortgage calculation
notary_fees_rate = 0.08  # This is the percentage for notary fees
notary_fees = property_price * notary_fees_rate
loan_amount = property_price - down_payment

monthly_interest_rate = interest_rate / 100 / 12
number_of_payments = loan_duration * 12

# Monthly mortgage payment calculation using the formula
monthly_payment = loan_amount * monthly_interest_rate / (1 - (np.power((1 + monthly_interest_rate), (-number_of_payments))))

st.markdown(f"## Estimated Monthly Payment: €{monthly_payment:,.2f}")
st.markdown(f"### Notary Fees (8%): €{notary_fees:,.2f}")
st.markdown(f"### Loan Amount: €{loan_amount:,.2f}")

# Optional: Include a pie chart to illustrate the loan amount versus interest


# Calculate interest amount
interest_amount = monthly_payment * number_of_payments - loan_amount

# Pie chart to illustrate loan amount versus interest
labels = ['Loan Amount', 'Interest Amount']
sizes = [loan_amount, interest_amount]
colors = ['#ff9999','#66b3ff']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.title('Loan Amount vs Interest Amount')
st.pyplot(fig1)