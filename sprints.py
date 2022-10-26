def meanCalculator (*args):
   intlist = []
   floatList = []
   typeNull = 0
   meanVal = 0
   evenNum = 0
   maxNum = 0
   sumVal = 0
   for i in args:
	   if (type(i)== type(1)):
		   intlist.append(i)

	   elif (type(i)==type(1.5)):
		   floatList.append(i)

	   else:
		   typeNull = typeNull +1

   if (typeNull == len(args)):
       output_2 = "No Integers or Floats Exist"
       return output_2

   for j in intlist:
		  if j%2 == 0:
			  sumVal = sumVal + j
			  evenNum = evenNum +1
   for z in floatList:
		   if z >= maxNum:
			   maxNum = z
   meanVal = sumVal/evenNum
   output = "The mean value = " + str(meanVal) + '\n'+\
            "The max number of float point numbers = " + str(maxNum) + '\n'

   return output