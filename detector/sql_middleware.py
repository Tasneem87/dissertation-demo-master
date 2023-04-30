
from detector.string_parser import detect_sqlia_string
from detector.randomise import randomise_check

def sqlia_detector(instance_query:str, user_input:str) -> bool:

    # detected the SQL injection strings
    if detect_sqlia_string(user_input):
        return True
    
    if randomise_check(instance_query, user_input):
        return True
    
    return False