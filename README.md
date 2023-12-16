# FilterPro
FilterPro is an Email Classification System designed to enhance email organization and prioritization. 
Leveraging Part-of-Speech Tagging for Urgency Assessment and Keyword Extraction for Relevance Assessment, Python libraries were employed to develop this system.
The system was evaluated using a diverse email dataset comprising 5000 emails, including over 1600 spam emails. 
Each email was ranked based on a combination of verb tenses and the number of keywords. 
To achieve precise classification, a Logistic Regression model was applied to the tagged data using the sklearn library. 

Future improvements include enhancing the classification model further and exploring the implementation of deep learning models such as transformers on the dataset.
