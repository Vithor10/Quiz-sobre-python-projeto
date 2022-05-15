from questions import quiz
import random
ranking={}

def check_ans(question, ans, attempts, score):
    """
    recebe os argumentos e confirma se a resposta do usuário está correta.
    Converte todas as respostas em minúsculas para garantir que o questionário não diferencia maiúsculas de minúsculas.
    """
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"resposta correta! \n seu score é:{score + 1}!")
        return True
    else:
        print(f"resposta errada :( \n voce perdeu {attempts - 1}  pontos sobraram! \ntente novamente...")
        return False


def print_dictionary():
    for question_id, ques_answer in quiz.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])


def intro_message():
    """
  Apresenta o usuário ao questionário e às regras e recebe uma entrada do cliente para iniciar o questionário.
    Retorna verdadeiro independentemente de qualquer tecla pressionada.
    """
    print("Bem Vindo ao quiz de python! \nVocê está pronto para testar seus conhecimentos a respeito dessa linguagem?")
    print("Teremos um total de 10 questões, voce pode pular a questão a qualquer momento, digitando 'skip'")
    input("pressione uma tecla para iniciar o quiz ;) ")
    return True


# python project.py
intro = intro_message()
while True:
    parte = 1
    score = 0
    user = input(str('Nome do Jogador> '))
    print()
    while parte < 6:
        score = score
        Lperguntas = quiz.keys()
        Lperguntas = list(Lperguntas)
        Lista_perguntas = random.choices(Lperguntas, k=5)
        while True:
            score = 0
            for question in quiz:
                attempts = 3
                while attempts > 0:
                    print(quiz[question]['question'])
                    answer = input("Digite a letra da sua resposta (para ir para proxima questão, digite 'skip') : ")
                    if answer == "skip":
                        break
                    check = check_ans(question, answer, attempts, score)
                    if check:
                        score += 1
                        break
                    attempts -= 1

    break
print(f"Sua pontuação final é {score}!\nobrigado por jogar!")
