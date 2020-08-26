invited_guest = ['Ken', 'Alice', 'Edith', 'Evans']
print(f"Hi {invited_guest[0]}, I woould like to invite you for dinner on 22nd August, 2020. Please confirm your \nattendance before the said date.")
print(f"Hi {invited_guest[1]}, I woould like to invite you for dinner on 22nd August, 2020. Please confirm your \nattendance before the said date.")
print(f"Hi {invited_guest[2]}, I woould like to invite you for dinner on 22nd August, 2020. Please confirm your \nattendance before the said date.")
print(f"Hi {invited_guest[3]}, I woould like to invite you for dinner on 22nd August, 2020. Please confirm your \nattendance before the said date.")
print(f"{invited_guest[2]} cannot make it for dinner")
invited_guest[2] = 'Caroline'

print(f"Hi {invited_guest[0]}, I woould like to invite you for dinner on 22nd August, 2020. Please confirm your \nattendance before the said date.")
print(f"Hi {invited_guest[1]}, I woould like to invite you for dinner on 22nd August, 2020. Please confirm your \nattendance before the said date.")
print(f"Hi {invited_guest[2]}, I woould like to invite you for dinner on 22nd August, 2020. Please confirm your \nattendance before the said date.")
print(f"Hi {invited_guest[3]}, I woould like to invite you for dinner on 22nd August, 2020. Please confirm your \nattendance before the said date.")

print("I just found a bigger dinner table and would therefore like to invite more people")

invited_guest.insert(0, 'Kabu')
invited_guest.insert(2, 'Grace')
invited_guest.append('Faith')
print(f"The total number of invited guests is: {len(invited_guest)}")

print(f"Hi {invited_guest[0]}, I woould like to invite you for dinner on 22nd August, 2020. Please confirm your \nattendance before the said date.")
print(f"Hi {invited_guest[1]}, I woould like to invite you for dinner on 22nd August, 2020. Please confirm your \nattendance before the said date.")
print(f"Hi {invited_guest[2]}, I woould like to invite you for dinner on 22nd August, 2020. Please confirm your \nattendance before the said date.")
print(f"Hi {invited_guest[3]}, I woould like to invite you for dinner on 22nd August, 2020. Please confirm your \nattendance before the said date.")
print(f"Hi {invited_guest[4]}, I woould like to invite you for dinner on 22nd August, 2020. Please confirm your \nattendance before the said date.")
print(f"Hi {invited_guest[5]}, I woould like to invite you for dinner on 22nd August, 2020. Please confirm your \nattendance before the said date.")
print(f"Hi {invited_guest[6]}, I woould like to invite you for dinner on 22nd August, 2020. Please confirm your \nattendance before the said date.")

print("I am sorry to inform you that I can only invite two guests for the dinner")

removed_guest1 = invited_guest.pop()
print(f"I am sorry {removed_guest1} unfortunately I cannot invite you for dinner at this time")
removed_guest2 = invited_guest.pop()
print(f"I am sorry {removed_guest2} unfortunately I cannot invite you for dinner at this time")
removed_guest3 = invited_guest.pop()
print(f"I am sorry {removed_guest3} unfortunately I cannot invite you for dinner at this time")
removed_guest4 = invited_guest.pop()
print(f"I am sorry {removed_guest4} unfortunately I cannot invite you for dinner at this time")
removed_guest5 = invited_guest.pop()
print(f"I am sorry {removed_guest5} unfortunately I cannot invite you for dinner at this time")

print(invited_guest)

print(f"Hi {invited_guest[0]}, I woould like to invite you for dinner on 22nd August, 2020. Please confirm your \nattendance before the said date.")
print(f"Hi {invited_guest[1]}, I woould like to invite you for dinner on 22nd August, 2020. Please confirm your \nattendance before the said date.")

del invited_guest[0]
print(invited_guest)
del invited_guest[0]
print(invited_guest)