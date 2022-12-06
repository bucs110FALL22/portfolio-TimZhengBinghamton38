class StringUtility:
    def __init__(self,string):
        self.original_string = str(string)
    def __str__(self) -> str:
        """
        Returns the original string
        args: self - the inputted string
        return: self.original string - the original inputted string
        """
        return self.original_string
    def vowels(self):
        """
        Counts the vowels in a string - if there are more than 5 it returns "many"
        args: self - the inputted string
        return: vowel count or "many" if over 5 vowels 
        """
        vowelcount = 0
        for i in range(0,len(self.original_string)):
            if self.original_string[i] in ("a","A","e","E","i","I","o","O","u","U"):
                vowelcount += 1
        if vowelcount >= 5:
            return "many"
        else:
            return str(vowelcount)
    def bothEnds(self):
        """
        Returns the first and last 2 characters of a string,
        if the length of the string is too small it returns an empty string
        args: self - the inputted string
        return: either the modified string or an empty string dependent on the string size
        
        """
        stringlength = len(self.original_string)
        if len(self.original_string) > 2:
            # 0 and one will always return the first and second letter, and stringlength is subtracted by 2 and one due to the len() function returning the count starting from 1
            newstring = self.original_string[0] + self.original_string[1] + self.original_string[stringlength-2] + self.original_string[stringlength-1]
            return str(newstring)
        else:
            return str("")
    def fixStart(self):
        """
        Returns a string where all occurences of the first character is replaced by "*", except for the first letter
        args: self - the inputted string
        return: modified string
        """
        if len(self.original_string) > 1:
            firstchar = self.original_string[0]
            modifiedstring = ""
            for i in range(0,len(self.original_string)):
                if i == 0:
                    modifiedstring += self.original_string[i]
                elif firstchar in self.original_string[i]:
                    modifiedstring += "*"
                else:
                    modifiedstring += self.original_string[i]
            return str(modifiedstring)
        elif len(self.original_string) <= 1:
            return str(self.original_string)
    def asciiSum(self):
        """
        Returns the sum of the interger values of the ascii characters within the string
        args: self - the inputted string
        return: asciisum - sum of ascii values
        """
        asciisum = 0
        for i in range(0,len(self.original_string)):
            asciisum += ord(self.original_string[i])
        return asciisum
    def cipher(self):
        """
        Returns an encoded string
        args: self - the inputted string
        return: secretstring - the scrambled string
        """
        secretstring = ""
        increment = len(self.original_string)
        #this simply keeps the amount to increment by within 26
        if increment > 26:
            increment = increment - 26
        for i in range(0,len(self.original_string)):
            #this checks for spaces and if there is to add the space back in instead of running it through the cipher
            if ord(self.original_string[i]) == 32:
                secretstring += chr(32)
            else:
                secretlettervalue = (ord(self.original_string[i]) + increment)
                print(secretlettervalue)
                # there are 26 letters in the english alphabet, and 90 and 122 are the values for Z and z respectively - unless ASCII changes this doesn't change
                if secretlettervalue > ord("z"):
                    newletter = secretlettervalue - 26
                    secretstring += chr(newletter)
                # this checks to make sure an uppercase letter is not being modified
                elif secretlettervalue > ord("Z") and secretlettervalue in range(91,97):
                    newletter = secretlettervalue - 26
                    secretstring += chr(newletter)
                else:
                    secretstring += chr(secretlettervalue)
        return secretstring