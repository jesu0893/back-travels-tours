# Proyecto Final CRUD, etapa 1

# Definimos una lista de diccionarios para guardar los productos
productos = []

# Agregar un producto (create)
def agregar_producto(codigo, descripcion, precio, imagen, proveedor):
    
    if consultar_producto(codigo):
        return False
    
    nuevo_producto = { # Construimos un diccionario de datos (pares clave-valor)
        'codigo': codigo,
        'descripcion': descripcion,
        'precio': precio,
        'imagen': imagen,
        'proveedor': proveedor
    }
    productos.append(nuevo_producto)
    return True # Producto agregado

def consultar_producto(codigo):
    for producto in productos:
        if producto['codigo'] == codigo:
            return producto
    return False 

# Modificar un producto (update)
def modificar_producto(codigo, nueva_descripcion, nuevo_precio, nueva_imagen, nuevo_proveedor):
    for producto in productos:
        if producto['codigo'] == codigo:
            producto['descripcion'] = nueva_descripcion
            producto['precio'] = nuevo_precio
            producto['imagen'] = nueva_imagen
            producto['proveedor'] = nuevo_proveedor
            return True
    return False 

# Listar los productos (read)
def listar_productos():
    print("-"*50)
    for producto in productos:
        print(f'Código.......: {producto['codigo']}')
        print(f'Descripción..: {producto['descripcion']}')
        print(f'Precio.......: {producto['precio']}')
        print(f'Imagen.......: {producto['imagen']}')
        print(f'Proveedor....: {producto['proveedor']}')
        print("-"*50)

# Eliminar un producto (Delete)
def eliminar_producto(codigo):
    for producto in productos:
        if producto['codigo'] == codigo:
            productos.remove(producto)
            return True
    return False

    
# Programa principal

# AGREGAR PRODUCTOS
agregar_producto(1, 'Viaje a Bariloche', 450000, 'bariloche.jpg', 101)
agregar_producto(2, 'Viaje a Cataratas de Iguazu', 250000, 'cataratas.jpg', 102)
agregar_producto(3, 'Viaje a Salta', 225000, 'salta.jpg', 103)
agregar_producto(4, 'Excursion a Mendoxa', 78500, 'mendoza.jpg', 104)
agregar_producto(5, 'Excursion a Alta Gracia', 50000, 'altagracia.jpg', 105)
agregar_producto(3, 'Excursio a Tigre', 25000, 'tigre.jpg', 105) # No es posible agregarlo, mismo código que el producto 3.
agregar_producto(6, 'Viaje a Barcelona', 2250000, 'barcelona.jpg', 115)
agregar_producto(7, 'Viaje a Paris', 2225000, 'paris.jpg', 203)
agregar_producto(8, 'Excursion a La Plata', 25000, 'la plata.jpg', 50)
agregar_producto(9, 'Excursion a Mar del Plata', 75000, 'mardelplata.jpg', 40)

# for producto in productos:
#     print(producto)
#     print()

# Consultar y Modificar producto
# cod = int(input("Ingrese el código a buscar: "))
# print(consultar_producto(cod))
# modificar_producto(cod, "excursion a Jujuy", 70000, "jujuy.jpg", 12)
# print(consultar_producto(cod))

# Listar los productos 
listar_productos()

# Eliminar un producto
print("Eliminando el producto....")
eliminar_producto(4)
listar_productos() 