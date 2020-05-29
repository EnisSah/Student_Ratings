import sqlite3
from price_reviews_demo import Student_Reviews
import tkinter as tk

HEIGHT = 500
WIDTH = 600

root = tk.Tk()
root.title('Student Ratings')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# background_image = tk.PhotoImage(file='4.png')
background_image = tk.PhotoImage(file='teacher.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bd=5)
frame.place(relx=0.5, rely=0.25, relwidth =0.6, relheight=0.4, anchor='n')

conn = sqlite3.connect("student_reviews.db")

c = conn.cursor()

''' Funkcija koja ce biti povezana sa dugmetom za dodavanje u bazu'''
def submit():
	conn = sqlite3.connect("student_reviews.db")
	c = conn.cursor()

	c.execute('INSERT INTO students_and_reviews VALUES(:first_name, :last_name, :age, :level, :number_of_sessions, :received_rating)',
		{'first_name': unos_imena.get(), 
		'last_name': unos_prezimena.get(), 
		'age' : unos_godina.get(), 
		'level': unos_levela.get(),
		'number_of_sessions': unos_broja_sesija.get(), 
		'received_rating' :unos_rejtinga.get()
			})

	unos_imena.delete(0,25)
	unos_prezimena.delete(0,25)
	unos_godina.delete(0,25)
	unos_levela.delete(0,25)
	unos_broja_sesija.delete(0,25)
	unos_rejtinga.delete(0,25)

	conn.commit()
	c.close()
	conn.close()

def search():
	conn = sqlite3.connect("student_reviews.db")
	c = conn.cursor()

	c.execute('SELECT * FROM  students_and_reviews WHERE first_name = :first_name AND last_name = :last_name',
		{'first_name': unos_imena.get(), 
		'last_name': unos_prezimena.get(), 
		'age' : unos_godina.get(), 
		'level': unos_levela.get(),
		'number_of_sessions': unos_broja_sesija.get(), 
		'received_rating' :unos_rejtinga.get()
			})
	print(c.fetchall())

	unos_imena.delete(0,25)
	unos_prezimena.delete(0,25)
	unos_godina.delete(0,25)
	unos_levela.delete(0,25)
	unos_broja_sesija.delete(0,25)
	unos_rejtinga.delete(0,25)

	conn.commit()
	c.close()
	conn.close()



# Labels 
ime_studenta = tk.Label(frame, text = 'Uneti ime:')
ime_studenta.grid(row = 1, column = 0)

prezime_studenta = tk.Label(frame, text = 'Uneti prezime:')
prezime_studenta.grid(row = 2, column = 0)

starost_studenta = tk.Label(frame, text = 'Uneti broj godina:')
starost_studenta.grid(row = 3, column = 0)

level_studenta = tk.Label(frame, text = 'Uneti level:')
level_studenta.grid(row = 4, column = 0)

broj_sesija = tk.Label(frame, text = 'Uneti broj sesija:')
broj_sesija.grid(row = 5, column = 0)

rating_od_studenta = tk.Label(frame, text = 'Uneti dobijeni rejting:')
rating_od_studenta.grid(row = 6, column = 0)


#Entry fields

unos_imena = tk.Entry(frame, width = 30)
unos_imena.grid(row = 1, column = 1)

unos_prezimena = tk.Entry(frame, width = 30)
unos_prezimena.grid(row = 2, column = 1)

unos_godina = tk.Entry(frame, width = 30)
unos_godina.grid(row = 3, column = 1)

unos_levela = tk.Entry(frame, width = 30)
unos_levela.grid(row = 4, column = 1)

unos_broja_sesija = tk.Entry(frame, width = 30)
unos_broja_sesija.grid(row = 5, column = 1)

unos_rejtinga = tk.Entry(frame, width = 30)
unos_rejtinga.grid(row = 6, column = 1)



# Dugme za snimanje u bazu
snimiti_studenta = tk.Button(frame, text = 'Dodati u bazu',command= submit, width = 25)
snimiti_studenta.grid(row = 7, column = 1)

# Dugme za pretrazivanje baze
pretraziti_studenta = tk.Button(frame, text = 'Pretraziti bazu', command= search, width= 25)
pretraziti_studenta.grid(row = 8, column = 1)


# conn = sqlite3.connect("student_reviews.db")

# c = conn.cursor()

''' posle kreiranja tabele
staljamo otvorenu zagradu da bismo napravili
koje sve kolone zelimo da imamo u nasoj tabeli'''

# c.execute("""CREATE table students_and_reviews (
# 		first_name text,
# 		last_name text, 
# 		age integer,
# 		level integer,
# 		number_of_sessions integer,
# 		received_rating integer
# 		)""")



# student_1 = Student_Reviews('Sarah', 'J', 7, 4, 123,8)
# student_2 = Student_Reviews('Jack', 'W', 6, 4, 123,9)

# c.execute("INSERT INTO students_and_reviews VALUES(?,?,?,?,?,?)", (student_1.first_name, 
# 	student_1.last_name, student_1.age, student_1.level,
# 	student_1.number_of_sessions, student_1.received_rating))

# conn.commit()

# c.execute("INSERT INTO students_and_reviews VALUES(:first_name, :last_name, :age, :level, :number_of_sessions, :received_rating)", 
# 	{'first_name':student_2.first_name, 'last_name': student_2.last_name, 'age' :student_2.age, 
# 	'level': student_2.level,'number_of_sessions': student_2.number_of_sessions, 
# 	'received_rating' :student_2.received_rating})
# c.execute('SELECT * FROM students_and_reviews ')

conn.commit()

# fetchall returns that number of rows as a list
# c.fetchmany(4)
# fetchone vraca jednog ali ne u obliku liste
# print(c.fetchone())

conn.commit()
conn.close()


root.mainloop()