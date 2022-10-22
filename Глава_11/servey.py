class AnonymousSurvey:

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        """Выводит вопрос"""
        print(self.question)

    def store_responses(self, newResponse):
        """Сохраняет один ответ на опрос"""
        self.responses.append(newResponse)

    def show_result(self):
        """Выводит все полученные ответы"""
        print('Survey results:')
        for response in self.responses:
            print(f"- {response}")
