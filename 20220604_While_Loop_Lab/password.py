username = input()
password = input()
password_attempt = input()
while True:
    if password_attempt == password:
        print(f'Welcome {username}!')
        break
    else:
        password_attempt = input()

# test input Nakov 1234 pass 1324 1234
# test input Gosho secret secret
