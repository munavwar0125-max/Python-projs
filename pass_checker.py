print("Enter password:" )
password=input()
print("The password is:",password)
has_length=False    
has_length = len(password) >= 8    
     
def uppercase():
     iscaps=False
     for i in password:
         if 65 <= ord(i) <= 90:
          iscaps=True
          return iscaps
         
      
def lowercase():
      issmall=False
      for i in password:
         if 97 <= ord(i) <= 122:
          issmall=True
          return issmall
         
 
def digts():
     isdigit=False
     for i in password:
         if 48 <= ord(i) <= 57:
          isdigit=True
          return isdigit
         
 
def specialchars():
     isspechar=False
     for i in password:
        if (33 <= ord(i) <= 47)or( 58 <= ord(i) <= 64)or(91<= ord(i) <= 96)or(123 <= ord(i) <= 126):
          isspechar=True
          return isspechar
          
iscaps=uppercase();
issmall=lowercase();
isdigit=digts();
isspechar=specialchars();
              
 
check=[has_length,iscaps,issmall,isdigit,isspechar]
score=check.count(True)
     
if score <= 2:
    print("Weak")
elif score <= 4:
    print("Medium")
else:
    print("Strong")