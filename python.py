class User:
    def __init__(self,first_name,last_name,email,age,member,gold_card_points):
        self.first_name = first_name
        self.last_name =last_name
        self.email = email
        self.age = age
        self.member = member
        self.gold_card_points = gold_card_points

#methods
def display_info(self):
    print(f"First Name: {self.first_name}")
    print(f"Last Name: {self.last_name}")
    print(f"email: {self.email}")
    print(f"Age: {self.age}")
    print(f"Rewards Memeber: {self.member}")
    if self.member == True:
        print(f"Gold card Points: {self.gold_card_points}")

def enroll(self):
    if self.member == False:
        print(f"You you like to sign up, {self.first_name} {self.last_name}?")
        self.member = True
        self.gold_card_points += 200
    else:
        print(f"Welcome Back, {self.first_name} {self.last_name}")

def spend_points(self,amount):
    if self.gold_card_points > amount:
        self.gold_card_points -= amount
        print(f"Points used: {amount}pts.")
        return self
    else:
        print(f"Insuffent Points. Additional Payment needed.\nPoints requested: {amount}pts. \nCurrent Amount: {self.gold_card_points}pts.")

#User database
Rebeca_Black = User('Rebeca','Black','thatfridaysong@gmail.com',22, False,0)
Kobe_Bryant = User('Kobe', 'Bryant','Coby@Bryant.com',41, True, 800)
Megan_Fox =  User('Megan','Fox',"megan@foxactor.com", 37, False, 0)

#Testing Commands
#Rebeca Black
print("----------")
print("----------")
display_info(Rebeca_Black)
print("----------")
enroll(Rebeca_Black)
print("----------")
display_info(Rebeca_Black)
print("----------")
enroll(Rebeca_Black)
print("----------")
spend_points(Rebeca_Black,50)

#KOBE
print("----------")
display_info(Kobe_Bryant)
print("----------")
enroll(Kobe_Bryant)
print("----------")
spend_points(Kobe_Bryant,80)
print("----------")
display_info(Kobe_Bryant)

#WHAT THE DOES THE FOX SAY
print("----------")
display_info(Megan_Fox)
print("----------")
enroll(Megan_Fox)
print("----------")
display_info(Megan_Fox)
print("----------")
enroll(Megan_Fox)
print("----------")
# 2nd Bonus
Megan_Fox.gold_card_points = 30
spend_points(Megan_Fox,40)