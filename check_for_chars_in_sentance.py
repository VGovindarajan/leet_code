import string

char_list = [chr(i) for i in range(ord('a'), ord('z'))]
char_set = set(char_list)
required = set()

def check_for_characters(s:string)-> bool:
    for c in s:
        cl = c.lower()
        if cl in char_set:
            required.add(cl)
            if len(required) == len(char_set):
                return True
    return False

def main():
    panagram = "The quick brown fox jumps over the lazy dog"
    exists = check_for_characters(panagram)
    print(exists)


if __name__ == "__main__":
    main()