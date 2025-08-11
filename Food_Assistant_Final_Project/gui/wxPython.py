import wx
import pandas as pd
import joblib

class FitnessApp(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(FitnessApp, self).__init__(*args, **kwargs)
        self.model_diet = joblib.load("../Models/diet_model_rfc.pkl")
        self.model_exercises = joblib.load("../Models/exercise_model_rfc.pkl")
        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)

        self.SetBackgroundColour('#87b3ff')
        heading_box = wx.StaticBox(pnl, pos=(120, 20), size=(940, 60))
        heading_box.SetBackgroundColour('#A8A8A8')
        heading_font = wx.Font(35, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        info_font = wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        heading = wx.StaticText(pnl, label="Smart Fitness Assistant", pos=(410, 35))
        heading.SetFont(heading_font)

        wx.StaticLine(pnl, pos=(28,90), size=(1140,2))

        info_text = wx.StaticText(pnl, label="Smart Fitness Assistant gives you a personalized diet and exercise plan\n based on your body and health details. Just enter your info — and get smart, \ninstant recommendations to reach your fitness goals.", pos=(140, 134), style=wx.ALIGN_CENTER)
        info_text.SetFont(info_font)

        input_box = wx.StaticBox(pnl, pos=(20, 240), size=(450, 630))
        input_box.SetBackgroundColour('#A8A8A8')


        input_heading = wx.StaticText(pnl, label="Enter Your Fitness Details:", pos=(45, 260))
        input_font = wx.Font(17, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        input_heading.SetFont(input_font)

        label_font = wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD)

        results_font = wx.Font(30, wx.DEFAULT, wx.NORMAL, wx.BOLD)


        self.sex_desc = wx.StaticText(pnl, label="Select Your Gender:", pos=(45, 300))
        self.sex_choice = wx.Choice(pnl, choices=["Male", "Female"], pos=(195, 298))
        self.sex_choice.SetSelection(0)
        self.sex_desc.SetFont(label_font)

        self.age_desc = wx.StaticText(pnl, label="Enter Your Age:", pos=(45, 340))
        self.age_input = wx.TextCtrl(pnl, pos=(165, 335), size=(100, -1))
        self.age_desc.SetFont(label_font)

        self.height_desc = wx.StaticText(pnl, label="Enter Your Height (m):", pos=(45, 380))
        self.height_input = wx.TextCtrl(pnl, pos=(218, 375), size=(100, -1))
        self.height_desc.SetFont(label_font)

        self.weight_desc = wx.StaticText(pnl, label="Enter your Weight (kg):", pos=(45, 420))
        self.weight_input = wx.TextCtrl(pnl, pos=(218, 415), size=(100, -1))
        self.weight_desc.SetFont(label_font)

        self.hypertension_desc = wx.StaticText(pnl, label="Do you have hypertension:", pos=(45, 460))
        self.radio_hp_yes = wx.RadioButton(pnl, label='Yes', pos=(245, 460), style=wx.RB_GROUP)
        self.radio_hp_no = wx.RadioButton(pnl, label='No', pos=(295, 460))
        self.radio_hp_no.SetValue(True)
        self.hypertension_desc.SetFont(label_font)

        self.diabet_desc = wx.StaticText(pnl, label="Do you have diabets:", pos=(45, 500))
        self.radio_d_yes = wx.RadioButton(pnl, label='Yes', pos=(205, 500), style=wx.RB_GROUP)
        self.radio_d_no = wx.RadioButton(pnl, label='No', pos=(255, 500))
        self.radio_d_no.SetValue(True)
        self.diabet_desc.SetFont(label_font)

        self.goal_desc = wx.StaticText(pnl, label="Select Your Fitness Goal:", pos=(45, 540))
        self.goal_choice = wx.Choice(pnl, choices=["Weight Gain", "Weight Loss"], pos=(232, 538))
        self.goal_choice.SetSelection(0)
        self.goal_desc.SetFont(label_font)

        image = wx.Image('../resources/health.png', wx.BITMAP_TYPE_ANY)
        image = image.Scale(400, 140, wx.IMAGE_QUALITY_HIGH)
        bitmap = wx.StaticBitmap(pnl, bitmap=wx.Bitmap(image), pos=(44,660))

        result_box = wx.StaticBox(pnl, pos=(730, 240), size=(450, 630))
        result_box.SetBackgroundColour('#A8A8A8')

        fitness_image = wx.Image('../resources/fitness.jpg', wx.BITMAP_TYPE_ANY)
        fitness_image = fitness_image.Scale(350, 180, wx.IMAGE_QUALITY_HIGH)
        bitmap_fitness = wx.StaticBitmap(pnl, bitmap=wx.Bitmap(fitness_image), pos=(740,250))

        diet_image = wx.Image('../resources/diet.jpeg', wx.BITMAP_TYPE_ANY)
        diet_image = diet_image.Scale(350, 180, wx.IMAGE_QUALITY_HIGH)
        bitmap_diet = wx.StaticBitmap(pnl, bitmap=wx.Bitmap(diet_image), pos=(820, 462))

        bench_image = wx.Image('../resources/bench_press.jpg', wx.BITMAP_TYPE_ANY)
        bench_image = bench_image.Scale(350, 180, wx.IMAGE_QUALITY_HIGH)
        bitmap_bench = wx.StaticBitmap(pnl, bitmap=wx.Bitmap(bench_image), pos=(740, 680))




        self.calculate_btn = wx.Button(pnl, label='Calculate Health Stats', pos=(150, 590), style=wx.NO_BORDER, size=(160, 40))
        self.calculate_btn.SetBackgroundColour("green")
        self.calculate_btn.SetForegroundColour("black")
        self.calculate_btn.Bind(wx.EVT_BUTTON, self.OnCalculate)

        self.bmi = wx.StaticText(pnl, label="BMI", pos=(582, 240))
        self.bmi.SetFont(input_font)

        self.line_bmi = wx.StaticLine(pnl, pos=(485, 260), size=(230, 2))

        self.bmi_score = wx.StaticText(pnl, label="Score", pos=(582, 270))
        self.bmi_score.SetFont(input_font)

        self.level = wx.StaticText(pnl, label="Level", pos=(577, 325))
        self.level.SetFont(input_font)

        self.line_level = wx.StaticLine(pnl, pos=(485, 345), size=(230, 2))

        self.level_score = wx.StaticText(pnl, label="Score", pos=(572, 355))
        self.level_score.SetFont(input_font)

        self.bmr = wx.StaticText(pnl, label="BMR", pos=(577, 410))
        self.bmr.SetFont(input_font)

        self.line_bmr = wx.StaticLine(pnl, pos=(485, 430), size=(230, 2))

        self.bmr_score = wx.StaticText(pnl, label="Score", pos=(570, 440))
        self.bmr_score.SetFont(input_font)

        self.tdee = wx.StaticText(pnl, label="TDEE", pos=(577, 495))
        self.tdee.SetFont(input_font)

        self.line_tdee = wx.StaticLine(pnl, pos=(485, 515), size=(230, 2))

        self.tdee_score = wx.StaticText(pnl, label="Score", pos=(567, 525))
        self.tdee_score.SetFont(input_font)

        self.target_calories = wx.StaticText(pnl, label="Target Calories", pos=(535, 580))
        self.target_calories.SetFont(input_font)

        self.line_calories = wx.StaticLine(pnl, pos=(485, 600), size=(230, 2))

        self.target_calories_score = wx.StaticText(pnl, label="Score", pos=(572, 610))
        self.target_calories_score.SetFont(input_font)




        self.act_factor = wx.StaticText(pnl, label="Activity Factor", pos=(537, 665))
        self.act_factor.SetFont(input_font)

        self.line_act = wx.StaticLine(pnl, pos=(485, 685), size=(230, 2))

        self.act_factor_score = wx.StaticText(pnl, label="Score", pos=(582, 695))
        self.act_factor_score.SetFont(input_font)


        self.diet_btn = wx.Button(pnl, label='Show Fitness Plan', pos=(525, 735), style=wx.NO_BORDER, size=(150, 40))
        self.diet_btn.SetBackgroundColour("green")
        self.diet_btn.SetForegroundColour("white")
        self.diet_btn.Bind(wx.EVT_BUTTON, self.OnDiet)



        #Hiding elements
        self.bmi.Hide()
        self.bmi_score.Hide()
        self.line_bmi.Hide()

        self.level.Hide()
        self.level_score.Hide()
        self.line_level.Hide()

        self.bmr.Hide()
        self.bmr_score.Hide()
        self.line_bmr.Hide()

        self.tdee.Hide()
        self.tdee_score.Hide()
        self.line_tdee.Hide()

        self.target_calories.Hide()
        self.target_calories_score.Hide()
        self.line_calories.Hide()

        self.act_factor.Hide()
        self.act_factor_score.Hide()
        self.line_act.Hide()

        self.diet_btn.Hide()

        self.SetSize((1200, 960))
        self.SetTitle("Smart Fitness Assistant")
        self.Centre()

    def OnCalculate(self, event):
        try:
            if not self.age_input.GetValue().strip() or not self.height_input.GetValue().strip() or not self.weight_input.GetValue().strip():
                wx.MessageBox("Please fill in Age, Height, and Weight fields before calculating.", "Missing Data",
                              wx.OK | wx.ICON_WARNING)
                return

            age = int(self.age_input.GetValue())
            height = float(self.height_input.GetValue())
            weight = float(self.weight_input.GetValue())

            if age <= 0 or height <= 0 or weight <= 0:
                wx.MessageBox("Age, Height, and Weight must be positive values.", "Invalid Input",
                              wx.OK | wx.ICON_WARNING)
                return

            age = int(self.age_input.GetValue())
            height = float(self.height_input.GetValue())
            weight = float(self.weight_input.GetValue())



            bmi = weight / (height ** 2)

            if bmi < 18.5:
                level = "Underweight"
            elif bmi < 25:
                level = "Normal"
            elif bmi < 30:
                level = "Overweight"
            else:
                level = "Obuse"


            sex = self.sex_choice.GetStringSelection()
            if sex == "Male":
                bmr = 10 * weight + 6.25 * height * 100 - 5 * age + 5
            else:
                bmr = 10 * weight + 6.25 * height * 100 - 5 * age - 161

            goal = self.goal_choice.GetStringSelection()
            if goal == "Weight Loss":
                fitness_type = "Cardio Fitness"
            else:
                fitness_type = "Muscular Fitness"

            if fitness_type == "Cardio Fitness":
                activity_factor = 1.55 if goal == "Weight Loss" else 1.375
            else:
                activity_factor = 1.725 if goal == "Weight Gain" else 1.55

            tdee = bmr * activity_factor

            if goal == "Weight Loss":
                target_calories = tdee - 500
            elif goal == "Weight Gain":
                target_calories = tdee + 300
            else:
                target_calories = tdee

            self.bmi_score.SetLabel(f'{bmi:.2f}')
            self.level_score.SetLabel(level)
            self.bmr_score.SetLabel(f'{bmr:.2f}')
            self.tdee_score.SetLabel(f'{tdee:.2f}')
            self.target_calories_score.SetLabel(f'{target_calories:.2f}')
            self.act_factor_score.SetLabel(f'{activity_factor:.3f}')

            self.bmi.Show()
            self.bmi_score.Show()
            self.line_bmi.Show()

            self.level.Show()
            self.level_score.Show()
            self.line_level.Show()

            self.bmr.Show()
            self.bmr_score.Show()
            self.line_bmr.Show()

            self.tdee.Show()
            self.tdee_score.Show()
            self.line_tdee.Show()

            self.target_calories.Show()
            self.target_calories_score.Show()
            self.line_calories.Show()


            self.act_factor.Show()
            self.act_factor_score.Show()
            self.line_act.Show()

            self.diet_btn.Show()

        except ValueError:
            wx.MessageBox("Please enter valid numeric values for Age, Height, and Weight.", "Invalid Input", wx.OK | wx.ICON_ERROR)
        except Exception as e:
            wx.MessageBox(f"Input error: {e}", "Error", wx.OK | wx.ICON_ERROR)


    def OnDiet(self, event):
        try:
            sex = 1 if self.sex_choice.GetStringSelection() == "Male" else 0
            age = int(self.age_input.GetValue())
            height = float(self.height_input.GetValue())
            weight = float(self.weight_input.GetValue())
            hypertension = 1 if self.radio_hp_yes.GetValue() else 0
            diabetes = 1 if self.radio_d_yes.GetValue() else 0
            goal = 1 if self.goal_choice.GetStringSelection() == "Weight Gain" else 0

            bmi = round(weight / (height ** 2), 2)

            if bmi < 18.5:
                level = 0  # Underweight
            elif 18.5 <= bmi < 25:
                level = 1  # Normal
            elif 25 <= bmi < 30:
                level = 2  # Overweight
            else:
                level = 3  # Obuse

            if goal == "Weight Loss":
                fitness_type = 0 #Cardio Fitness
            else:
                fitness_type = 1 #Muscular Fitness

            if fitness_type == 0:
                activity_factor = 1.55 if goal == 0 else 1.375
            else:
                activity_factor = 1.725 if goal == 1 else 1.55

            if sex == 1:  # Male
                bmr = 10 * weight + 6.25 * (height * 100) - 5 * age + 5
            else:  # Female
                bmr = 10 * weight + 6.25 * (height * 100) - 5 * age - 161

            tdee = bmr * activity_factor

            target_calories = tdee + 300 if goal == 1 else tdee - 500

            dataframe = pd.DataFrame([{
                'Sex': sex,
                'Age': age,
                'Height': height,
                'Weight': weight,
                'Hypertension': hypertension,
                'Diabetes': diabetes,
                'BMI': bmi,
                'Level': level,
                'Fitness Goal': goal,
                'Fitness Type': fitness_type,
                'Activity Factor': activity_factor,
                'BMR': bmr,
                'TDEE': tdee,
                'Target Calories': target_calories
            }])

            FEATURES_EX = ['Age', 'Weight', 'Hypertension', 'Diabetes', 'BMI', 'Level', 'Target Calories']
            x_ex = dataframe[FEATURES_EX]

            prediction_ex = self.model_exercises.predict(x_ex)[0]

            dataframe['Exercises'] = prediction_ex

            FEATURES_DIET = ['Age', 'Weight', 'Hypertension', 'Diabetes', 'BMI', 'Level', 'Exercises', 'Target Calories']
            x_diet = dataframe[FEATURES_DIET]
            prediction_diet = self.model_diet.predict(x_diet)[0]

            exercise_map = {
                0: "Squats, deadlifts, bench presses, and overhead presses",
                1: "Squats, yoga, deadlifts, bench presses, and overhead presses",
                2: "Brisk walking, cycling, swimming, running , or dancing.",
                3: "Walking, Yoga, Swimming.",
                4: "brisk walking, cycling, swimming, or dancing."
            }

            predicted_exercises = exercise_map[prediction_ex]

            vegetables, protein, juice = prediction_diet.split(';')

            diet_message = (
                f"Your Personalized Diet Plan:\n\n"
                f"{vegetables}\n\n"
                f"{protein}\n\n"
                f"{juice}\n\n\n"
                f"Recommended Exercises:\n\n"
                f"{predicted_exercises}\n\n\n"
            )

            # Show in a message box
            wx.MessageBox(diet_message, "Diet Plan", wx.OK | wx.ICON_INFORMATION)




        except Exception as e:
            wx.MessageBox(f"Грешка: {str(e)}", "Error", wx.OK | wx.ICON_ERROR)




def main():
    app = wx.App()
    frame = FitnessApp(None)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()