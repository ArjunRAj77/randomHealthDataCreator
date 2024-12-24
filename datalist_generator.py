import streamlit as st
import random
import pandas as pd
import io

# List of sample healthcare terms (expanded to include more terms)
HEALTHCARE_TERMS = [
    "Cardiology", "Oncology", "Neurology", "Orthopedics", "Pediatrics",
    "Radiology", "Gastroenterology", "Endocrinology", "Hematology",
    "Psychiatry", "Dermatology", "Urology", "Nephrology", "Pulmonology",
    "Immunology", "Pathology", "Ophthalmology", "Anesthesiology",
    "Rheumatology", "Pharmacology", "Virology", "Genetics",
    "Epidemiology", "Allergy", "Obstetrics", "Gynecology", "Surgery",
    "Rehabilitation", "Palliative Care", "Primary Care", "Acupuncture",
    "Audiology", "Biochemistry", "Biostatistics", "Biomedical Research",
    "Chiropractic", "Clinical Trials", "Community Health", "Critical Care",
    "Dental Surgery", "Dentistry", "Diabetology", "Dietetics",
    "Emergency Medicine", "Environmental Health", "Family Medicine",
    "Forensic Medicine", "Geriatrics", "Health Informatics",
    "Health Policy", "Health Promotion", "Homeopathy", "Hospice Care",
    "Infectious Diseases", "Kinesiology", "Laboratory Medicine",
    "Medical Genetics", "Medical Imaging", "Medical Toxicology",
    "Microbiology", "Molecular Biology", "Naturopathy", "Nuclear Medicine",
    "Nursing", "Occupational Health", "Occupational Therapy",
    "Optometry", "Orthodontics", "Osteopathy", "Palliative Medicine",
    "Parasitology", "Pharmacy", "Physical Therapy", "Physiology",
    "Plastic Surgery", "Preventive Medicine", "Prosthetics",
    "Public Health", "Radiation Oncology", "Reproductive Medicine",
    "Respiratory Therapy", "Social Work", "Speech Therapy",
    "Sports Medicine", "Toxicology", "Transplantation Medicine",
    "Traumatology", "Tropical Medicine", "Veterinary Medicine",
    "Wound Care", "Zoological Medicine", "Health Administration",
    "Health Economics", "Behavioral Science", "Clinical Psychology",
    "Cognitive Therapy", "Elderly Care", "Fitness Medicine",
    "Genomic Medicine", "Global Health", "Health Counseling",
    "Hospital Administration", "Hyperbaric Medicine", "Invasive Cardiology",
    "Medical Biophysics", "Medical Robotics", "Men's Health",
    "Military Medicine", "NanoMedicine", "Neuropsychiatry",
    "Nutritional Science", "Occupational Therapy Assistance",
    "Orthoptics", "Pediatric Surgery", "Perioperative Care",
    "Precision Medicine", "Radiologic Technology", "Regenerative Medicine",
    "Rehabilitation Counseling", "Sleep Medicine", "Substance Abuse Medicine",
    "Telemedicine", "Travel Medicine", "Urgent Care Medicine",
    "Veterinary Pathology", "Women's Health", "Yoga Therapy",
    "Zoonotic Diseases", "Clinical Ethics", "Community Nursing",
    "Disaster Medicine", "Global Mental Health", "HIV Medicine",
    "Lifestyle Medicine", "Mental Health Counseling", "Nursing Education",
    "Pharmaceutical Sciences", "Quality Improvement", "Rehabilitation Medicine",
    "Sexual Medicine", "Therapeutic Radiology", "Traditional Medicine",
    "Vascular Surgery", "Wellness Coaching", "Wilderness Medicine"
]

def generate_terms(num_terms):
    """Generate a random list of unique healthcare terms."""
    if num_terms > len(HEALTHCARE_TERMS):
        st.warning("The number of terms requested exceeds the available unique terms.")
        num_terms = len(HEALTHCARE_TERMS)
    return random.sample(HEALTHCARE_TERMS, num_terms)

def convert_to_csv(data):
    """Convert list to CSV."""
    df = pd.DataFrame(data, columns=["Healthcare Terms"])
    return df.to_csv(index=False).encode('utf-8')

def convert_to_txt(data):
    """Convert list to TXT."""
    return "\n".join(data).encode('utf-8')

# Streamlit App
def main():
    st.title("Random Healthcare Terms Generator")

    st.sidebar.header("Settings")
    num_terms = st.sidebar.number_input(
        "Number of terms to generate:", min_value=1, max_value=len(HEALTHCARE_TERMS), value=5
    )

    if st.sidebar.button("Generate"):
        terms = generate_terms(num_terms)
        st.subheader("Generated Healthcare Terms")
        st.write(terms)

        csv_data = convert_to_csv(terms)
        txt_data = convert_to_txt(terms)

        st.download_button(
            label="Download as CSV",
            data=csv_data,
            file_name="healthcare_terms.csv",
            mime="text/csv"
        )

        st.download_button(
            label="Download as TXT",
            data=txt_data,
            file_name="healthcare_terms.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()
