import sys

if len(sys.argv) >= 3:
  script_name = sys.argv[0]
  salary = sys.argv[1]
else:
  script_name = sys.argv[0]
  salary = 15000

bamount=salary*0.10
bonus=salary+bamount
print("Bonus amount:",bamount)
print("total Amount:",bonus)
