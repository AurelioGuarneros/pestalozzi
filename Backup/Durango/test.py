

# dias_dentro = 0
# tipo_tarifa_sistema = False

# file =  open(f'Test_DG.py', "w", encoding="UTF-8")
# code = """import unittest
# from Controllers.CobroController import CobroController

# class TestCobroController(unittest.TestCase):
#     def __init__(self, methodName: str = "runTest") -> None:
#         super().__init__(methodName)
#         self.cobro_controller = CobroController()\n\n"""
# file.write(code)

# for hour in range(24):

#     # with open('example.txt', "w", encoding="UTF-8") as file:
#         for i in range(0, 60):

#             importe = 0
#             if hour == 0:
#                 importe = 30
#             else:

#                 # Calcula la tarifa y el importe a pagar
#                 if i == 0:
#                     cuarto_hora = 0
#                 elif i < 16 and i >= 1:
#                     cuarto_hora = 1
#                 elif i < 31 and i >= 16:
#                     cuarto_hora = 2
#                 elif i < 46 and i >= 31:
#                     cuarto_hora = 3
#                 elif i <= 59 and i >= 46:
#                     cuarto_hora = 4

#                 if cuarto_hora < 3: 
#                     importe = (hour * 30) + (cuarto_hora * 8)

#                 elif cuarto_hora  == 3: 
#                     importe = (hour * 30) + 23
    
#                 elif cuarto_hora == 4: 
#                     importe = int((hour * 30) + (cuarto_hora *7.5))

#             code = f"""
#     def test_get_importe_tarifa_case_{hour}_{i}(self):
#         resultado = self.cobro_controller.get_importe_tarifa(
#             tipo_tarifa_sistema = {tipo_tarifa_sistema},
#             inicio_cobro_fraccion=2,
#             minutos_dentro={i},
#             horas_dentro={hour}, 
#             dias_dentro={dias_dentro})
#         self.assertEqual(resultado, {importe})\n\n"""

#             file.write(code)

# code =  """
# def run_code():
#     unittest.main()\n\n"""
# file.write(code)

# code =  """
# if __name__ == '__main__':
#     run_code()\n\n"""
# file.write(code)


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
                importe = 30

            else:

                if ii < 3: 
                    importe = (i * 30) + (ii * 8)

                elif ii  == 3: 
                    importe = (i * 30) + 23
    
                elif ii == 4: 
                    importe = (i * 30) + (ii *7.5)


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




