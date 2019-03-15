# import these modules 
from nltk.stem import WordNetLemmatizer 
  
lemmatizer = WordNetLemmatizer() 

print("rocks :", lemmatizer.lemmatize("rocks")) 
print("ultimately :", lemmatizer.lemmatize("ultimately")) 