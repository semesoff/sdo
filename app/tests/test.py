from app.db.db import *


# Определение функций
def delete_tables():
    Base.metadata.drop_all(engine)


def create_tables():
    Base.metadata.create_all(engine)


delete_tables()
create_tables()

# Добавление пользователей
add_user_test(username='admin', password='adminPass', role_type='admin', form_education='Бюджет',
              faculty='Информационные системы и технологии')
add_user_test(username='teacher1', password='teacherPass', role_type='teacher', form_education=None,
              faculty='Информационные системы и технологии')
add_user_test(username='student', password='student', role_type='student', study_group='211-365',
              form_education='Платная', faculty='Вычислительная техника и программное обеспечение')

# Добавление дисциплин
add_subject(name="Python")
add_subject(name="С++")
add_subject(name="Java")
add_subject(name="C#")

# Привязка пользователя к дисциплине по ID дисциплины
reg_user_in_subject(user_id=2, subject_identifier=1)
reg_user_in_subject(user_id=2, subject_identifier=2)
# Привязка пользователя к дисциплине по названию дисциплины
reg_user_in_subject(user_id=3, subject_identifier=1)
reg_user_in_subject(user_id=3, subject_identifier=4)

# Добавление заданий по ID дисциплины
add_task(name="Задание 1. Python - числовые типы", subject_identifier=1, description="Задача на числовые типы",
         max_symbols_count=128, max_strings_count=10, teacher_formula="b1=a1+a2-a3\nb2=b1+a2",
         input_variables="a1\na2\na3")
add_task(name="Задание 1. С++ - числовые типы", subject_identifier=2, description="Задача на числовые типы",
         max_symbols_count=128, max_strings_count=10, teacher_formula="c - d", input_variables="a3, a4")
add_task(name="Задание 2. Python - строки", subject_identifier=1, description="Задача на строки",
         max_symbols_count=128, max_strings_count=10, teacher_formula="a + b", input_variables="a1, a2")
add_task(name="Задание 2. С++ - строки", subject_identifier=2, description="Задача на строки",
         max_symbols_count=128, max_strings_count=10, teacher_formula="c - d", input_variables="a3, a4")
add_task(name="Задание 3. Python - списки", subject_identifier=1, description="Задача на списки",
         max_symbols_count=128, max_strings_count=10, teacher_formula="a + b", input_variables="a1, a2")
add_task(name="Задание 3. С++ - списки", subject_identifier=2, description="Задача на списки",
         max_symbols_count=128, max_strings_count=10, teacher_formula="c - d", input_variables="a3, a4")

add_task(name="Задание 1. Java - числовые типы", subject_identifier=3, description="Задача на числовые типы",
         max_symbols_count=128, max_strings_count=10, teacher_formula="a + b", input_variables="a1, a2")
add_task(name="Задание 2. Java - строки", subject_identifier=3, description="Задача на строки",
         max_symbols_count=128, max_strings_count=10, teacher_formula="a + b", input_variables="a1, a2")
add_task(name="Задание 3. Java - списки", subject_identifier=3, description="Задача на списки",
         max_symbols_count=128, max_strings_count=10, teacher_formula="a + b", input_variables="a1, a2")
add_task(name="Задание 4. Java - массивы", subject_identifier=3, description="Задача на массивы",
         max_symbols_count=128, max_strings_count=10, teacher_formula="a + b", input_variables="a1, a2")
add_task(name="Задание 5. Java - классы", subject_identifier=3, description="Задача на классы",
         max_symbols_count=128, max_strings_count=10, teacher_formula="a + b", input_variables="a1, a2")

add_task(name="Задание 1. C# - числовые типы", subject_identifier=4, description="Задача на числовые типы",
         max_symbols_count=128, max_strings_count=10, teacher_formula="a + b", input_variables="a1, a2")
add_task(name="Задание 2. C# - строки", subject_identifier=4, description="Задача на строки",
         max_symbols_count=128, max_strings_count=10, teacher_formula="a + b", input_variables="a1, a2")
add_task(name="Задание 3. C# - списки", subject_identifier=4, description="Задача на списки",
         max_symbols_count=128, max_strings_count=10, teacher_formula="a + b", input_variables="a1, a2")
add_task(name="Задание 4. C# - массивы", subject_identifier=4, description="Задача на массивы",
         max_symbols_count=128, max_strings_count=10, teacher_formula="a + b", input_variables="a1, a2")
add_task(name="Задание 5. C# - классы", subject_identifier=4, description="Задача на классы",
         max_symbols_count=128, max_strings_count=10, teacher_formula="a + b", input_variables="a1, a2")

# Добавление авто-тестов для заданий
add_test_case(input_data="1 2 0 7", output_data="10", task_id=1)
add_test_case(input_data="3 4 2 0", output_data="9", task_id=2)

# Добавление решения для задания
add_solution(code="print('Hello, World!')", user_id=3, task_id=1)
add_solution(code="print('Hello, World!')", user_id=3, task_id=3, mark=85, length_test_result=False,
             formula_test_result=True, auto_test_result=80)

# Добавление результатов тестирования
add_test_result(passed=True, test_case_id=1, solution_id=1)
add_test_result(passed=True, test_case_id=2, solution_id=2)

# Выставление оценки
evaluate_solution(solution_id=2, new_mark=100)

# Примеры получения данных
print("Информация о дисциплинах:")
subjects = get_subjects()
for subject in subjects:
    print(f"Subject ID: {subject.id}, Name: {subject.name}")
    subject_tasks = get_tasks_by_subject(subject.id)
    print(f"Задания дисциплины {subject.name}:")
    for task in subject_tasks:
        print(f"Task ID: {task[0]}, Name: {task[1]}")
        task_test_cases = get_test_cases_by_task(task_id=task[0])
        if len(task_test_cases) != 0:
            print(f"Авто-тесты для задания {task[1]}:")
        for test_case in task_test_cases:
            print(f"TestCase ID: {test_case.id}, Input: {test_case.inp}, Output:{test_case.out}")
    subject_users = get_users_by_subject(subject_id=subject.id)
    if len(subject_users) > 0:
        print(f"Пользователи, привязанные к дисциплине {subject.name}:")
    for user in subject_users:
        print(f"User ID: {user.id}, Username: {user.username}, Role: {user.roleType}, Group: {user.studyGroup}")
    print()

print("Информация о пользователях:")
users = get_users()
for user in users:
    print(f"User ID: {user.id}, Username: {user.username}, Role: {user.roleType}, Group: {user.studyGroup}")
    user_subjects = get_user_subjects(user.username)
    if len(user_subjects) != 0:
        print(f"Дисциплины пользователя {user.username}:")
    for user_subject in user_subjects:
        print(f"UserSubject ID: {user_subject[0]}, Name: {user_subject[1]}")
        user_subject_tasks = get_tasks_by_subject(user_subject[0])
        for user_subject_task in user_subject_tasks:
            user_subject_task_solutions = get_user_solutions_by_task(user.id, user_subject_task[0])
            if len(user_subject_task_solutions) != 0:
                print(f"Решения пользователя {user.username} для задания {user_subject_task[1]}:")
            for user_subject_task_solution in user_subject_task_solutions:
                print(
                    f"UserSubjectTaskSolution ID: {user_subject_task_solution.id}, Mark: {user_subject_task_solution.mark}")
                user_subject_task_solution_test_results = get_user_testCase_results_by_solution(user.id,
                                                                                                user_subject_task_solution.id)
                if len(user_subject_task_solution_test_results) != 0:
                    print(f"Результаты авто-тестов для задания {user_subject_task[1]}:")
                for user_subject_task_solution_test_result in user_subject_task_solution_test_results:
                    print(
                        f"UserSubjectTaskSolutionTestResult ID: {user_subject_task_solution_test_result.id}, Passed: {user_subject_task_solution_test_result.passed}")
    print()

print("Пользователи, привязанные к учебной группе 211-365")
group_users = get_users_by_group(study_group="211-365")
for user in group_users:
    print(f"User ID: {user.id}, Username: {user.username}, Role: {user.roleType}, Group: {user.studyGroup}")
print()

print("Решения пользователя по дисциплине с ID: 1")
user_task_solutions = get_user_solutions_by_task(user_id=3, task_id=1)
for user_task_solution in user_task_solutions:
    print(f"ID: {user_task_solution.id}, Mark: {user_task_solution.mark}")
