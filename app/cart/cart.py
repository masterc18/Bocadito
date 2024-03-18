#se creo el diccionario
cart = {}
#funcion para agregar productos
def addProdut():
    nameP = input("Nombre: ")
    priceP = float(input("Precio: "))
    #se usa el nombre el nombre del producto como llave
    cart[nameP] = priceP

#funcion para ekiminar los productos
def deleteProduct():
    nameP = input("Ingrese el nombre")
    if nameP in cart:
        del cart[nameP]
    else:
        print(f"{nameP} no esta en el carrito")
        
