from gtts import gTTS
import pandas as pd
import os

# Load dataset with discharge summaries
df = pd.read_csv('discharge_summaries.csv')  # Replace with your file

# Create output directory for audio files
output_dir = 'audio_summaries'
os.makedirs(output_dir, exist_ok=True)

# Loop through each discharge summary
for index, row in df.iterrows():
    summary_text = f"""
    Discharge Summary
    
    Patient ID: {row['Patient ID']}
    Age: {row['Age']}
    Gender: {row['Gender']}
    Admission Date: {row['Admission Date']}
    Discharge Date: {row['Discharge Date']}
    
    Chief Complaint:
    {row['Chief Complaint']}
    
    Diagnosis:
    {row['Diagnosis']}
    
    Procedures Performed:
    {row['Procedures Performed']}
    
    Treatment Given:
    {row['Treatment Given']}
    
    Medications Prescribed:
    {row['Medications Prescribed']}
    
    Follow-Up Recommendations:
    {row['Follow-Up Recommendations']}
    """
    
    # Convert text to speech
    tts = gTTS(summary_text, lang='en')
    file_name = os.path.join(output_dir, f"discharge_summary_{index+1}.mp3")
    tts.save(file_name)
    print(f"Saved: {file_name}")
