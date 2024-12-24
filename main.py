import streamlit as st
from faker import Faker
import random
from gtts import gTTS
import pandas as pd
import io

# Initialize Faker
fake = Faker()

# Sample medical data
diagnoses = ["Hypertension", "Diabetes Mellitus", "Acute Appendicitis", "Pneumonia"]
procedures = ["Appendectomy", "Laparoscopic Cholecystectomy", "Endoscopy", "CT Scan"]
medications = ["Metformin", "Amoxicillin", "Atorvastatin", "Lisinopril"]
follow_ups = ["Follow up with GP in 1 week", "Consult cardiology", "Repeat blood test in 2 weeks"]

# Generate a single discharge summary
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
def generate_summaries(num_summaries):
    summaries = [generate_discharge_summary() for _ in range(num_summaries)]
    return pd.DataFrame(summaries)

# Convert a summary to audio and return as BytesIO
def text_to_audio(summary_text):
    tts = gTTS(summary_text, lang='en')
    audio_buffer = io.BytesIO()
    tts.save(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer

# Streamlit App
def main():
    st.title("Discharge Summary Generator and Audio Converter")
    st.info(
        "This app allows you to generate discharge summaries and convert them to audio files for healthcare training purposes."
    )
    st.sidebar.header("Settings")

    # Input: Number of summaries to generate
    num_summaries = st.sidebar.number_input(
        "Number of discharge summaries to generate:",
        min_value=1,
        max_value=1000,
        value=10
    )
    
    # Generate summaries
    if st.sidebar.button("Generate Summaries"):
        with st.spinner("Generating summaries..."):
            summaries = generate_summaries(num_summaries)
            st.session_state["summaries"] = summaries
            st.success(f"{num_summaries} discharge summaries generated!")
            st.dataframe(summaries)

            # Allow user to download the summaries as CSV
            csv = summaries.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Summaries as CSV",
                data=csv,
                file_name="discharge_summaries.csv",
                mime="text/csv"
            )

    # Convert to audio
    if "summaries" in st.session_state:
        summaries = st.session_state["summaries"]

        st.header("Convert Summaries to Audio")
        max_audio = 50
        num_to_convert = st.slider(
            "Select the number of summaries to convert to audio:",
            min_value=1,
            max_value=min(max_audio, len(summaries)),
            value=min(max_audio, len(summaries))
        )

        if st.button("Convert to Audio"):
            with st.spinner("Converting summaries to audio..."):
                for i, summary in summaries.head(num_to_convert).iterrows():
                    summary_text = f"""
                    Discharge Summary

                    Patient ID: {summary['Patient ID']}
                    Age: {summary['Age']}
                    Gender: {summary['Gender']}
                    Admission Date: {summary['Admission Date']}
                    Discharge Date: {summary['Discharge Date']}

                    Chief Complaint:
                    {summary['Chief Complaint']}

                    Diagnosis:
                    {summary['Diagnosis']}

                    Procedures Performed:
                    {summary['Procedures Performed']}

                    Treatment Given:
                    {summary['Treatment Given']}

                    Medications Prescribed:
                    {summary['Medications Prescribed']}

                    Follow-Up Recommendations:
                    {summary['Follow-Up Recommendations']}
                    """
                    audio_buffer = text_to_audio(summary_text)
                    st.download_button(
                        label=f"Download Audio for Summary {i + 1}",
                        data=audio_buffer,
                        file_name=f"discharge_summary_{i + 1}.mp3",
                        mime="audio/mpeg"
                    )
                st.success(f"{num_to_convert} summaries converted to audio!")

if __name__ == "__main__":
    main()
