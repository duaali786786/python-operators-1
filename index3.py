print("Please write the obtained marks of the following subjects")
english=int(input( "obtained marks english"))
maths=int(input( "obtained marks maths"))
urdu=int(input( "obtained marks urdu"))
science=int(input( "obtained marks science"))

sum= english+urdu+maths+science
print( "the sum is", sum)

perc=(sum/400)*100
print("the percentage is",perc)
