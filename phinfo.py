import phonenumbers
from phonenumbers import geocoder,carrier
import time

print("ONLY CYBERNULLS MEMBERS CAN USE THIS TOOL")
time.sleep(4)

talk=input("Ok?:")
time.sleep(3)

print("Checking...")
time.sleep(4)


print("Installing phonenumbers pip...")
time.sleep(4)
print("Done!")
time.sleep(2)

print("adding virtual root for this tool...")
time.sleep(4)
print("Done!")
time.sleep(1)


print("=====CYBERNULLS TEAM=====")
time.sleep(5)
print("=====Mobile Number information=====\n")
time.sleep(2)

print("Wait loading Tool....")
time.sleep(5)

cd=input("\n\t Enter code number eg[+63]:")
n=input("\n\t Enter Your Number:")


mob_cd=phonenumbers.parse(cd+n)


n=input("\n\twait searching details....")
time.sleep(3)

print("\n\t Country Name :",geocoder.description_for_number(mob_n,"en"))

print("\n\t Sim Name :",carrier.name_for_number(mob_n,"en"))


