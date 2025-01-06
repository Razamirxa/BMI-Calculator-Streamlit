import streamlit as st

def calculate_bmi(weight, height):
    """Calculate BMI given weight in kg and height in meters."""
    if height <= 0:
        return "Height must be greater than zero."
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def main():
    st.title("BMI Calculator")
    st.write("Calculate your Body Mass Index (BMI) using your weight and height.")

    # Input fields for weight and height
    weight = st.number_input("Enter your weight (in kg):", min_value=0.0, step=0.1, format="%.1f")
    height = st.number_input("Enter your height (in meters):", min_value=0.0, step=0.01, format="%.2f")

    # Calculate BMI when the button is clicked
    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            st.success(f"Your BMI is: {bmi}")
            # Provide feedback on BMI category
            if bmi < 18.5:
                st.info("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                st.info("You have a normal weight.")
            elif 25 <= bmi < 29.9:
                st.info("You are overweight.")
            else:
                st.info("You are in the obese category.")
        else:
            st.error("Please enter valid weight and height values.")

if __name__ == "__main__":
    main()
