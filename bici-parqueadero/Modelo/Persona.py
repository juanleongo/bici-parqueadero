class Persona:
    def __init__(self, nombre, apellido, fecha_nacimiento,tipo_documento,numero_documento):
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_nacimiento = fecha_nacimiento
        self._tipo_documento = tipo_documento
        self._numero_documento = numero_documento

        # metodos GET
    @property
    def nombre(self):
        return self._nombre

    # metodo SET
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def tipo_documento(self):
        return self._tipo_documento

    @tipo_documento.setter
    def tipo_documento(self, tipo_documento):
        self._tipo_documento = tipo_documento

    @property
    def numero_documento(self):
        return self._numero_documento

    @numero_documento.setter
    def numero_documento(self, numero_documento):
        self._numero_documento = numero_documento

    def __str__(self):
        return f'persona:{self._nombre} {self._apellido} {self._fecha_nacimiento}{self._tipo_documento}{self._numero_documento}'

