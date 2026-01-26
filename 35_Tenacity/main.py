import random
from tenacity import retry

# @retry
# def do_something_unreliable():
#     number = random.randint(0, 100)
#     print(number)
#     if number > 15:
#         raise IOError("Broken sauce, everything is hosed!!!111one")
#     else:
#         return "Awesome sauce!"



# print(do_something_unreliable())

@retry
def do_something_unreliable():
    number = random.randint(0, 10)
    print(number)
    if number != 5:
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"

print(do_something_unreliable())