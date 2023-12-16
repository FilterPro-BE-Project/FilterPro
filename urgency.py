import pandas as pd
import spacy
import re

# Load the pre-trained spaCy model
nlp = spacy.load('en_core_web_sm')

# Load the CSV data into a DataFrame
df = pd.read_csv('emails.csv')

# Define a function to determine urgency based on NLP analysis
def determine_urgency(text):
    doc = nlp(text)
    
    # Check for urgency-related keywords
    urgency_keywords = [
        "Urgent",
    "Immediate attention required",
    "Important",
    "Emergency",
    "Critical",
    "Time-sensitive",
    "ASAP (As Soon As Possible)",
    "asap",
    "as soon as possible"
    "Action required",
    "Deadline",
    "Priority",
    "Alert",
    "Crisis",
    "Request for assistance",
    "Help needed",
    "Quick response needed",
    "Impending deadline",
    "Attention required",
    "Please read ASAP",
    "Act now",
    "Urgent matter",
    "Immediate action necessary",
    "Response needed",
    "Important update",
    "Quick decision needed",
    "High-priority issue"
        # Add more urgency keywords here
    ]
    
    # Check for non-urgency-related keywords
    non_urgency_keywords = [
        "Information",
    "Update",
    "Meeting",
    "Discussion",
    "Follow-up",
    "Agenda",
    "Notification",
    "Question",
    "Feedback",
    "Reminder",
    "Confirmation",
    "Status",
    "Routine",
    "General",
    "Inquiry",
    "Inquiry",
    "Announcement",
    "Request",
    "Introduction",
    "Greetings",
    "Feedback",
    "Reminder",
    "Communication",
    "Notification",
    "Appreciation",
    "Acknowledgment",
    "Response",
    "Schedule",
    "Calendar",
    "Invitation",
    "Confirmation",
    "Summary",
    "Report",
    "Update",
    "Milestone",
    "Review",
    "Appraisal",
    "Progress",
    "Memo",
    "Note",
    "Collaboration",
    "Teamwork",
    "Discussion",
    "Contribution",
    "Exchange",
    "Cooperation",
    "request",
    "Request for information",
    "Request for clarification"
    ]
  # Determine the tonal urgency level
   # Add more non-urgency keywords here
    
    
    if any(token.text.lower() in urgency_keywords for token in doc) and not any(token.text.lower() in non_urgency_keywords for token in doc):
        return 1
    elif any(token.text.lower() in urgency_keywords for token in doc):
        return 0.5
    elif any(token.text.lower() in non_urgency_keywords for token in doc):
        return 0.25
    else:
        # If no keywords found, default to non-urgent
        return 0

# Create a new column 'urgency' and apply the determine_urgency function
df['urgency'] = df['text'].apply(determine_urgency)

# Reset the index of the DataFrame
df.reset_index(drop=True, inplace=True)

# Save the updated DataFrame to a new CSV file
df.to_csv('updated_email.csv',index=False) 