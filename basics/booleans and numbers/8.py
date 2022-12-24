print("Enter the value: ");
x = input();
try:
   y = float(x) if "." in x else int(x)
   z = abs(y)
   if (y == z):
       print ("True");
   else:
       print ("False");
except ValueError:
   print("No.. the input value is not a number. It's a string")
