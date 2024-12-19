def validarPassword(_rutaArchivo, _password):
    #ABRIENDO ARCHIVO
    archivoPasswords = open(_rutaArchivo, "r");
    
    #LISTA DE PASSWORDS
    listaPasswords = archivoPasswords.read().split("\n");
    
    #VALIDANDO
    for passwordRecorrido in listaPasswords:
        if _password == passwordRecorrido:
            print(f"\n\tSE ENCONTRO LA CONTRASENA: {passwordRecorrido}\n");
            break;
        
    #CERRANDO ARCHIVO
    archivoPasswords.close()


#MAIN
usuario = "fercho";
password = "charlie";

validarPassword("./passwords.txt", password);