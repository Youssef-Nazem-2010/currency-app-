#step 1: Importing lib
import requests 
import streamlit as st

#Step 2: Gettig exchance rate
def get_conversion_rates(base_currency): 
    apikey = "4c8b3000d400b7e775524815"
    req = f"https://v6.exchangerate-api.com/v6/{apikey}/latest/{base_currency}"

    response = requests.get(req)
    

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return 'An error occured'

#Step 3: Streamlit main app
st.title('💹Currency app🏦')
st.subheader('💱Convert all currencies in a real-time!')

currencies = [
    "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN",
    "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL",
    "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY",
    "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP",
    "ERN", "ETB", "EUR", "FJD", "FKP", "FOK", "GBP", "GEL", "GGP", "GHS",
    "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF",
    "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD",
    "JPY", "KES", "KGS", "KHR", "KID", "KMF", "KRW", "KWD", "KYD", "KZT",
    "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD",
    "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN",
    "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK",
    "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR",
    "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", "SLL", "SOS", "SRD",
    "SSP", "STN", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY",
    "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VES",
    "VND", "VUV", "WST", "XAF", "XCD", "XOF", "XPF", "YER", "ZAR", "ZMW",
    "ZWL"
]

col1, col2 = st.columns(2)

with col1:
    base_currency = st.selectbox('From currency', currencies, index=0)

with col2:
    taregt_currency = st.selectbox('To currency',currencies, index=1)

amount = st.number_input('Enter the amount:', 1, value=1, step=1)


rates = get_conversion_rates(base_currency)['conversion_rates']

if st.button('Calculate Rate'):
    exchange_rate = rates[taregt_currency]
    total = exchange_rate * amount
    st.success(f'{amount} {base_currency} = {total:,} {taregt_currency}')