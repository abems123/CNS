import string

alphabet = string.ascii_uppercase

class Rotor:
    """
    initial_value is a string
    """
    def __init__(self, initial_value):
        self.initial_value = initial_value
        self.value = initial_value
        self.first_time = True

    def shift_left(self):
        self.value = self.value[1:26] + self.value[0]

    """ shifts the value of the rotor with one value to the left and return true if it is a full rotation """
    def rotate(self):
        self.shift_left()
        return self.value == self.initial_value

    """ 
        letter is the number of the input int
        can_advance means if the rotor can rotate
        
        @:return int is the encrypted letter
     """
    def change(self, letter):
        if not isinstance(letter, int):
            raise TypeError('letter must be an int')

        returned_letter = ord(self.value[letter]) - ord('A')

        return returned_letter

    def index(self, letter):
        return self.value.index(letter)

class EnigmaMachine:
    def __init__(self, rotor1, rotor2, rotor3):
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3


    """
        When typing on a normal Enigma Machine, each letter gets changed 7 to 9 times before getting lighted up on the light board.
        But for this challenge, there is no mention for the plug board, or the reflector.
        So we have only the three rotors, which should change the letter 6 times according to the normal implementation.
        But I'm not sure if that's gonna work since we don't have enough information
        
        @:return int is the encrypted letter's order between 0 and 25
    """
    def type(self, letter):
        if isinstance(letter, str) and len(letter) != 1:
            raise Exception('Invalid letter')
        elif isinstance(letter, int) and not 1 <= letter <= 26:
            raise Exception('Letter must be between 1 and 26')

        rotate_first_rotor = self.rotor1.rotate()
        rotate_second_rotor = self.rotor2.rotate() if rotate_first_rotor else False
        if rotate_second_rotor:
            self.rotor3.rotate()

        typed_letter = letter if isinstance(letter, int) else ord(letter.upper()) - ord('A')
        result = self.encrypt(typed_letter)


        return result

    def encrypt(self, letter):
        encrypted_letter = (
            self.rotor1.change(
            self.rotor2.change(
            self.rotor3.change(letter))))

        return encrypted_letter

    def encrypt_message(self, message):
        result = ''
        for letter in message:
            result +=  alphabet[self.type(letter)] if letter.upper() in alphabet else letter

        return result

    def fake_decrypt(self, message):
        result = ''
        for letter in message:
            if letter.upper() not in alphabet:
                result += letter
                continue

            rotate_first_rotor = self.rotor1.rotate()
            rotate_second_rotor = self.rotor2.rotate() if rotate_first_rotor else False
            if rotate_second_rotor:
                self.rotor3.rotate()

            i3 = self.rotor3.index(letter)
            c3 = alphabet[i3]

            i2 = self.rotor2.index(c3)
            c2 = alphabet[i2]

            i1 = self.rotor1.index(c2)
            c1 = alphabet[i1]

            result += c1

        return result
