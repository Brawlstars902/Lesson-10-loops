x=input('Please enter your own string (series of letters).\n')
s=('')
for i in x:
    s = i+s
print('Your original string was',x,'.')
print('Your reversed string was',s,'.')