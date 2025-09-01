


dias_dentro = 0
tipo_tarifa_sistema = False

file =  open(f'Test_AM.py', "w", encoding="UTF-8")
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

            importe = 0
            if hour == 0:
                importe = 28
            else:

                # Calcula la tarifa y el importe a pagar
                if i == 0:
                    cuarto_hora = 0
                elif i < 16 and i >= 1:
                    cuarto_hora = 1
                elif i < 31 and i >= 16:
                    cuarto_hora = 2
                elif i < 46 and i >= 31:
                    cuarto_hora = 3
                elif i <= 59 and i >= 46:
                    cuarto_hora = 4

                # Calcula el importe a pagar según la tabla de precios
                if hour <= 3:

                    if hour == 3:
                        importe = 80
                    elif hour == 2 and cuarto_hora == 4:
                        importe = 80
                    else:
                        importe = (hour * 28) + (cuarto_hora * 7)
                        


                else:
                    if 3 <= hour < 12:
                        importe = 80

                    elif 12 <= hour <= 14:
                        if hour == 14  and cuarto_hora == 4:
                            importe = 160
                        else:
                            importe = (hour * 28) + (cuarto_hora * 7) - 256
                

                    else:
                        importe = 160

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
                importe = 28
            else:

                # Calcula el importe a pagar según la tabla de precios
                if i <= 3:

                    importe = (i * 28) + (ii * 7)
                    if i == 2 and ii == 4:
                        importe = 77

                    if i == 3 and ii >= 0:
                        importe = 80

                else:
                    if 3 <= i < 12:
                        importe = 80

                    elif 12 <= i <= 14:
                        importe = (i * 28) + (ii * 7) - 256
                        if i == 14  and ii == 4:
                            importe = 160
                        else:
                            importe = (i * 28) + (ii * 7) - 256

                    else:
                        importe = 160


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





importe = 0
horas_dentro = 2
minutos_dentro = 59

if horas_dentro == 0:
    importe = 28
else:

    # Calcula la tarifa y el importe a pagar
    if minutos_dentro == 0:
        cuarto_hora = 0
    elif minutos_dentro < 16 and minutos_dentro >= 1:
        cuarto_hora = 1
    elif minutos_dentro < 31 and minutos_dentro >= 16:
        cuarto_hora = 2
    elif minutos_dentro < 46 and minutos_dentro >= 31:
        cuarto_hora = 3
    elif minutos_dentro <= 59 and minutos_dentro >= 46:
        cuarto_hora = 4

    # Calcula el importe a pagar según la tabla de precios
    if horas_dentro <= 3:

        importe = (horas_dentro * 28) + (cuarto_hora * 7)
        if horas_dentro == 2 and cuarto_hora == 4:
            importe = 77

        if horas_dentro == 3:
            importe = 80

    else:
        if 3 <= horas_dentro < 12:
            importe = 80

        elif 12 <= horas_dentro <= 14:
            if horas_dentro == 14  and cuarto_hora == 4:
                importe = 160
            else:
                importe = (horas_dentro * 28) + (cuarto_hora * 7) - 256
                

        else:
            importe = 160


