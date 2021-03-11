import string
import secrets

from typing import List, Union


class Simplepass:
    def __init__(self, length: int, characters: str) -> None:
        if length > 65536:  # 2^16 characters in a password should be more than enough
            raise ValueError("pls specify a length <= 2^16")

        self.length: int = length
        self.characters: str = characters

    def generate(self, iterations: int = 1) -> Union[str, List[str]]:
        """returns one or multiple passwords,
        depending on length, given characters and iterations.
        Args:
            iterations (int): how many passwords to return
        Returns:
            Union[str, List[str]]: one or multiple passwords
        """
        if iterations == 1:
            return self._gen_pw()
        else:
            return [self._gen_pw() for _ in range(iterations)]

    def _gen_pw(self) -> str:
        """returns a password depending on lenght and given caracters
        Returns:
            str: a randomly generated password
        """
        output_password: str = ''
        for i in range(self.length):
            output_password += secrets.choice(self.characters)
        return output_password


class Complexpass(Simplepass):
    def __init__(
        self,
        length: int,
        string_method: str = "both",
        numbers: bool = True,
        special_chars: bool = False,
    ) -> None:
        characters: str = ''
        try:
            methods: dict = {
                "upper": string.ascii_uppercase,
                "lower": string.ascii_lowercase,
                "both": string.ascii_letters,
            }
            characters += methods[string_method]
        except KeyError:
            raise ValueError(
                "pls specify any of ['upper', 'lower', 'both'] for string_method"
            )

        if numbers:
            characters += string.digits
        if special_chars:
            characters += string.punctuation

        super().__init__(length=length, characters=characters)

if __name__ == "__main__":
    cp = Complexpass(20, "both", True, True)
    print(cp.generate(3))

    sp = Simplepass(20, 'abcdefghijklmnopqrstuvwxyz0123467589')
    print(sp.generate())
    print(sp.generate(2))
    print(sp.generate(3))