import random
import csv
# Generate a synthetic dataset
def generate_dataset(num_rows):
    education_levels = ["High School Diploma", "Associate's Degree", "Bachelor's Degree", "Master's Degree", "PhD"]
    job_satisfaction_range = (2.0, 5.0)
    salary_structures = ["Basic", "Moderate", "Competitive", "Lucrative"]
    age_range = (22,65)
    dataset = []

    for i in range(1, num_rows + 1):
        education_level = random.choice(education_levels)
        job_satisfaction = round(random.uniform(*job_satisfaction_range), 2)
        salary_structure = random.choice(salary_structures)
        age= random.randint(*age_range)

        row = [i, education_level, job_satisfaction, salary_structure, age]
        dataset.append(row)

    return dataset

# Save the dataset to a specific directory in Colab
def save_to_csv(dataset, filepath):
    with open(filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Participant_ID", "Education_Level", "Job_Satisfaction", "Salary_Structure", "Age"])
        writer.writerows(dataset)

# Generate and save a dataset with 1000 rows in a specific directory
num_rows = 1000
dataset = generate_dataset(num_rows)

# Specify the desired file path within the Colab environment
file_path_in_colab = '/content/my_dataset.csv'

# Save the dataset to the specified file path
save_to_csv(dataset, file_path_in_colab)
