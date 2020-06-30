from PyQt5.QtWidgets import*
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.setObjectName("theWin")
        self.setStyleSheet("#theWin{\n"
        "background:#2e262f;\n"
        "}#theWin QPushButton{\n"
        "    width:50px;\n"
        "    height:50px;\n"
        "    border-radius:25px;\n"
        "    color:white;\n"
        "    margin:10px;\n"
        "    border:2px solid #623e0e; \n"
        "    font-size:20px;\n"
        "}\n"
        "#theWin QPushButton:hover{\n"
        "    width:50px;\n"
        "    height:50px;\n"
        "    border-radius:25px;\n"
        "    color:#2e262f;\n"
        "    background-color:#623e0e;\n"
        "    font-size:20px;\n"
        "    transition:3s;\n"
        "}\n"
        "\n"
        "")
        
        self.Dis = QLineEdit()
        layout.addWidget(self.Dis,0,1,1,4)
        self.Dis.setObjectName("Dis")
        self.Dis.setStyleSheet("#Dis{\n"
        "    padding:10px;\n"
        "    width:100%;\n"
        "    border:red solid 1px;\n"
        "    font-size:30px;\n"
        "    background:#433b44;\n"
        "    color:white;\n"
        "}")
        
        _clear_btn=QPushButton("CE")
        layout.addWidget(_clear_btn,1,1,1,1)
        _back=QPushButton("<")
        layout.addWidget(_back,1,2,1,1)
        _per=QPushButton("%")
        layout.addWidget(_per,1,3,1,1)

        Num_1=QPushButton("1")
        layout.addWidget(Num_1,2,1,1,1)
        Num_2=QPushButton("2")
        layout.addWidget(Num_2,2,2,1,1)
        Num_3=QPushButton("3")
        layout.addWidget(Num_3,2,3,1,1)

        

        Num_4=QPushButton("4")
        layout.addWidget(Num_4,3,1,1,1)
        Num_5=QPushButton("5")
        layout.addWidget(Num_5,3,2,1,1)
        Num_6=QPushButton("6")
        layout.addWidget(Num_6,3,3,1,1)

        Num_7=QPushButton("7")
        layout.addWidget(Num_7,4,1,1,1)
        Num_8=QPushButton("8")
        layout.addWidget(Num_8,4,2,1,1)
        Num_9=QPushButton("9")
        layout.addWidget(Num_9,4,3,1,1)


        
        Num_Minus=QPushButton("-")
        layout.addWidget(Num_Minus,5,1,1,1)
        Num_Mult=QPushButton("X")
        layout.addWidget(Num_Mult,5,2,1,1)
        Num_Plus=QPushButton("+")
        layout.addWidget(Num_Plus,5,3,1,1)

        Num_Sum=QPushButton("=")
        layout.addWidget(Num_Sum,6,1,1,2)
        Num_Div=QPushButton("/")
        layout.addWidget(Num_Div,6,3,1,1)

        sq=QPushButton("sq")
        layout.addWidget(sq,6,4,1,1)
        sqr=QPushButton("sqr")
        layout.addWidget(sqr,5,4,1,1)
        redu=QPushButton("re")
        layout.addWidget(redu,4,4,1,1)
        undo=QPushButton("ud")
        layout.addWidget(undo,3,4,1,1)
        Zero=QPushButton("0")
        layout.addWidget(Zero,2,4,1,1)
        Pow=QPushButton("pw")
        layout.addWidget(Pow,1,4,1,1)




        #events
        Num_1.clicked.connect(lambda:self.Num('1'))
        Num_2.clicked.connect(lambda:self.Num('2'))
        Num_3.clicked.connect(lambda:self.Num('3'))
        Num_4.clicked.connect(lambda:self.Num('4'))
        Num_5.clicked.connect(lambda:self.Num('5'))
        Num_6.clicked.connect(lambda:self.Num('6'))
        Num_7.clicked.connect(lambda:self.Num('7'))
        Num_8.clicked.connect(lambda:self.Num('8'))
        Num_9.clicked.connect(lambda:self.Num('9'))
        Zero.clicked.connect(lambda:self.Num('0'))


        Num_Plus.clicked.connect(lambda:self.setOpr('add'))
        Num_Mult.clicked.connect(lambda:self.setOpr('mult'))
        Num_Minus.clicked.connect(lambda:self.setOpr('min'))
        Num_Div.clicked.connect(lambda:self.setOpr('div'))
        Num_Sum.clicked.connect(lambda:self.setOpr(''))
        _back.clicked.connect(lambda:self.BackSp())
        _clear_btn.clicked.connect(lambda:self.clear())
        sq.clicked.connect(lambda:self.sq())
    Numstr=[]
    opr=""
    CurrVal="0"
    prev="0"
    def Num(self,num):
        self.Numstr.append(num)
        val=''.join(self.Numstr)
        self.Dis.setText(val)
    def clear(self):
        if  self.Numstr:
            self.Numstr=[]
            self.CurrVal=''.join(self.Numstr)
            self.Dis.setText(self.CurrVal)
    def setOpr(self,opr):
        if self.Numstr:
            self.prev=self.CurrVal
            self.CurrVal=''.join(self.Numstr)
            self.Numstr=[]
            self.do_as_opr()
            self.opr=opr

    
  

    def do_as_opr(self):
        if(self.opr=="add"):
            total=str(float(self.prev)+float(self.CurrVal))
            self.CurrVal=total
            self.Dis.setText(total)
        elif(self.opr==""):
            self.Dis.setText(self.CurrVal)
        elif(self.opr=="mult"):
            total=str(float(self.prev)*float(self.CurrVal))
            self.CurrVal=total
            self.Dis.setText(total)
        elif(self.opr=="div"):
            total=str(float(self.prev)/float(self.CurrVal))
            self.CurrVal=total
            self.Dis.setText(total)
        elif(self.opr=="min"):
            total=str(float(self.prev)-float(self.CurrVal))
            self.CurrVal=total
            self.Dis.setText(total)
        
    def sq(self):
        if  self.Numstr:
            Num_=int(''.join(self.Numstr))
            sq=Num_*Num_
            self.CurrVal=str(sq)
            self.Dis.setText(self.CurrVal)
    def BackSp(self):
        if  self.Numstr:
            self.Numstr.pop()
            self.CurrVal=''.join(self.Numstr)
            self.Dis.setText(self.CurrVal)

    def on_button_clicked(self):
        print("The button was pressed!")

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
