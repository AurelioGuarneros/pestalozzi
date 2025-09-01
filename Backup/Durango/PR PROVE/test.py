



dias_dentro = 0
tipo_tarifa_sistema = False
promo = "PR PROVE"
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


            if hour == 0:

                if cuarto_hora == 0:
                    importe = 0
                elif cuarto_hora == 1:
                    importe = 0
                elif cuarto_hora == 2:
                    importe = 8
                elif cuarto_hora == 3:
                    importe = 15
                elif cuarto_hora == 4:
                    importe = 22

            else:
                if cuarto_hora < 3: 
                    importe = (hour * 30) + (cuarto_hora * 8)

                elif cuarto_hora  == 3: 
                    importe = (hour * 30) + 23

                elif cuarto_hora == 4: 
                    importe = (hour * 30) + 30
                
                importe -= 8

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

            if i == 0:

                if ii == 0:
                    importe = 0
                elif ii == 1:
                    importe = 0
                elif ii == 2:
                    importe = 8
                elif ii == 3:
                    importe = 15
                else:
                    importe = 22

            else:
                if ii < 3: 
                    importe = (i * 30) + (ii * 8)

                elif ii  == 3: 
                    importe = (i * 30) + 23

                elif ii == 4: 
                    importe = (i * 30) + 30
                
                importe -= 8


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
