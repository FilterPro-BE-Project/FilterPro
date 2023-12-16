# FilterPro

FilterPro is an Email Classification System developed using Python it is designed to enhance email organization and prioritization.
The system leverages part-of-speech Tagging for Urgency Assessment and Keyword Extraction for Relevance Assessment. 
The system was evaluated using a diverse email dataset comprising 5000 emails, including over 1600 spam emails. 
Each email was ranked based on a combination of verb tenses and the number of keywords. 
To achieve precise classification, a Logistic Regression model was applied to the tagged data using the sklearn library.

Future improvements include enhancing the classification model further and exploring the implementation of deep learning models such as transformers on the dataset.
