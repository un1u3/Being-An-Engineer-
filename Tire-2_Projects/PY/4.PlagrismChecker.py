'''Step 1: Plan the Features
We'll keep it simple for now:

Input two pieces of text.
Clean the text (remove unnecessary characters like punctuation and convert it to lowercase).
Split the text into words or sentences for comparison.
Compare the two texts:
Count the number of matching words or sentences.
Calculate a similarity percentage.
Display the result.'''



import re # For text cleaning 

def clean_text(text):
    text = text.lower() #convert to lower case 
    text = re.sub(r'[^\w\s]','',text) # remove puncutaions 
    return text 

#Inputs 
text1 = input("Enter first text")
text2 = input("Enter second text")

# clean the texts 
text1_clean = clean_text(text1)
text2_clean = clean_text(text2)
print("clearned Text1 :",text1_clean)
print("clearned Text2 :",text2_clean)

def split_into_words(text):
    return text.split()


words1 = split_into_words(text1_clean)    
words2 = split_into_words(text2_clean)   

print(words1)
print(words2) 


def calculate_similarity(word1,word2):
    
    set1 = set(words1)
    set2 = set(words2)
    
    common_words = set1.intersection(set2)
    similarity_percantage = (len(common_words)/len(set1.union(set2))) * 100
    return similarity_percantage, common_words


similarity, common  = calculate_similarity(words1,words2)

print(f"Similarity: {similarity:.2f}%")
print(common)
# HAHAHAHAAH