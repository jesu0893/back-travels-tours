# Proyecto Final CRUD, etapa 2

class Catalogo:
    productos = []
    
    # Agregar un producto (create)
    def agregar_producto(self, codigo, descripcion, precio, imagen, proveedor):
        
        if self.consultar_producto(codigo):
            return False
        
        nuevo_producto = { # Construimos un diccionario de datos (pares clave-valor)
            'codigo': codigo,
            'descripcion': descripcion,
            'precio': precio,
            'imagen': imagen,
            'proveedor': proveedor
        }
        self.productos.append(nuevo_producto)
        return True # Producto agregado

    def consultar_producto(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                return producto
        return False 
    
    # Listar los productos (read)
    def listar_productos(self):
        print("-"*50)
        for producto in self.productos:
            print(f'Código.......: {producto['codigo']}')
            print(f'Descripción..: {producto['descripcion']}')
            print(f'Precio.......: {producto['precio']}')
            print(f'Imagen.......: {producto['imagen']}')
            print(f'Proveedor....: {producto['proveedor']}')
            print("-"*50)
    
    # Modificar un producto (update)
    def modificar_producto(self, codigo, nueva_descripcion, nuevo_precio, nueva_imagen, nuevo_proveedor):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                producto['descripcion'] = nueva_descripcion
                producto['precio'] = nuevo_precio
                producto['imagen'] = nueva_imagen
                producto['proveedor'] = nuevo_proveedor
                return True
        return False 
    
    # Eliminar un producto
    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                self.productos.remove(producto)
                return True
        return False
    
    # Funcion extra
    # Mostrar un producto
    def mostrar_producto(self, codigo):
        producto = self.consultar_producto(codigo)
        if producto:
            print("-"*50)
            print(f'Código.......: {producto['codigo']}')
            print(f'Descripción..: {producto['descripcion']}')
            print(f'Precio.......: {producto['precio']}')
            print(f'Imagen.......: {producto['imagen']}')
            print(f'Proveedor....: {producto['proveedor']}')
            print("-"*50)
            
            
# Programa principal
catalogo = Catalogo() # Creamos el objeto catalogo
catalogo.agregar_producto(1, 'Viaje a Bariloche', 450000, 'bariloche.jpg', 101)
catalogo.agregar_producto(2, 'Viaje a Cataratas de Iguazu', 250000, 'cataratas.jpg', 102)
catalogo.agregar_producto(3, 'Viaje a Salta', 225000, 'salta.jpg', 103)

print("Listado de productos:")
catalogo.listar_productos()

print("Modificando un producto...")
catalogo.modificar_producto(3, 'Excursion a La Plata', 25000, 'la plata.jpg', 50)
catalogo.listar_productos()

print("Eliminando un producto...")
catalogo.eliminar_producto(1)
catalogo.listar_productos()

print("Mostrando los datos de un producto...")
catalogo.mostrar_producto(3)