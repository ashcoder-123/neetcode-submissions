class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += (str(len(string))+"#"+string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # Read the string...
            string = s[j+1:length+j+1]
            decoded_list.append(string)
            # Move i... 
            i = length+j+1
        return decoded_list
