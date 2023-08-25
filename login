import time
password={
    "log":123
}
new=input("Are you a new user:----->")
if new=='True' or new=='yes' or new=='true':
    print("Lets set you up.")
    while(1):
        login=input("Select your login_id:")
        re_login=input("Reinter login_id:")
        if login==re_login and (login not in password):
            time.sleep(1)
            pass1=int(input("Let's select a password:"))
            re_pass1=int(input("Reinter password:"))
            if pass1==re_pass1:
                print("Alldone.Your setup is complete.")
                password[login]=pass1
                break

print("Let's sign up.")
time.sleep(1)
login=input("Enter with existing id:")
pass1=int(input("Enter password:"))
if password[login]==pass1:
   print("Succesfully logged in \nFurther website")

        
