import tkinter as tk

FONT = font = ('Arial', 12)

window = tk.Tk()
window.title('BMI Calculator')
window.minsize(300, 400)

bmi_dict = {
    "Severe Thinness": (0, 16),
    "Moderate Thinness": (16, 17),
    "Mild Thinness": (17, 18.5),
    "Normal": (18.5, 25),
    "Overweight": (25, 30),
    "Obese Class I": (30, 35),
    "Obese Class II": (35, 40),
    "Obese Class III": (40, float('inf'))
}


def classify_bmi(bmi, bmi_dict):
    for category, (low, high) in bmi_dict.items():
        if low <= bmi < high:
            return category
    return "Unknown"


def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    return bmi


def check_appropriate_bmi(weight, height):
    if weight.isnumeric() and height.isnumeric():
        return True
    return False


label_weight = tk.Label(text='Enter Weight (kg)', font=FONT)
label_weight.pack()

entry_weight = tk.Entry(width=20, font=('Arial', 12))
entry_weight.pack()

label_height = tk.Label(text='Enter Height (cm)', font=FONT)
label_height.pack()

entry_height = tk.Entry(width=20, font=('Arial', 12))
entry_height.pack()

label_result = tk.Label(text='', font=FONT)
label_result.pack()

def driver():
    weight = entry_weight.get()
    height = entry_height.get()

    if check_appropriate_bmi(weight, height):
        weight = float(weight)
        height = float(height) / 100  # cm to meter transformation
        user_bmi = calculate_bmi(float(weight), float(height))
        classification = classify_bmi(user_bmi, bmi_dict)
        result = "Your BMI is {:.2f}. Your BMI class: {}".format(user_bmi, classification)
        label_result.config(text=result)
    else:
        label_result.config(text="Please enter valid weight and height")


calculate_button = tk.Button(text='Calculate', command=driver, font=FONT)
calculate_button.pack()

window.mainloop()
