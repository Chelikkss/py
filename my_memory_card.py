from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox
from random import shuffle


app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')

btn_OK = QPushButton('Ответить')
lb_qestion = QLabel('Какой национальности не существует?')


Radiogroupbox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

layout_main = QVBoxLayout()

Radiogroupbox.setLayout(layout_ans1)

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)



AnsGroupBox = QGroupBox('Результат теста')
text1 = QLabel('Правильно/Неправильно')
text2 = QLabel('Правильный ответ')

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

layout_res = QVBoxLayout()
layout_res.addWidget(text1, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(text2, alignment=(Qt.AlignHCenter | Qt.AlignTop))

layout_main = QVBoxLayout()

AnsGroupBox.setLayout(layout_res)

AnsGroupBox.hide()

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_qestion, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(Radiogroupbox)
layout_line2.addWidget(AnsGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_main.addLayout(layout_line1, stretch=2)
layout_main.addLayout(layout_line2, stretch=8)
layout_line3.addStretch(1)
layout_main.addLayout(layout_line3, stretch=1)
layout_line3.addStretch(1)
layout_line3.addStretch(5)



def show_result(res, right_answer):
    Radiogroupbox.hide()
    AnsGroupBox.show()
    text1.setText(res)
    text2.setText(right_answer)
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroup.setExclusive(False)    
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    Radiogroupbox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
        

def check_answer():
    answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
    if answers[0].isChecked():
        show_result('Правильно!', 'Энцы')
    else:
        show_result('Неверно', 'Энцы')

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

    def ask(q):
        answers = [q]
        shuffle(answers)
        right_answer = answers[0]
        wrong1 = answers[1]
        wrong2 = answers[2]
        wrong3 = answers[3]

        window = QWidget()
        window.setLayout(layout_main)
        window.setWindowTitle('Memo Card')

        window.show()
        app.exec_()

q = Question('Какой национальности не существует?', 'Энцы', 'Смурфы', 'Чулымцы', 'Алеуты')
ask(q)
btn_OK.clicked.connect(check_answer)

window.setLayout(layout_main)
window.show()
app.exec_()
