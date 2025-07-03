# 🎰 Terminal Slot Machine Game

This is a simple **text-based slot machine game** written in Python.

---

## 💡 What It Does

- Lets the user deposit money.  
- Allows betting on 1 to 3 horizontal lines.  
- Spins a 3x3 slot machine with random symbols.  
- Pays out based on matching symbols in each line.  
- Keeps track of balance, winnings, and number of spins.  

---

## 📸 Sample Run

```
Enter the amount to deposit : $100  
Enter the number of lines to bet (1 - 3) : 2  
Enter the amount to bet (per line) : $5  
Are you sure you want to bet $5 on 2 lines, for a total of $10? You have $100 left. (Y/N/Q) : Y

     Col 1    Col 2    Col 3  
Line 1   A        A        A  
Line 2   B        C        D  
Line 3   C        D        B  

You won $25 on line 1.  
You lost on line 2.  
You did not bet on line 3.

Spin Winnings : $25  
Total Winnings : $25  
Updated Balance : $115
Change in Balance : $15
```

---

## 🧠 Why I Built This

This is my first Python project and was built to practice:

- Writing clean input/output logic  
- Using loops, conditionals, and functions  
- Working with `pandas` and randomization  
- Learning how to structure a complete terminal-based game

---

## 📁 How to Run It

Make sure you have Python 3 installed.

```
pip install pandas
python slot_machine.py
```

---

## 🔰 Beginner Project

This is a beginner-friendly project and a great starting point if you're learning Python and want to build something fun in the terminal!
