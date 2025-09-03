x=int(input('Please select the number of your preffered footwear.\n1.Sneakers \n2.Chappals\n'))
if x ==1:
    y=int(input('What sneakers brand do you preffer; \n1.Nike \n2.Adidas\n'))
    if y==1:
        print('Nike has good sneakers.')
    if y==2:
        print('I agree that Adidas has better sneakers.')
if x==2:
    z=int(input('What chappals brand do you preffer; \n1.Bata \n2.Woodlands\n'))
    if z==1:
        print('I agree with you that Bata are better in chappals.')
    if z==2:
        print('Woodlands has good chappals.')
else:
    print('Invalid Input. Try checking if you typed the number of your choice correctly.')