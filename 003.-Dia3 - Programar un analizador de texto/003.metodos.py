texto = "Este es el texto de Federico"

#transformando en mayusculas
upper_text = texto.upper()
print(upper_text)

#transformando en minusculas
lower_text= texto.lower()
print(lower_text)

#aplicando split
split_ist=texto.split() #separa por espacios
print(split_ist)

#aplicando split con argumento
split_ist2=texto.split('t') #hace una división donde encuuentre una t
print(split_ist2)

#Join

a = 'Aprender'
b = 'Python'
c = 'Es'
d = 'Genial'
e = ' '.join([a,b,c,d]) #toma todos los elementos en une lista une con un espacio

print(e)

#metodo find
#"es exactamente igual al metodo index"
find_text = texto.find('t') #si no encuentra el caracter devuelve -1
print(find_text)

#replace
#reemplaza una parte especifica de un texto por otra seleccionada
replace_text = texto.replace("Federico", "Javier")
print(replace_text)