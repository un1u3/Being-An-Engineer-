def madlib_generaor():
    
    story = """
    Once upon a time, there was a [word1] [word2] who loved to [word3]. 
    One day, the [word4] found a [word1] treasure chest full of [word4]. 
    Excited, the [word2] decided to [word3] all day long. 
    It was truly a [word1] adventure!
    """
    
    
    
    
    placeholders = ['word1','word2','word3','word4']
    
    userinput = {}
    
    for placeholder in placeholders:
        userinput[placeholder] = input("Enter ")
        
    for key, value in userinput.items():
        story = story.replace(f"[{key}]",value)
        
        
        
    print(story)
        
    
    
madlib_generaor()
    