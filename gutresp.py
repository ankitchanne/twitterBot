from guttenberg import gutten
product = 'the picture of dorian gray'
res = gutten(product)
print res.split('//')[1]
