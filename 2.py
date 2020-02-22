student = "SFU"
batch = "9"
gender = "male"

if student == "SFU":
	print ("I am SFU student")
	if batch == "9":
		print ("Yes, I am from batch 9")
		if gender == "male":
			print ( "I am a man")
		else:
			print ( "I am a woman")
	else:
		print ("No, I am from other batch")
else:
	print ("I am not SFU student")