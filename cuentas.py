class Cuenta:
    def __init__(self,nombre_cuenta,saldo_cuenta):
        self.nombre=nombre_cuenta
        self.saldo=saldo_cuenta

    def Depositar(self,valor_ingreso):
        """ 
        Ingresa el valor a depositar en la cuenta

        if valor_ingreso > 0:
            self.saldo=self.saldo+valor_ingreso
            print("Deposito realizado")
        else:
            print("Valor invalido")

        """

    def retirar(self,valor_retiro):
        """ 
        Retira el dinero disponible de la cuenta
        
        if valor_retiro <= self.saldo and valor_retiro > 0:
            self.saldo=self.saldo-valor_retiro
            print("Retiro realizado")
        else:
            print("No es posible realizar el retiro")

        """


def transferir(origen,destino,valor):
    if valor > 0 and valor <= origen.saldo:
        origen.saldo=origen.saldo-valor
        destino.saldo=destino.saldo+valor
        print("Transferencia realizada")
    else:
        print("No es posible realizar la transferencia")


def mostrar_cuenta(cuenta):
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
