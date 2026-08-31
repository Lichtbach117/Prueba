class Cuenta:
    """ 
    Representa una cuenta bancaria.

    Attributes:
        titular (str): nombre del titular.
        saldo (float): saldo disponible.
    """

    def __init__(self,nombre_cuenta,saldo_cuenta):
        """Inicializa una cuenta bancaria.

        Args:
            nombre_cuenta (str): _description_
            saldo_cuenta (float): _description_
        """
        self.nombre=nombre_cuenta
        self.saldo=saldo_cuenta

    def Depositar(self,valor_ingreso):
        """ Ingresa el valor a depositar en la cuenta

        Args:
            valor_ingreso (float): Dato del monto que se ingresa a la cuenta
        """

        if valor_ingreso > 0:
            self.saldo=self.saldo+valor_ingreso
            print("Deposito realizado")
        else:
            print("Valor invalido")


    def retirar(self,valor_retiro):
        """ Retira el dinero disponible de la cuent

        Args:
            valor_retiro (float): Dato del monto que se ingresa a la cuenta
        """
        
        if valor_retiro <= self.saldo and valor_retiro > 0:
            self.saldo=self.saldo-valor_retiro
            print("Retiro realizado")
        else:
            print("No es posible realizar el retiro")



def transferir(origen,destino,valor):
    """ funcion para transferir el dinero de una cuenta a otra

    Args:
        origen (Cuenta): cuenta la cual transfiere el dinero
        destino (Cuenta): cuenta que resive el dinero de la transferencia
        valor (float): monto que se transferira de una cuenta a la otra
    """

    if valor > 0 and valor <= origen.saldo:
        origen.saldo=origen.saldo-valor
        destino.saldo=destino.saldo+valor
        print("Transferencia realizada")
    else:
        print("No es posible realizar la transferencia")


def mostrar_cuenta(cuenta):
    """ Muestra los datos de la cuenta

    Args:
        cuenta (Cuenta): objeto que almacena los datos (nombre y saldo)
    """

    print("Titular:",cuenta.nombre)
    print("Saldo:",cuenta.saldo)


def main():
    cuenta1=Cuenta("Ana",1000)
    cuenta2=Cuenta("Carlos",500)

    print("=== CUENTAS INICIALES ===")
    mostrar_cuenta(cuenta1)
    mostrar_cuenta(cuenta2)

    cuenta1.Depositar(500)
    cuenta1.retirar(200)
    transferir(cuenta1,cuenta2,300)

    print("\n=== CUENTAS FINALES ===")
    mostrar_cuenta(cuenta1)
    mostrar_cuenta(cuenta2)


if __name__=="__main__":
    main()