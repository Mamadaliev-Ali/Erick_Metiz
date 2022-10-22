from servey import AnonymousSurvey

# Определение вопроса с созданием экземпляра класса
question = "What language did you first learn to spek"
mySurvey = AnonymousSurvey(question)

# Вывод вопроса и сохранение ответов
mySurvey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    mySurvey.store_responses(response)


# Вывод результата
print("\nThank you to everyone who participated in the survey!")
mySurvey.show_result()