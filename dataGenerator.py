import random
from faker import Faker
import csv

# Initialize Faker
fake = Faker()

# Load medical data (lists of diagnoses, procedures, etc.)
diagnoses = ["Hypertension", "Diabetes Mellitus", "Acute Appendicitis", "Pneumonia"]
procedures = ["Appendectomy", "Laparoscopic Cholecystectomy", "Endoscopy", "CT Scan"]
medications = ["Metformin", "Amoxicillin", "Atorvastatin", "Lisinopril"]
follow_ups = ["Follow up with GP in 1 week", "Consult cardiology", "Repeat blood test in 2 weeks"]

# Function to generate one discharge summary
def generate_discharge_summary():
    summary = {
        "Patient ID": fake.uuid4(),
        "Age": random.randint(18, 90),
        "Gender": random.choice(["Male", "Female"]),
        "Admission Date": fake.date_this_year(),
        "Discharge Date": fake.date_between(start_date='-5d', end_date='today'),
        "Chief Complaint": fake.sentence(nb_words=6),
        "Diagnosis": random.choice(diagnoses),
        "Procedures Performed": random.choice(procedures),
        "Treatment Given": fake.paragraph(nb_sentences=3),
        "Medications Prescribed": random.choice(medications),
        "Follow-Up Recommendations": random.choice(follow_ups),
    }
    return summary

# Generate multiple summaries
num_summaries = 1000
summaries = [generate_discharge_summary() for _ in range(num_summaries)]

# Save to a CSV file
with open('discharge_summaries.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=summaries[0].keys())
    writer.writeheader()
    writer.writerows(summaries)

print("1000 Discharge Summaries Generated and Saved to 'discharge_summaries.csv'")
