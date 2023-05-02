import importlib
import os

if __name__ == '__main__':
    module_dir = 'hillel_HW_Git/lesson_6'
    for file in os.listdir(module_dir):
        if file.endswith('.py') and file.startswith('HW_'):
            task_number = file.split('_')[1].split('.')[0]
            print(f'**********Task № {task_number}**********')
            module_name = os.path.splitext(file)[0]
            module = importlib.import_module(f'{module_dir}.{module_name}')
            functions = [getattr(module, f) for f in dir(module) if callable(getattr(module, f)) and f.startswith('task_')]
            for function in functions:
                function()
            print('\n')
