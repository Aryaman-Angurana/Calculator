from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import ObjectProperty

Builder.load_file("1.kv")


operation = ""
prenum = 0
pre = []

class MyLayout(Widget):
    name = ObjectProperty(None)

    def clear(self):
        self.b1.text = ""
        self.b2.text = ""
        global prenum
        global operation
        global pre
        prenum = 0
        operation = ""
        pre = []


    def evaluate(self):
        exp = self.b1.text
        self.new_num = 0
        for i in range(len(exp) - 1, -1, -1):
            if (exp[i] != "." and not exp[i].isdigit() and exp[i] != "-"):
                self.new_num = i
                break
        else:
            self.new_num = -1
        self.new_num = float(exp[self.new_num + 1:])
        global prenum
        global operation
        global pre
        pre += [prenum]

        if operation == "+":   
            prenum += self.new_num
        elif operation == "-":   
            prenum -= self.new_num
        elif operation == "*":   
            prenum *= self.new_num
        elif operation == "/":   
            prenum /= self.new_num
        else:
            prenum = self.new_num


    def add(self):
        global operation
        if self.b1.text == "":
            return None
        elif self.b1.text[-1] == " ":
            self.b1.text = self.b1.text[: -3] + " + "
            operation = "+"
            return None
        self.evaluate()
        operation = "+"

        self.b1.text += " + "
        
        self.b2.text = str(prenum)


    def sub(self):
        global operation
        if self.b1.text == "":
            return None
        elif self.b1.text[-1] == " ":
            self.b1.text = self.b1.text[: -3] + " - "
            operation = "-"
            return None
        self.evaluate()
        
        operation = "-"

        self.b1.text += " - "
        
        self.b2.text = str(prenum)


    def mul(self):
        global operation
        if self.b1.text == "":
            return None
        elif self.b1.text[-1] == " ":
            self.b1.text = self.b1.text[: -3] + " * "
            operation = "*"
            return None
        self.evaluate()
        
        operation = "*"

        self.b1.text += " * "
        
        self.b2.text = str(prenum)


    def div(self):
        global operation
        if self.b1.text == "":
            return None
        elif self.b1.text[-1] == " ":
            self.b1.text = self.b1.text[: -3] + " / "
            operation = "/"
            return None
        self.evaluate()
        
        operation = "/"

        self.b1.text += " / "
        
        self.b2.text = str(prenum)


    def equal(self):
        if self.b1.text == "":
            return None
        elif self.b1.text[-1] == " ":
            return None
        self.evaluate()
        global operation
        
        operation = ""

        self.b1.text = str(prenum)
        
        self.b2.text = str(prenum)
        

    def back(self):
        global pre
        if self.b1.text != "":
            if self.b1.text[-1] != " ":
                self.b1.text = self.b1.text[:-1]
            else:
                self.b1.text = self.b1.text[:-3]
                self.b2.text = str(pre[-1])
                pre = pre[:-1]


    def change_sign(self):
        if self.b1.text != "":
            self.equal()
            self.b1.text = str(-1*(float(self.b1.text)))
            self.b2.text = str(-1*(float(self.b2.text)))
            global prenum
            prenum = float(self.b2.text)


    def text(self, num):
        self.b1.text += num
        


class CalculatorApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        Window.size = (300,500)
        
        return MyLayout()

if __name__ == "__main__":
    CalculatorApp().run()