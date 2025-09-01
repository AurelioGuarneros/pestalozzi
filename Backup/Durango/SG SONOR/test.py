



dias_dentro = 0
tipo_tarifa_sistema = False
promo = "SG SONOR"
name_promo = "Promo_"+promo

file =  open(f'Test_{name_promo.replace(" ", "_")}.py', "w", encoding="UTF-8")
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

            if i == 0:
                cuarto_hora = 0
            elif i < 16 and i >= 1:
                cuarto_hora = 1
            elif i < 31 and i >= 16:
                cuarto_hora = 2
            elif i < 46 and i >= 31:
                cuarto_hora = 3
            else:
                cuarto_hora = 4


            if hour <= 3:
                importe = 60

                if hour == 3 and cuarto_hora >= 1:
                    importe = 90


            elif hour <= 9:
                importe = 90

                if hour == 9 and cuarto_hora >= 1:
                    if cuarto_hora < 3: 
                        importe = importe + (cuarto_hora * 8)

                    elif cuarto_hora  == 3: 
                        importe = importe + 23

                    elif cuarto_hora == 4: 
                        importe = importe + 30

            else:
                importe = 180

                if cuarto_hora < 3: 
                    importe = -importe + (cuarto_hora * 8) + (hour * 30)

                elif cuarto_hora  == 3: 
                    importe = -importe + 23 + (hour * 30)

                elif cuarto_hora == 4: 
                    importe = -importe + 30 + (hour * 30)
                

            code = f"""
    def test_get_importe_tarifa_{name_promo.replace(" ", "_")}_case_{hour}_{i}(self):
        resultado, _ = self.cobro_controller.get_importe_promo(
            promo_id='{promo}',
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


with open(f'tarifa_{name_promo}.json', "w", encoding="UTF-8") as file:
    code = "{\n"
    file.write(code)
    for i in range(25):
        code = f'\t"{i}": '+"{\n"
        file.write(code)
        
        for ii in range(4):
            ii_text = ii
            if ii == 0:
                ii_text = "hora"

            # if minutos_dentro == 0:
            #     cuarto_hora = 0
            # elif minutos_dentro <= 16 and minutos_dentro >= 1:
            #     cuarto_hora = 1
            # elif minutos_dentro <= 31 and minutos_dentro > 16:
            #     cuarto_hora = 2
            # elif minutos_dentro <= 46 and minutos_dentro > 31:
            #     cuarto_hora = 3
            # else:
            #     cuarto_hora = 4

            if i <= 3:
                importe = 60

                if i == 3 and ii >= 1:
                    importe = 90


            elif i <= 9:
                importe = 90

                if i == 9 and ii >= 1:
                    if ii < 3: 
                        importe = importe + (ii * 8)

                    elif ii  == 3: 
                        importe = importe + 23

                    elif ii == 4: 
                        importe = importe + 30

            else:
                importe = 180

                if ii < 3: 
                    importe = -importe + (ii * 8) + (i * 30)

                elif ii  == 3: 
                    importe = -importe + 23 + (i * 30)

                elif ii == 4: 
                    importe = -importe + 30 + (i * 30)


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

minutos_dentro = 46
horas_dentro = 1
dias_dentro = 0
