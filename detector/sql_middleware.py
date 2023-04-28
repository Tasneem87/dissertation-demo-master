
from detector.string_parser import detect_sqlia_string
from detector.randomise import randomise_check

def sqlia_detector(referece_query:str, instance_query:str, user_input:str) -> bool:

    # detected the SQL injection strings
    if detect_sqlia_string(user_input):
        return True
    
    if randomise_check(referece_query, instance_query):
        return False
    
    return False