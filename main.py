from colorama import Fore, Style
from random import randint

random_number = randint(1,10)

try_count = 0

print(f'\n{Fore.BLACK} < Random-Number-Game > {Style.RESET_ALL}')

while True:

    input_number = int(input(f"\n{Fore.MAGENTA}Input Number -> {Style.RESET_ALL}"))

    if input_number == random_number:

        try_count += 1

        print(f'\n{Fore.GREEN}( ✔ ) Congratulions, you found it!{Style.RESET_ALL}')
        print(f'\n{Fore.YELLOW}( 🔑 ) You found it in {try_count} tries!{Style.RESET_ALL}')

        random_number = randint(1,10)
        print(f'\n{Fore.YELLOW}( ⚙ ) A new random number has been selected!{Style.RESET_ALL}')
        try_count = 0


    elif input_number > random_number:

        try_count += 1

        print(f'\n{Fore.RED}( - ) Smaller!{Style.RESET_ALL}')

    elif input_number < random_number:

        try_count += 1

        print(f'\n{Fore.BLUE}( + ) Bigger!{Style.RESET_ALL}')