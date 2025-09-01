



dias_dentro = 0
tipo_tarifa_sistema = False
promo = "ST STARB"
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
                importe = 24 
            else:
                importe = (hour * 24) + (cuarto_hora * 6)

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

