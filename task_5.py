class TestCase:
    def __init__(self):
        self.steps={}
        self.result=None


def set_step(self,step_number, step_text):
    self.steps[step_number]=step_text


def delete_step(self, step_number):
    self.steps.pop(step_number)

def set_result(self, result):
    self.result = result

def get_test_case(self):
     print({
        'Шаги': self.steps,
        'Ожидаемый результат':self.result
    })

test = TestCase()

test.set_step(1, 'Открыть браузер')
test.set_step(2, 'Перейти на сайт')
test.set_result('Сайт успешно открылся')

test.get_test_case()