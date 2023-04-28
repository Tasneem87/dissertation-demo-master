import re
from typing import List

def detect_sqlia_string(user_input: str, allowlist:List[str] = []) -> bool:
    filter_user_input = user_input
    for allow in allowlist:
        filter_user_input = re.sub(re.compile(allow.upper()), '', filter_user_input.upper())
    if re.search(r"(INSERT)|(DROP)|(OR)|(AND)", filter_user_input.upper()):
        return True
    if re.search(r"['\"`,',@,(,true,-]", filter_user_input):
        return True
    return False
