import random
import string

def randPass(length, numbers, aplpha, punctuation):
    """Generate a random string of letters, digits and special characters """
    password_characters = ""

    if numbers:
        # if numbers is true, add digits to the string
        password_characters = password_characters + string.digits
    
    if aplpha: 
        # if alpha characters is true, add ascii_letters to the string
        password_characters = password_characters + string.ascii_letters

    if punctuation:
        # if punctuation is true, add punctuation to the string
        password_characters = password_characters + string.punctuation
        
    if password_characters == "":
        # if nothing is specified, add ascii_letters, digits and punctuation to the string
        password_characters = string.ascii_letters + string.digits + string.punctuation

    # on a blank string join the random choice of characters for the length of our string
    return ''.join(random.choice(password_characters) for i in range(length))


# If we are running the file directly, lets add some arguments for our script. 
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Random Password Generator")
    parser.add_argument("-l", "--length", type=int, help="Length of password in integer, default is 14", default=14)
    parser.add_argument("-n", "--numbers", action='store_true', help="Add numbers to password")
    parser.add_argument("-a", "--alpha", action='store_true',  help="Add mixed case alpha characters to password")
    parser.add_argument("-p", "--punctuation", action='store_true', help="Add punctuation characters to password")
    parser.add_argument("-c", "--count", type=int, help="Number of passwords to generate", default=1)

    # gather arguments
    args = parser.parse_args()
    length = args.length
    numbers = args.numbers
    alpha = args.alpha
    punctuation = args.punctuation
    count = args.count

    # add our choices together to then print them in the result. 
    choices = ""
    if numbers:
        choices += " numbers"
    
    if alpha:
        choices += " letters"
    
    if punctuation:
        choices += " special characters"

    if choices == "":
        choices = " numbers, letters, and special characters"

    # print line stating the number or random strings, the length and the choices of the password
    print(f"Generating {count} Random String password of {length} characters with{choices}")
    # get the 'count' and for make a new password until the count is finished
    
    for x in range(count):
        # start x at 1 then add 1 to x
        x += 1
        # generate the password
        password = randPass(length, numbers, alpha, punctuation)
        # output the password to the screen
        print(f"{x} : {password}")
