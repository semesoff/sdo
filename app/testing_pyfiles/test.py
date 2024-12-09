import contextlib
import io
import threading
import time
import asyncio


class TeacherList:
    variables = dict()
    input_variables = []
    formulas_teacher = dict()
    formulas_student = dict()
    check = []
    operations_in_math = ['+', '-', '/', '*', '=']

    def __int__(self, variables, formulas):
        self.variables = variables
        self.formulas = formulas

    def binding_variables(self, a, b):  # a - student variable, b - teacher variable
        buff = dict()
        for i in range(0, len(self.variables)):
            if b == list(self.variables.items())[i][1]:
                buff[a] = b
            else:
                buff[list(self.variables.items())[i][0]] = list(self.variables.items())[i][1]
        self.variables = buff

    def binding_formulas(self, a, b):  # a - student formula, b - teacher formula
        for i in range(0, len(self.formulas_teacher)):
            if b == list(self.formulas_teacher.items())[i][1]:
                self.formulas_student[i] = a

    def add_variable(self, a):
        flag = False
        for i in range(0, len(self.variables)):
            if a == self.variables[i]:
                flag = True
        if not flag:
            self.variables[len(self.variables)] = a

    def add_teacher_formula(self, a):
        buff = []
        for char1 in a:
            for char2 in self.operations_in_math:
                if char1 == char2:
                    [...]
        buff.append(a)
        self.add_variable(a)
        self.formulas_teacher[len(self.formulas_teacher)] = buff
        self.check.append(False)

    def add_student_formula(self, a):
        formula = []
        for char1 in a:
            for char2 in self.operations_in_math:
                if char1 == char2:
                    [...]
        formula.append(a)
        for ind2 in range(0, len(self.formulas_teacher)):
            check = True
            if len(formula) != len(self.formulas_teacher[ind2]):
                check = False
            for ind1 in range(2, len(formula), 2):
                if ind1 % 2 == 0:
                    [...]
                else:
                    [...]
            if check:
                self.binding_variables(formula[0], self.formulas_teacher[ind2][0])
                self.binding_formulas(formula, self.formulas_teacher[ind2])


async def check_formulas(teacher_formula_str, input_variables_str, code_str):
    teacher_list = TeacherList()
    for line in teacher_formula_str.splitlines():
        line = line.rstrip()
        teacher_list.add_teacher_formula(line)
    buff = dict()
    for i in range(1, len(teacher_list.variables) - 1):
        if teacher_list.variables[i] == 'a1':
            buff['a'] = teacher_list.variables[i]
        else:
            buff[i] = teacher_list.variables[i]

    for line in input_variables_str.splitlines():
        line = line.rstrip()
        teacher_list.input_variables.append(line)

    input_count = 0
    for line in code_str.splitlines():
        line = line.rstrip()
        if line.find('input()') > -1:
            char = line[:line.find('=')]
            teacher_list.binding_variables(char, teacher_list.input_variables[input_count])
            input_count = input_count + 1
        else:
            teacher_list.add_student_formula(line)

    res = ""
    for i in range(len(teacher_list.formulas_teacher)):
        if teacher_list.formulas_student.get(i, False):
            res += "".join(teacher_list.formulas_student[i]) + '\n'
    return res


async def execute_code(code_str: str) -> tuple[str, float, int]:
    output = io.StringIO()
    start_time = time.time()

    def exec_code():
        try:
            with contextlib.redirect_stdout(output):
                exec(code_str)
        except Exception as e:
            output.write(f"Error executing code: {e}")

    thread = threading.Thread(target=exec_code)
    thread.start()
    thread.join(timeout=5)

    if thread.is_alive():
        output.write("Execution timed out.")
        thread.join()

    end_time = time.time()
    execution_time = round(end_time - start_time, 3)
    code_length = sum(1 for line in code_str.split('\n') if line.strip())
    result = output.getvalue()

    return result, execution_time, code_length


# main testing function
async def check_file(teacher_formula_str, input_variables_str, code_str) -> tuple[str, str, float, int]:
    formulas_output = await check_formulas(teacher_formula_str, input_variables_str, code_str)
    code_output, execution_time, code_length = await execute_code(code_str)
    return formulas_output, code_output, execution_time, code_length