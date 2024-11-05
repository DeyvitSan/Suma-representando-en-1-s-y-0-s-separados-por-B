class TuringMachine:
    def __init__(self, numbers):
        self.tape = self.create_tape(numbers)  # La cinta 
        self.head = 0                          # Posición inicial 
        self.state = 'q0'                      # Estado inicial de la máquina
        self.blank_symbol = 'B'                # Símbolo en blanco o el separador

    def create_tape(self, numbers):
        
        tape = ['B']
        for num in numbers:
            tape.extend(['1'] * num)  
            tape.append('0')
        tape[-1] = 'B'  
        return tape

    def step(self):
    
        symbol = self.tape[self.head]  

        if self.state == 'q0':
            if symbol == '1':
                self.head += 1 
            elif symbol == '0':
                self.tape[self.head] = 'B' 
                self.state = 'q1'  
                self.head -= 1  
            elif symbol == 'B':
                self.state = 'q2'  

        elif self.state == 'q1':
            if symbol == '1':
                self.head -= 1  
            elif symbol == 'B':
                self.tape[self.head] = '1'  
                self.state = 'q0'  
                self.head += 1  

        elif self.state == 'q2':
            
            if symbol in ['1', '0']:
                self.tape[self.head] = 'B'  
                self.head += 1
            elif symbol == 'B':
                self.state = 'halt'  

    def run(self):
        while self.state != 'halt':
            self.step()
        return ''.join(self.tape)



def input_numbers():
    print("Ingrese los numeros que desea sumar, separados por espacios:")
    user_input = input()
    numbers = [int(num) for num in user_input.split()]
    return numbers



numbers_to_sum = input_numbers()  
machine = TuringMachine(numbers_to_sum)
output_tape = machine.run()


sum_result = output_tape.count('1')
print(f"Resultado de la suma normal: {sum_result}")
print(f"Cinta final donde los unos representan el numero ingresado: {output_tape}")  
