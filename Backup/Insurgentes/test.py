


dias_dentro = 0
tipo_tarifa_sistema = False

file =  open(f'Test_IS.py', "w", encoding="UTF-8")
code = """import unittest
from Controllers.CobroController import CobroController

class TestCobroController(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.cobro_controller = CobroController()\n\n"""
file.write(code)

for hour in range(24):

    # with open('example.txt', "w", encoding="UTF-8") as file:
        for i in range(0, 60):

            if hour == 0:
                # Si la permanencia es menor a 1 hora, se aplica una tarifa fija de 28 unidades
                importe = 28
            else:
                if i == 0:
                    minutos = 0
                elif i < 16 and i >= 1:
                    minutos = 1
                elif i < 31 and i >= 16:
                    minutos = 2
                elif i < 46 and i >= 31:
                    minutos = 3
                elif i <= 59 and i >= 46:
                    minutos = 4

                # Calcula el importe a pagar según la tabla de precios
                if hour < 3:
                    importe = (hour * 28) + (minutos * 7)

                elif hour >= 3 and hour <= 12:
                    if hour == 3 and minutos == 0:
                        importe = 84

                    elif hour == 12 and minutos >= 1:
                        importe = 250
                        
                    else:
                        importe = 90

                else:
                    importe = 250

            code = f"""
    def test_get_importe_tarifa_case_{hour}_{i}(self):
        resultado = self.cobro_controller.get_importe_tarifa(
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


with open(f'tarifa.json', "w", encoding="UTF-8") as file:
    code = "{\n"
    file.write(code)
    for i in range(25):
        code = f'\t"{i}": '+"{\n"
        file.write(code)
        
        for ii in range(4):
            ii_text = ii
            if ii == 0:
                ii_text = "hora"


            importe = 0

            if i == 0:
                # Si la permanencia es menor a 1 hora, se aplica una tarifa fija de 28 unidades
                importe = 28

            # Calcula el importe a pagar según la tabla de precios
            elif i < 3:
                importe = (i * 28) + (ii * 7)

            elif i >= 3 and i <= 12:
                importe = 90

                if i == 3 and ii == 0:
                    importe = 84

                elif i == 12 and ii >= 1:
                    importe = 250

            else:
                importe = 250


            code = f'\t\t"{ii_text}": {importe}'
            if ii ==3:
                code += '\n'
            else:
                code += ',\n'
            
            file.write(code)
            if ii_text == "hora":
                ii_text = 0

        if i ==24:
            code = "\t}\n"
        else:
            code = "\t},\n"
        
        file.write(code)

    code = "}\n"
    file.write(code)




