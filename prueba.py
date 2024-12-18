#LIBRERIAS
import os;

#Limpiar Consola
def limpiarConsola():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux/Mac
        os.system("clear")

#DESCRIFRAR CREDENCIALES
def descifrarCredenciales(_archivoUsuarios, _archivoPasswords, _baseDatosUsuarios):
    #ABRIENDO LOS ARCHIVOS EN LECTURA
    archivoUsuarios = open(_archivoUsuarios, "r")
    archivoPasswords = open(_archivoPasswords, "r");
    
    #GENERANDO UNA LISTA CON TODAS LAS PASSWORDS EN EL ARCHIVO
    listaUsuarios = archivoUsuarios.read().split("\n");
    listaPasswords = archivoPasswords.read().split("\n");
    
    #RECORRIENDO Y VALIDANDO USUARIOS
    for usuario in listaUsuarios:
        if usuario in listaUsuarios:
            for password in listaPasswords:
                if password == _baseDatosUsuarios[usuario]:
                    print(f"\n\tCREDENCIALES ENCONTRADAS.\n\t\tUsuario: {usuario}\n\t\tPassword: {password}");
                    break;
                else:
                    pass;
        else:
            pass;

    #CERRANDO EL ARCHIVO
    archivoUsuarios.close();
    archivoPasswords.close();

#Estilo
def completarEstilo():
    print("{:-^50}".format(""));

#PAUSANDO PROGRAMA
def pausarPrograma():
    input("\nPRESIONE ENTER PARA CONTINUAR...");

#VALIDAR INICIO DE SESION
def validarInicioSesion(_usuario, _password, _baseDatosUsuarios):
    #verificando que el usuario exista dentro de la base de datos
    if _usuario in _baseDatosUsuarios.keys():
        if _password == _baseDatosUsuarios[_usuario]:
            print("\n\t\tINICIO DE SESION CORRECTO.");
        else:
            print("\n\t\tERROR: PASSWORD INCORRECTA.");
    else:
        print("\n\t\tERROR: EL USUARIO NO EXISTE EN LA BASE DE DATOS.");


#MAIN
#SIMULANDO UNA BASE DE DATOS DE USUARIOS
baseDatosUsuarios = {
    'james': 'football',
    'michael': '12345',
    'sophie': 'qwerty',
    'tom': '1q2w3e4r',
    'kate': 'login',
    'test': 'welcome1',
    'emma': '1q2w3e4r',
    'daniel': 'soccer',
    'sarah': 'test',
    'paul': 'dragon',
    'guest': 'iloveyou',
    'root': 'abc123',
    'hannah': 'freedom',
    'alex': 'abc123',
    'zoe': 'letmein',
    'helen': 'password123',
    'anna': '123123',
    'tyler': 'login',
    'user': 'batman',
    'kim': 'prueba3',
    'karen': 'iloveyou123',
    'admin': 'trustno1',
    'amy': 'freedom',
    'john': 'qazwsx',
    'brandon': 'hello',
    'fer': 'prueba1',
    'andrew': 'charlie',
    'david': 'qwerty123',
    'chris': '12345',
    'jane': 'iloveyou123',
    'kevin': '123qwe',
    'victoria': 'batman'
}

#MENU PRINCIPAL
inicioPrograma = True;

while inicioPrograma == True:
    limpiarConsola();
    completarEstilo();
    print(f"\n\t1. Inicio de sesion con credenciales. \n\t2. Descifrar credenciales. \n\t3. Salir del programa. \n");
    completarEstilo();
    opcionMenu = int(input("\nIngresa la opcion que quieras: "));
    
    #ENTRANDO A LA OPCION 1
    if opcionMenu == 1:
        limpiarConsola();
        completarEstilo();
        print(f"\n\tINICIO SESION\n");
        completarEstilo();
        pausarPrograma();

        #PIDIENDO CREDENCIALES
        usuario = input("\n\tIngresa el nombre de usuario: ");
        password = input("\n\tIngresa el password: ");

        #VALIDANDO INICIO DE SESION
        validarInicioSesion(usuario, password, baseDatosUsuarios);
        pausarPrograma();
        
        #BIENVENIDA AL PROGRAMA
        limpiarConsola();
        print(f"\nBienvenido {usuario.upper()}, estas dentro del sistema.");
        print(f"\nTus credenciales de acceso son las siguientes: \n\tUsuario: {usuario}\n\tPassword: {password}");
        pausarPrograma();
        
    #ENTRANDO A LA OPCION 2
    elif opcionMenu == 2:
        limpiarConsola();
        completarEstilo();
        print(f"\n\tDESCUBRIR CREDENCIALES\n");
        completarEstilo();
        pausarPrograma();
        
        #ENCONTRANDO CREDENCIALES DENTRO DE LA BASE DE DATOS
        descifrarCredenciales("usuarios.txt", "passwords.txt", baseDatosUsuarios);
        
    elif opcionMenu == 3:
        completarEstilo();
        opcionSalir = False;
        while opcionSalir == False:
            desicionSalir = input(f"\n\tEstas seguro de que quieres salir del programa (si/no): ");
            desicionSalir.lower();
            
            if desicionSalir == "si":
                print(f"\n\t\tCerrando el programa...\n");
                inicioPrograma = False;
                break;
            elif desicionSalir == "no":
                break;
            else:
                print(f"\n\tERROR: OPCION INCORRECTA");