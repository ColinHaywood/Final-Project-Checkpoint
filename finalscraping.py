import requests
import re
import requests_cache
from bs4 import BeautifulSoup as bs

# a = open("Greatsword.html")
# greatsword_html = a.read()



# RuinsGreatswordResponse = requests.get("https://eldenring.wiki.fextralife.com/Ruins+Greatsword")
# RuinsGreatswordSoup = bs(RuinsGreatswordResponse.text, 'html.parser')
# #Str 50, Int 16

# AxeofGodrickResponse = requests.get("https://eldenring.wiki.fextralife.com/Axe+of+Godrick")
# AxeofGodrickSoup = bs(AxeofGodrickResponse.text, 'html.parser')
# #Str 34, Dex 22

GreatswordResponse = requests.get("https://eldenring.wiki.fextralife.com/Greatsword")
GreatswordSoup = bs(GreatswordResponse.text, 'html.parser')
#Str 31, Dex 12

# BoltofGransaxResponse = requests.get("https://eldenring.wiki.fextralife.com/Bolt+of+Gransax")
# BoltofGransaxSoup = bs(BoltofGransaxResponse.text, 'html.parser')
# #Str 20, Dex 40

# DragonKingCragbladeResponse = requests.get("https://eldenring.wiki.fextralife.com/Dragon+King's+Cragblade")
# DragonKingCragbladeSoup = bs(DragonKingCragbladeResponse.text, 'html.parser')
# #Str 18, Dex 37

# HandofMaleniaResponse = requests.get("https://eldenring.wiki.fextralife.com/Hand+of+Malenia")
# HandofMaleniaSoup = bs(HandofMaleniaResponse.text, 'html.parser')
# #Str 16, Dex 48

# GoldenOrderGreatswordResponse = requests.get("https://eldenring.wiki.fextralife.com/Golden+Order+Greatsword")
# GoldenOrderGreatswordSoup = bs(GoldenOrderGreatswordResponse.text, 'html.parser')
# #Str 16, Dex 21, Fai 28

# DarkMoonGreatswordResponse = requests.get("https://eldenring.wiki.fextralife.com/Dark+Moon+Greatsword")
# DarkMoonGreatswordSoup = bs(DarkMoonGreatswordResponse.text, 'html.parser')
# #Str 16, Dex 11, Int 38

# MoonveilResponse = requests.get("https://eldenring.wiki.fextralife.com/Moonveil")
# MoonveilSoup = bs (MoonveilResponse.text, 'html.parser')
# #Str 12, Dex 18, Int 23

# SwordofNightFlameResponse = requests.get("https://eldenring.wiki.fextralife.com/Sword+of+Night+and+Flame")
# SwordofNightFlameSoup = bs(SwordofNightFlameResponse.text, 'html.parser')
# #Str 12, Dex 12, Int 24, Fai 24

# BattleAxeResponse = requests.get("https://eldenring.wiki.fextralife.com/Battle+Axe")
# BattleAxeSoup = bs(BattleAxeResponse.text, 'html.parser')
# #Str 12, Dex 8

# FlailResponse = requests.get("https://eldenring.wiki.fextralife.com/Flail")
# FlailSoup = bs(FlailResponse.text, 'html.parser')
# #Str 10, Dex 18

# BastardStarsResponse = requests.get("https://eldenring.wiki.fextralife.com/Bastard's+Stars")
# BastardStarsSoup = bs(BastardStarsResponse.text, 'html.parser')
# #Str 8, Dex 22, Int 22

# ShortSwordResponse = requests.get("https://eldenring.wiki.fextralife.com/Straight+Swords")
# ShortSwordSoup = bs(ShortSwordResponse.text, 'html.parser')
# #Str 8, Dex 10

###need to cache these. how?

###is this acceptable auto-cache method?
###currently set to expire after 30 minutes
requests_cache.install_cache(cache_name="Elden Ring Wiki Cache", backend="sqlite", expire_after=1800)
#just do filter

#As per discussion with Professor Madamanchi on 4/29, using filter instead of tree as solution

RuinsGreatSwordStr = []
AxeofGodrickStr = []
GreatswordStr = []
BoltofGransaxStr = []
DragonKingCragbladeStr = []
HandofMaleniaStr  = []
GoldenOrderGreatswordStr = []
DarkMoonGreatswordStr = []
MoonveilStr = []




def run(tree):
    """parses tree for input stats"""
    ###(string, integer, integer, integer, integer)
    weapon_name, strength_req, dexterity_req, intelligence_req, faith_req = tree

    ###example trees
    ###these need to be populated from BS parsings of the requests
    ###how should these stack/compare?
    SwordofNightFlame_tree = \
        ("Sword of Night and Flame", 12, 12, 24, 24)
    ShortSword_tree = \
        ("Short Sword", 8, 10, 0, 0)
    GoldenOrderGreatsword_tree = \
        ("Golden Order Greatsword", 16, 21, 0, 28)
    Moonveil_tree = \
        ("Moonveil", 12, 18, 23, 0)

#at each node have all of the possible weapons


#putlist at each node
#or put code for list comprehension at the node
#node at str 16



all_list_items = GreatswordSoup.find_all('div', class_='infobox')

for item in all_list_items:
    print(item)

print(type(all_list_items))

print(all_list_items[0].text)

print("\ntesting\n")

test_list = all_list_items[0].text
print(type(test_list))
split_list = test_list.split()
print(test_list.split())


for x in range(len(split_list)):
    if split_list[x] == "Requires":
        str_req = int(split_list[x+2])
        if split_list[x+3] == "Dex":
            dex_req = int(split_list[x+4])
        else:
            dex_req = 0
        if split_list[x+5] == "Int":
            int_req = int(split_list[x+6])
        else:
            int_req = 0
        if split_list[x+7] == "Fai":
            fai_req = int(split_list[x+8])
        else:
            fai_req = 0

print(f"{str_req}, {dex_req}, {int_req}, {fai_req}")
GreatswordList = []
GreatswordList.append(str_req)
GreatswordList.append(dex_req)
GreatswordList.append(int_req)
GreatswordList.append(fai_req)
print(f"Greatsword List: {GreatswordList}")




def main():
    """input prompts resulting in 4 variables.
    prompt responses must be numeric and between a certain range of numbers.
    integer-converted input values will be compared to tree values"""

    print("\nWelcome to the Elden Ring Weapon Recommender!\nPlease enter your character's stats below and we will recommend a weapon ideally suited to you.\n")

    # while True:
    #     try:
    #         str_input = input("Enter your character's Strength: ")
    #         if str_input.strip().isnumeric() == True and int(str_input) >= 8 and int(str_input) <=99:
    #             break
    #         elif str_input.strip().isnumeric() == False:
    #             print("\nPlease enter a numeric value.\n")
    #         elif int(str_input) < 8:
    #             print("\nThe minimum Strength for a character is 8.\n")
    #         elif int(str_input) > 99:
    #             print("\nThe maximum Strength for a character is 99.\n")
    #         else:
    #             print("\nPlease enter a numeric value.\n")
    #     except:
    #         print("\nThere's been an error.  Please try again.\n")

    # while True:
    #     try:
    #         dex_input = input("Enter your character's Dexterity: ")
    #         if dex_input.strip().isnumeric() == True and int(dex_input) >= 9 and int(dex_input) <= 99:
    #             break
    #         elif dex_input.strip().isnumeric() == False:
    #             print("\nPlease enter a numeric value.\n")
    #         elif int(dex_input) < 9:
    #             print("\nThe minimum Dexterity for a character is 9.\n")
    #         elif int(dex_input) > 99:
    #             print("\nThe maximum Dexterity for a character is 99.\n")
    #         else:
    #             print("\nPlease enter a numeric value.\n")
    #     except:
    #         print("\nThere's been an error.  Please try again.\n")

    # while True:
    #     try:
    #         int_input = input("Enter your character's Intelligence: ")
    #         if int_input.strip().isnumeric() == True and int(int_input) >= 7 and int(int_input) <= 99:
    #             break
    #         elif int_input.strip().isnumeric() == False:
    #             print("\nPlease enter a numeric value.\n")
    #         elif int(int_input) < 7:
    #             print("\nThe minimum Intelligence for a character is 7.\n")
    #         elif int(int_input) > 99:
    #             print("\nThe maximum Intelligence for a character is 99.\n")
    #         else:
    #             print("\nPlease enter a numeric value.\n")
    #     except:
    #         print("\nThere's been an error.  Please try again.\n")

    # while True:
    #     try:
    #         fai_input = input("Enter your character's Faith: ")
    #         if fai_input.strip().isnumeric() == True and int(fai_input) >= 7 and int(fai_input) <= 99:
    #             break
    #         elif fai_input.strip().isnumeric() == False:
    #             print("\nPlease enter a numeric value.\n")
    #         elif int(fai_input) < 7:
    #             print("\nThe minimum Faith for a character is 7.\n")
    #         elif int(fai_input) > 99:
    #             print("\nThe maximum Faith for a character is 99.\n")
    #         else:
    #             print("\nPlease enter a numeric value.\n")
    #     except:
    #         print("\nThere's been an error.  Please try again.\n")


    # # print(type(str_input))
    # print("\nCharacter Stats (Test Code)")
    # print(f"Str: {str_input}")
    # print(f"Dex: {dex_input}")
    # print(f"Int: {int_input}")
    # print(f"Fai: {fai_input}")


if __name__ == '__main__':
    main()