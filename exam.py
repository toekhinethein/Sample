x = int(input("Please Enter Exam Result: "))
if x < 50 and x > 0:
		print ( "F" )
elif x > 49 and x < 60:
		print ( "D" )
elif x > 59 and x < 80:
		print ( "C" )
elif x > 79 and x < 90:
		print ( "B" )
elif x > 89 and x < 101:
		print ( "A" )
else:
	print ("Check Again")