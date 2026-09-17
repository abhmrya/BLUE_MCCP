# print(int(input("Enter a number")))

# try:
#     age = int(input("Enter a number"))
#     print(f'age is {age}')
# except ValueError as e:
#     print(e)
#     print(f'you fill wrong age ')
#     print("please enter a valid number")
# finally:
#     print("finally always run")


# class UserNotFoundError(Exception):
#     print("user not found. please try again....")

# def get_user(user_id):
#     user = None

#     if user is None:
#         raise UserNotFoundError(f"User {user_id} not found")

#     return user

# get_user(8)

import logging

logger = logging.getLogger()

try:
    something()

except Exception:
    logger.error("something wrong")
    logger.exception("Something failed")
