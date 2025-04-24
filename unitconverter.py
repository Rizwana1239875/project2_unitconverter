import streamlit as st

# Function to convert units based on predefined conversion factors or formulas
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        return value * conversions[key]
    elif unit_from == unit_to:
        return value
    else:
        return "Conversion not supported" # return a message if the conversion is not supported

st.title(" 👨‍🎓 Unit Converter") # set the title of the web app

# user input: numerical value to convert
value = st.number_input(" 👲 Enter the value:")

# dropped down to sellect unit to convert from

unit_from = st.selectbox(" 🙌 Convert from:", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox(" ✌ Convert to:", ["meter", "kilometer", "gram", "kilogram"])

# button to trigger the conversion
if st.button(" 👩‍🔧 Convert"):
    result = convert_units(value, unit_from, unit_to) # call the conversion function
    st.write(f" 🤳  Converted value: {result}") # display the result
