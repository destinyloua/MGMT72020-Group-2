# Patient Class 
from descriptive_functions import get_data

class Patient: 
    """Represents a patient from the lung cancer dataset."""
    # def __init__(self, Gender, Age_Group, Country, Family_History, 
    #              Smoking_Status, Cigarettes_Per_Day, Alcohol_Use, 
    #              Exercise_Frequency, WHO_Region, Air_Pollution_Exposure, 
    #              Secondhand_Smoke): 
    #     self.gender = Gender
    #     self.age_group = Age_Group
    #     self.country = Country
    #     self.family_history = Family_History
    #     self.smoking_status = Smoking_Status
    #     self.cigarettes_per_day = Cigarettes_Per_Day
    #     self.alcohol_use = Alcohol_Use
    #     self.exercise_frequency = Exercise_Frequency
    #     self.who_region = WHO_Region
    #     self.air_pollution_exposure = Air_Pollution_Exposure
    #     self.secondhand_smoke = Secondhand_Smoke

    def __init__(self, **args): 
        self.__dict__.update(args)

    def create_patient_list(df): 
        """Returns a list of patient objects."""
        patients = [] 
        for i in range(len(df)): 
            p = Patient(**df.iloc[i].to_dict())
            patients.append(p)
        return patients

# Temporary testing (delete later)
# df = get_data("../data/lung_cancer_dataset.csv")
# patients = create_patient_list(df)
# print(len(patients))


    