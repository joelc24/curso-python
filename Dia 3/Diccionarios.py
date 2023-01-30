diccionario = {"c1":"valor1","c2":"valor2"}
resultado = diccionario.get("c1")

cliente = {"nombre": "Juan", "apellido": "Fuentes", "peso": 88, "talla": 1.76}
consulta = cliente.get("apellido")

dic = {"c1": 55, "c2": [10,20,30], "c3":{"s1": 100, "s2": 200}}
lista = dic["c2"][1]
dic2 = dic["c3"].get("s1")
dic3 = {"c1":["a","b","c"],"c2":["d","e","f"]}
E = dic3.get("c2")[1].upper()
dic4 = {1:"a",2:"b"}
print(dic4)
dic4[3] = "c"

print(dic4)

dic4[2] = "B"

print(dic4)