class MediosDeAcceso:
    def __init__(self, estatus, tipo, clave, fechaCreacion, fechaExpiracion):
        self.estatus = estatus
        self.tipo = tipo
        self.clave= clave
        self.fechaCreacion = fechaCreacion
        self.fechaExpiracion = fechaExpiracion

    def Activar(self):
        print('El medio de acceso {} está activo'.format(self.clave))


class Tarjeta(MediosDeAcceso):
    def esDebito(self):
        if(self.tipo == 'TAR'):
            print('El medio de acceso {} es débito'.format(self.clave))
            

tarjeta1 = Tarjeta(estatus=1, tipo= 'TAR', clave= '1234567898761324', fechaCreacion= '2023-01-01', fechaExpiracion= '2026-02-01')

tarjeta1.Activar()
tarjeta1.esDebito()
