import re
# ----------------------------------------
# ex= re.compile("\d\d\d\d")

# cadena_1= ex.search("probando 1234 si")
# # cadena_2= ex.search("probando 1324 si")
# # cadena_3= ex.search("probando 4234 si")

# # print(cadena_1,cadena_2,cadena_3)
# if cadena_1 is None:
#     print("Existe coincidencia",cadena_1)
# else:
# #     print("No hay coincidencia")
# -----------------------------------------
# re.sub(r"\d", "|","123elpepe123",2)
# -----------------------------------------

import re
texto = "aquellos que no conocen la historia estan condenados a repetirla - Edmund Burke"
resultado = re.split(" ",texto)
print(resultado)