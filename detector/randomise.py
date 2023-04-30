
import random

# define the vulnerable keywords
vulnerable_keywords = ["SELECT", "AND", "OR", "FROM", "UNION", "IF", "WHERE", "ORDER BY", "GROUP BY", "HAVING", "LIMIT"]

def randomise_check(instance_query:str, user_input:str):
    randomise_query, random_number = get_randomise_query(instance_query)
    combined_query = randomise_query + user_input
    return check_query_for_sqli(combined_query, random_number)

def check_query_for_sqli(combined_query:str, random_number):

    words= combined_query.upper().split()
    for word in words:
        for keyword in vulnerable_keywords:
            if keyword in word:
                if any(char.isdigit() for char in word) and (str(random_number) in word):
                    continue
                return True
    return False

def get_randomise_query(instance_query:str):
    
    # loop through each vulnerable keyword in the query
    for keyword in vulnerable_keywords:
        # find the position of the keyword in the query string
        pos = query.upper().find(keyword)
        if pos != -1:
            # generate a random number
            random_number = str(random.randint(0, 999999))
            
            # append the random number to the keyword as a suffix
            query = query[:pos + len(keyword)] + " " + random_number + query[pos + len(keyword):]
    
    return query, random_number