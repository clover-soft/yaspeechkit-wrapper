from nltk.classify import NaiveBayesClassifier
import pickle


class Analizator:
    def __init__(self):
        self.train_data = [
            ("Могу", "positive"),
            ("Да, отлично", "positive"),
            ("Хорошо, а сколько времени займет?", "question"),
            ("Нет, не очень хорошо", "negative"),
            ("Нет", "negative"),
            ("Ненадо", "negative"),
            ("Не интересно", "negative"),
            ("Некогда", "negative"),
            ("Да вы уже достали!", "negative"),
            ("Достали меня, ну ладно, соедините!", "positive"),
            ("А сколько времени займет?", "question"),
            ("Смотря сколько времени займет?", "question"),
            ("А долго?", "question"),
            ("Ну если это не долго, тогда давайте", "positive"),
            ("Если это займет немного времени, тогда давайте", "positive"),
            ("Да, это хорошо", "positive"),
            ("Нет, это неудобно", "negative"),
            ("Может быть", "question"),
            ("Не уверен", "question"),
            ("Да, это замечательно", "positive"),
            ("Нет, спасибо", "negative"),
            ("Мне неизвестно", "question"),
            ("Да, это интересно", "positive"),
            ("Нет, мне это не нужно", "negative"),
            ("Безусловно", "positive"),
            ("Я не думаю так", "negative"),
            ("Сложно сказать", "question"),
            ("А что вы думаете?", "question"),
            ("Да, это правильно", "positive"),
            ("Нет, это неправильно", "negative"),
            ("Я подумаю об этом", "question"),
            ("Я не могу ответить на это", "question"),
            ("Конечно, давайте сделаем это", "positive"),
            ("Нет, это не стоит делать", "negative"),
            ("Да, с удовольствием", "positive"),
            ("А как это работает?", "question"),
            ("Нет, не очень", "negative"),
            ("Нет, мне не интересно", "negative"),
            ("Да, уже достало!", "negative"),
            ("Достали меня, ну ладно, давайте соединимся!", "positive"),
            ("А сколько времени это займет?", "question"),
            ("Зависит от времени, сколько это займет?", "question"),
            ("А долго это будет длиться?", "question"),
            ("Если это займет немного времени, давайте", "positive"),
            ("Если это не займет много времени, я готов", "positive"),
            ("Да, это здорово", "positive"),
            ("Нет, это неудобно для меня", "negative"),
            ("Возможно", "question"),
            ("Я не уверен", "question"),
            ("Да, это отлично", "positive"),
            ("Нет, спасибо за предложение", "negative"),
            ("Я не знаю ответа", "question"),
            ("Да, это интересно для меня", "positive"),
            ("Нет, я не хочу этого", "negative"),
            ("Конечно", "positive"),
            ("Я не согласен с этим", "negative"),
            ("Это сложно сказать", "question"),
            ("А что вы думаете об этом?", "question"),
            ("Да, это верно", "positive"),
            ("Нет, это неправильно", "negative"),
            ("Я подумаю над этим", "question"),
            ("Я не могу ответить на это вопрос", "question"),
            ("Конечно, давайте сделаем это вместе", "positive"),
            ("Нет, это не стоит делать", "negative"),
            ("Да, я согласен с этим", "positive"),
            ("А какие есть альтернативы?", "question"),
            ("Нет, это не хорошо", "negative"),
            ("Нет, мне это неинтересно", "negative"),
            ("Да, я уже устал от этого!", "negative"),
            ("Давайте закончим с этим, соедините нас!", "positive"),
            ("А сколько времени это займет?", "question"),
            ("Сколько времени это займет?", "question"),
            ("А долго ли это продлится?", "question"),
            ("Если это не долго, давайте", "positive"),
            ("Если это займет немного времени, тогда я согласен", "positive"),
            ("Да, я считаю это хорошей идеей", "positive"),
            ("Нет, я не согласен с этим", "negative"),
            ("Возможно ли это?", "question"),
            ("Я не уверен в этом", "question"),
            ("Да, это замечательно", "positive"),
            ("Нет, спасибо, я отказываюсь", "negative"),
            ("Я не знаю", "question"),
            ("Да, это интересно", "positive"),
            ("Нет, это не нужно мне", "negative"),
            ("Безусловно, я согласен", "positive"),
            ("Я не думаю так", "negative"),
            ("Трудно сказать", "question"),
            ("А что вы думаете об этом?", "question"),
            ("Да, это правильно", "positive"),
            ("Нет, это неправильно", "negative"),
            ("Я подумаю над этим", "question"),
            ("Я не могу дать ответ на это", "question"),
            ("Конечно, давайте сделаем это", "positive"),
            ("Нет, это не стоит делать", "negative"),
            ("Не могу, я за рулем сейчас", "negative"),
            ("Я сейчас за рулем", "negative"),
            ("Я сейчас за рулем, но давайте", "positive"),
            ("Не могу сижу с ребенокм", "negative"),
            ("У меня маленький ребенок", "negative"),
            ("Я глуяю с ребенком, какой еще опрос", "negative"),
            ("Я не могу сижу с ребенком", "negative"),
        ]
        self.train_features = [(self.extract_features(text), label)
                  for (text, label) in self.train_data]
        self.classifier = NaiveBayesClassifier.train(self.train_features)
    def extract_features(self,text):
        words = text.lower().split()
        return {word: True for word in words}
    def classify(self,text):
        return self.classifier.classify(self.extract_features(text))