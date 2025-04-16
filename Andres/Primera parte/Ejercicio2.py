class CuentaBancaria:
    def __init__(self, nombre_persona, saldo_cuenta):
        self.nombre_persona = nombre_persona
        self.saldo_cuenta = saldo_cuenta
    
    def depositar(self, cantidad):
        self.saldo_cuenta = self.saldo_cuenta + cantidad
    
    def retirar(self, cantidad):
        if cantidad > self.saldo_cuenta:
            print("No hay Fondos suficientes")
        else:
            self.saldo_cuenta = self.saldo_cuenta - cantidad
    def mostar_saldo(self):
        print(f"El saldo de la cuenta es: {self.saldo_cuenta}pesos")
cuenta1 = CuentaBancaria("Andres", 5000)
cuenta1.depositar(2000) 
print(cuenta1.saldo_cuenta)
cuenta1.retirar(1000)
print(cuenta1.saldo_cuenta)




