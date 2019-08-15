from PyQt4 import QtGui, QtCore
import sys, words, random, start_page

class MyApp(QtGui.QMainWindow, words.Ui_MainWindow):
        def __init__(self):
            super(MyApp, self).__init__()
            self.setupUi(self)

class MyOpp(QtGui.QMainWindow, start_page.Ui_MainWindow):
        def __init__(self):
            super(MyOpp, self).__init__()
            self.setupUi(self)

def func_for_file():
    global list_of_words, five_words, form, my_dict, flag, result, wrong_answers, english, form
    flag, result, wrong_answers, five_words, list_of_words = 0, 0, 0, [], []
    for i in range(1, 11):
        my_dict[i].setVisible(True)
        my_dict[i].setEnabled(True)
    my_file = open('text.txt', 'r')
    if not english:
        my_file.close()
        my_file = open('names.txt', 'r')
    for line in my_file:
        line = line.strip()
        if not english:
            line = line.split()
            if len(line) == 3:
                list_of_words.append(line)
        else:
            list_of_words.append(line)
    my_file.close()
    for i in range(5):
        random_number = random.randint(1, len(list_of_words) - 1)
        while list_of_words[random_number] in five_words:
            random_number = random.randint(1, len(list_of_words) - 1)
        five_words.append(list_of_words[random_number])
    for i in range(1, 6):
        if english:
            my_dict[i].setText(five_words[i - 1][:five_words[i - 1].index('--')])
        else:
            my_dict[i].setText(five_words[i - 1][0])
    ran = [6, 7, 8, 9, 10]
    random.shuffle(ran)
    for i in range(5):
        if english:
            my_dict[ran[i]].setText(five_words[i][five_words[i].index('--') + 2:])
        else:
            my_dict[ran[i]].setText(five_words[i][2])

def buttons_listener(pushButton, button_index, a, b):
    global flag, result, my_dict, five_words, form, wrong_answers, english, form
    check = ""
    secondcheck = ""
    thirdcheck = ""
    if flag in range(a, b):
        w = str(my_dict[flag].text())
        ind = -1
        for i in range(5):
            if (a == 6):
                secondcheck = five_words[i][2]
            elif (a == 1):
                secondcheck = five_words[i][0]
            if english:
                if (five_words[i].find(w) != -1):
                    ind = i
                    break
            else:
                if (secondcheck == w):
                    ind = i
                    break
        if (a == 6 and english):
            check = five_words[ind][:five_words[ind].find('--')]
        elif (a == 6 and (not english)):
            thirdcheck = five_words[ind][0]
        elif (a == 1 and english):
            check = five_words[ind][five_words[ind].find('--') + 2:]
        elif (a == 1 and (not english)):
            thirdcheck = five_words[ind][2]
        if (english and str(pushButton.text()) == check):
            pushButton.setVisible(False)
            my_dict[flag].setVisible(False)
            result += 1
            if result == 5:
                QtGui.QMessageBox.information(form, "Result", "Amount of wrong answers: " + str(wrong_answers), QtGui.QMessageBox.Ok)
                func_for_file()
            flag = 0
        elif (not english and str(pushButton.text()) == thirdcheck):
            pushButton.setVisible(False)
            my_dict[flag].setVisible(False)
            result += 1
            if result == 5:
                QtGui.QMessageBox.information(form, "Result", "Amount of wrong answers: " + str(wrong_answers), QtGui.QMessageBox.Ok)
                func_for_file()
            flag = 0
        else:
            form.label_2.setText(str(int(form.label_2.text()) + 1))
            wrong_answers += 1
    else:
        if flag != 0:
            my_dict[flag].setEnabled(True)
        pushButton.setEnabled(False)
        flag = button_index

def one():
    buttons_listener(form.pushButton, 1, 6, 11)
def two():
    buttons_listener(form.pushButton_2, 2, 6, 11)
def three():
    buttons_listener(form.pushButton_3, 3, 6, 11)
def four():
    buttons_listener(form.pushButton_4, 4, 6, 11)
def five():
    buttons_listener(form.pushButton_5, 5, 6, 11)
def six():
    buttons_listener(form.pushButton_6, 6, 1, 6)
def seven():
    buttons_listener(form.pushButton_7, 7, 1, 6)
def eight():
    buttons_listener(form.pushButton_8, 8, 1, 6)
def nine():
    buttons_listener(form.pushButton_9, 9, 1, 6)
def ten():
    buttons_listener(form.pushButton_10, 10, 1, 6)

def english_russian():
    global english, firm, form
    wrong_answers = 0
    english = True
    firm.hide()
    form.show()
    func_for_file()

def name_meaning():
    global firm, form
    firm.hide()
    form.show()
    func_for_file()

def back():
    global firm, form, english, wrong_answers
    wrong_answers = 0
    form.label_2.setText(str(wrong_answers))
    english = False
    form.hide()
    firm.show()
app = QtGui.QApplication(sys.argv)
form = MyApp()
firm = MyOpp()
firm.show()
firm.pushButton.clicked.connect(english_russian)
firm.pushButton_2.clicked.connect(name_meaning)
form.pushButton_11.clicked.connect(back)

english = False
my_dict = {1: form.pushButton, 2: form.pushButton_2, 3: form.pushButton_3, 4: form.pushButton_4, 5: form.pushButton_5, 6: form.pushButton_6, 7: form.pushButton_7, 8: form.pushButton_8, 9: form.pushButton_9, 10: form.pushButton_10}
my_list = [1, one, two, three, four, five, six, seven, eight, nine, ten]
for i in range(1, 11): my_dict[i].clicked.connect(my_list[i])
list_of_words, five_words, flag, result, wrong_answers = [], [], 0, 0, 0
sys.exit(app.exec_())
