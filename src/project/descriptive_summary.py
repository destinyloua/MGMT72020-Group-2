import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DescriptiveSummary:
    def __init__(self, data):
        self.data = data

    def get_category_count(self, category, df):
        """Returns a count of the number of patients in each category."""
        return self.data[category].value_counts(dropna=True)
    
    def gender_pie_chart(self):
        """Generates a pie chart for gender distribution."""
        gender_count = self.get_category_count("Gender", self.data)
        plt.pie(gender_count, 
                labels=gender_count.index, 
                autopct="%1.1f%%",
                startangle=90,
                colors=["#66b3ff", "#ff9999"])
        plt.title("Gender Distribution")
        plt.axis("equal")
        plt.show()

    def age_group_bar_chart(self):
        """Generates a bar chart for age group distribution."""
        age_order = ["30-39", "40-49", "50-59", "60-69", "70-79", "80-89"]
        age_group_counts = self.get_category_count("Age_Group", self.data)
        age_group_counts_ordered = age_group_counts.reindex(age_order)

        bars = plt.bar(age_group_counts_ordered.index, 
                       age_group_counts_ordered.values, 
                       color="#66b3ff",
                       edgecolor="black")
        plt.title("Age Group Distribution")
        plt.xlabel("Age Group")
        plt.ylabel("Number of Patients")
        plt.bar_label(bars)
        plt.show()

    def smoking_status_bar_chart(self):
        """Generates a bar chart for smoking status distribution."""
        smoking_status_counts = self.get_category_count("Smoking_Status", self.data)

        bars = plt.bar(smoking_status_counts.index, 
                       smoking_status_counts.values, 
                       color = "gray",
                       edgecolor="black")
        plt.title("Smoking Status Distribution")
        plt.xlabel("Smoking Status")
        plt.ylabel("Number of Patients")
        plt.bar_label(bars)
        plt.show()

    def alcohol_use_bar_chart(self):
        """Generates a bar chart for alcohol use distribution."""
        alcohol_order = ["No Alcohol", "Moderate", "Heavy"]
        alcohol_use_counts = self.get_category_count("Alcohol_Use", self.data)
        alcohol_use_counts_ordered = alcohol_use_counts.reindex(alcohol_order)

        bars = plt.bar(alcohol_use_counts_ordered.index, 
                       alcohol_use_counts_ordered.values, 
                       color = "skyblue",
                       edgecolor="black")
        plt.title("Alcohol Use Distribution")
        plt.xlabel("Alcohol Use")
        plt.ylabel("Number of Patients")
        plt.bar_label(bars)
        plt.show()

    def cigs_per_day_hist(self):
        """Generates a histogram for cigarettes per day distribution."""
        plt.hist(self.data["Cigarettes_Per_Day"], 
                 bins = 8, 
                 color='orange', 
                 edgecolor='black')
        plt.title("Cigarettes Per Day Distribution")
        plt.xlabel("Cigarettes Per Day")
        plt.ylabel("Number of Patients")
        plt.show()

    def exercise_freq_bar_chart(self):
        """Generates a bar chart for exercise frequency distribution."""
        exercise_order = ["Low", "Moderate", "High"]
        exercise_freq_counts = self.get_category_count("Exercise_Frequency", self.data)
        exercise_freq_counts_ordered = exercise_freq_counts.reindex(exercise_order)

        bars = plt.bar(exercise_freq_counts_ordered.index, 
                exercise_freq_counts_ordered.values, 
                color = "lightgreen",
                edgecolor="black")
        plt.title("Exercise Frequency Distribution")
        plt.xlabel("Exercise Frequency")
        plt.ylabel("Number of Patients")
        plt.bar_label(bars)
        plt.show()
    
    def air_pollution_heatmap(self):
        """Generates a heatmap showing air pollution exposure by WHO region."""
        cross_tab_df = pd.crosstab(self.data["WHO_Region"], self.data["Air_Pollution_Exposure"])
        air_order = ["Low", "Moderate", "High"]
        air_pollution_ordered = cross_tab_df.reindex(air_order, axis=1)

        sns.heatmap(air_pollution_ordered, 
                    annot=True, 
                    fmt="d", 
                    cmap="coolwarm")
        plt.title("Air Pollution Exposure by WHO Region")
        plt.xlabel("Air Pollution Level")
        plt.ylabel("WHO Region")    
        plt.show()