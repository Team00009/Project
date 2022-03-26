import streamlit as st

# to take input we have to use write_input

# in this case we take weight and heights\

# st.write('''
# # Check your BMI today''')

# weight = st.number_input("Enter your weight")
# height = st.number_input("Enter your height")

# weight = st.text_input("Enter your weight") # we can't directly parse the
# # input to the integer in this to get integer we need to use number_input
# height = st.text_input("Enter your height")

# for the large text area we use

# age = st.number_input("Enter your age")
# to summarize and to be fancier

# if weight!=0 and height != 0:
#     st.markdown(
#     f"""
#     * Weight: {weight}
#     * Height : {height}
#     * Age :  {age}
#     """ )

wt_units = st.selectbox("Select weight units", ("Pounds", "Kilograms"))
st.write()
try:
    if (wt_units =="Pounds"):
        weight = st.text_input("Enter your weight (lbs)")
        wt= int(weight) # converting to kgs
        height = st.text_input("Enter your height (ft and inches) ")
        height = int(height[0])*12 + int(height[2:4])

    else:
        weight = st.text_input("Enter your weight (kgs")
        wt = int(weight)

        height = st.text_input("Enter your height in (mts or cms)")
        if(float(height)<=2):
            height = float(height)
        else:
            height = int(height)/100


    bmi_cat = [(18.5,'Underweight'), (24.9,'Healthy Weight'), (29.9,'Overweight'),(float('inf'),'Obesity')]

    if (wt_units == "Pounds"):
        bmi_val = (wt*703)/height**2
    else:
        bmi_val = wt/(height**2)

    for i,j in bmi_cat:
        if(bmi_val<=i):
            st.write("Your bmi is %.2f means it is %s"%(bmi_val, j))
            break
except:
    print()




description = st.text_area("Any explanation:")
