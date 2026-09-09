class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"{":"}","[":"]","(":")"}

        while '()' in s or '{}' in s or '[]' in s:
            s=s.replace("()",'')
            s=s.replace("{}",'')
            s=s.replace("[]",'')
        return s==''
