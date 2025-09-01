from Controllers.CobroController import CobroController

importe = 38
dias_dentro = 0
tipo_tarifa_sistema = True


file =  open(f'Test_PN.py', "w", encoding="UTF-8")
code = """import unittest
from Controllers.CobroController import CobroController

class TestCobroController(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.cobro_controller = CobroController()\n\n"""
file.write(code)

for hour in range(25):
        if hour == 0:
            importe = importe
        else:
            importe +=13

    # with open('example.txt', "w", encoding="UTF-8") as file:
        for i in range(0, 16):
            if i == 0:
                importe -= 13
            code = f"""
    def test_get_importe_tarifa_case_{hour}_{i}(self):
        resultado = self.cobro_controller.get_importe_tarifa(
            tipo_tarifa_sistema = {tipo_tarifa_sistema},
            inicio_cobro_fraccion=2,
            minutos_dentro={i},
            horas_dentro={hour}, 
            dias_dentro={dias_dentro})
        self.assertEqual(resultado, {importe})\n\n"""
            file.write(code)

            if i == 0:
                importe += 13

        if hour == 0:
            importe = importe 
        else:
            importe +=13

        for i in range(16, 31):
            code = f"""
    def test_get_importe_tarifa_case_{hour}_{i}(self):
        resultado = self.cobro_controller.get_importe_tarifa(
            tipo_tarifa_sistema = {tipo_tarifa_sistema},
            inicio_cobro_fraccion=2,
            minutos_dentro={i},
            horas_dentro={hour}, 
            dias_dentro={dias_dentro})
        self.assertEqual(resultado, {importe})\n\n"""
            file.write(code)

        if hour == 0:
            importe = importe 
        else:
            importe +=6

        for i in range(31, 46):
            code = f"""
    def test_get_importe_tarifa_case_{hour}_{i}(self):
        resultado = self.cobro_controller.get_importe_tarifa(
            tipo_tarifa_sistema = {tipo_tarifa_sistema},
            inicio_cobro_fraccion=2,
            minutos_dentro={i},
            horas_dentro={hour}, 
            dias_dentro={dias_dentro})
        self.assertEqual(resultado, {importe})\n\n"""

            file.write(code)

        if hour == 0:
            importe = importe 
        else:
            importe +=6

        for i in range(46, 60):
            code = f"""
    def test_get_importe_tarifa_case_{hour}_{i}(self):
        resultado = self.cobro_controller.get_importe_tarifa(
            tipo_tarifa_sistema = {tipo_tarifa_sistema},
            inicio_cobro_fraccion=2,
            minutos_dentro={i},
            horas_dentro={hour}, 
            dias_dentro={dias_dentro})
        self.assertEqual(resultado, {importe})\n\n"""

            file.write(code)

code =  """
def run_code():
    unittest.main()\n\n"""
file.write(code)

code =  """
if __name__ == '__main__':
    run_code()\n\n"""
file.write(code)



print(CobroController().get_importe_tarifa(
    tipo_tarifa_sistema = True,
    inicio_cobro_fraccion=2,
    minutos_dentro=1,
    horas_dentro=0, 
    dias_dentro=1
    ))

