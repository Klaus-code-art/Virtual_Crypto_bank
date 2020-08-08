import os
import requests

CONST = "(*****************************************)"

def bankinfo():
	bank_info = {'version': 0.2, 'autor' : 'Ladyzhenskiy_nikolay', 'Capital' : 10000,}
	print("Версия банка >>>", bank_info['version'])
	print("Автор банка>>>", bank_info['autor'])
	print("Капитализация банка>>>", bank_info['Capital'])
	print("____________________________________________")
	bank_create_folder()

def bank_create_folder(path = ""): #Если запущенная программа не находит в своем расположении папки с банком, то эта функция его создает
	path = str(os.getcwd())
	
	if "Virtual_bank_folder" in os.listdir(path):
		os.chdir(path + "\\" + "Virtual_bank_folder")
		banklogin(path)
	else:
		os.makedirs("Virtual_bank_folder")
		print("Создаю банк")
		bank_create_folder(path)

def banklogin(path):
	log_num = str(input("Если вы хотите войти введите 1, если вы хотите зарегистрироваться, введите 2>>> "))
	
	if log_num == "1":
		print("Вы выбрали вход:")
		login = input("Введите ваш логин>>> ")
		
		if login in os.listdir(path): #Если введеный пользователем логин есть в папке, то программа идет дальше
			os.chdir(path + "\\" + login)
			print(os.getcwd())
			print("Логин Найден")
			pass_control(path, login)
		else:
			print("К сожалению логина нет в базе...")
			ask = input("Хотите создать учетную запись? 1 = да, 0 = нет.")
			
			if ask == "1":
				print("Запрос на регистрацию принят")
				bankregister(path)
			elif ask == "0":
				print("Будем рады вас видеть, до свидания")
			else:
				banklogin(path)
	elif log_num == "2": #Создаем кортеж из рег данных и на их основе даем папку с названием указанного имени, и фаил с данными о пользователе
		bankregister(path)
	else: 
		print(CONST)
		print("Не верно задан запрос, повторите попытку...")
		print(CONST)
	banklogin(path)

def pass_control(path,login):
	print("Текущая директория изменилась на folder:", os.getcwd(), "Ваш Логин:", login)
	login = login + ".txt" #Присваиваем имя файла после того как зашли в папку с логином
	file = open(login,'r') #Открываем логин.txt
	str_dict = file.read() #Присваиваем переменной хеш, но он в формате str 
	dict_data = eval(str_dict) #Меняем формат str в dict
	pass_control = dict_data.get("password") # В словаре ищем значение с ключем пароля
	count = 3 #Счетчик попыток ввода пароля

	while count > 0: 
		print(pass_control)
		password_log = input("Введите пароль>>>")
		if password_log == pass_control: #Сравниваем указыванный пользователем пароль с вытащенным значением
			print("Вы указали верный пароль")
			credit_trade()
			break
		else:
			print("Вы указали не верный пароль")
			count = count - 1
			print("Повторите попытку", "Лимит попыток: ", count)
	print("Вы исчерпали лимит попыток ввода пароля")

def bankregister(path): #Функция запрашивает регистрационные данные пользователя
	os.chdir(path)
	print("Вам необходимо сформировать регистрационный запрос")
	email = input("Напишите ваш email>>> ")
	
	if email in os.listdir(path):
		print(CONST)
		print("такой логин уже есть, придумайте другой")
		print(CONST)
	else:
		first_name = input("Напишите ваше имя>>> ")
		last_name = input("Напишите вашу фамилию>>> ")
		patronymic = input("Напишите ваше отчество>> ")
		age = input("Сколько вам лет?>>> ")
		city = input("Город проживания?>>> ")
		phone_num = input("Номер вашего телефона?>>> ")
		citizenship = input("Ваше гражданство? >>> ")
		Bank_account = input("Напишите свой банковский номер/счет/номер банкоской карты>>> ")
		password = input("Придумайте пароль>>>")

		info_case = {'email':email, 'first_name':first_name, 'last_name': last_name,
		'patronymic': patronymic, 'age': age, 'city': city, 'phone_num': phone_num, 
		'citizenship': citizenship, 'Bank_account': Bank_account, "password":password}

		print(type(info_case))
		print(info_case)
		os.makedirs(email) #Создаем папку
		os.chdir(path + "\\" + email) # Заходим в созданную папку
		print(os.getcwd())
		text_file = open(email + ".txt", "w", encoding = "utf-8") #Создаем фаил регистрации с данным пользователя.
		info_case = str(info_case)
		text_file.write(info_case)
		text_file.close()
		print("Вас успешно зарегистрировали.")

		banklogin(path)

def credit_trade():
	print("Привет дорогой пользователь...")
	print("Введите 1 - чтобы просмотерть потребительский кредит")
	print("Введите 2 - чтобы просмотерть кредит для бизнеса")
	print("Введите 3 - чтобы просмотерть взятые вами кредиты")
	print("Введите 4 - чтобы просмотреть Криптовалютные пары")
	
	reply = input(">>>")
	
	if reply == "1":
		consumer_credit_verification()
	elif reply == "2":
		verification_business_loan()
	elif reply == "3":
		print("Ваша кретитная история:")
		history_credit_chack()
	elif reply == "4":
		print("Запушен модуль криптовалютного анализа рынка")
		crypto()
	else:
		print("Непредусмотренный вариант ответа, повторите попытку")
		credit_trade()

def consumer_credit_verification(sum_credit = 0, time_credit = 0): #принятие условий и рассчет потребительского кредита.
	path = str(os.getcwd())
	print("на кредит действуют следующие ограничения : сумма кредита не должна превышать; 300к и срок выплаты более 5 лет")
	print("Без процентной ставки")
	sum_credit = int(input("Введите сумму желаемого кредита>>>"))
	time_credit = int(input("Введите введите колличество месяцев выплачивания кредита>>>"))
	
	if sum_credit > 300000 and time_credit > 60:
		print("Вы нарушили условия выдачи кредита, ввести попробуйте снова")
		consumer_credit_verification()
	else:
		month = sum_credit / time_credit
		print("В месяц вам необходимо выплачивать", month, "рублей")
		answer = (input("Вы согласны на данные условия кредита?, Да - 1, Нет - 0"))
		
		if answer == "1":
			print("Активируется Аудит Клиент потребительского кредита")
			client_audit_consumer_credit(sum_credit, time_credit)
		elif answer == "0":
			print("Вы отказались от потребительского кредита, переводим вас к предложению пакетов")
			credit_trade()
		else:
			print("Программа не расспознает ваш ответ, указываете ответ без пробелов и лишних символов")
			consumer_credit_verification()

def verification_business_loan(sum_credit = 0, time_credit = 0): #По сути кредит для бизнеса но копия потребительского.
	path = str(os.getcwd())
	print("на кредит действуют следующие ограничения : сумма кредита не должна превышать; 300к и срок выплаты более 5 лет")
	print("Без процентной ставки")
	sum_credit = int(input("Введите сумму желаемого кредита>>>"))
	time_credit = int(input("Введите введите колличество месяцев выплачивания кредита>>>"))
	
	if sum_credit > 300000 and time_credit > 60:
		print("Вы нарушили условия выдачи кредита, ввести попробуйте снова")
		consumer_credit_verification()
	else:
		month = sum_credit / time_credit
		print("В месяц вам необходимо выплачивать", month, "рублей")
		answer = (input("Вы согласны на данные условия кредита?, Да - 1, Нет - 0"))
		
		if answer == "1":
			print("Активируется Аудит Клиента кредита для бизнеса")
			client_audit_business_loan(sum_credit, time_credit)
		elif answer == "0":
			print("Вы отказались от потребительского кредита, переводим вас к предложению пакетов")
			credit_trade()
		else:
			print("Программа не расспознает ваш ответ, указываете ответ без пробелов и лишних символов")
			consumer_credit_verification()

def client_audit_consumer_credit(sum_credit, time_credit):
	path = str(os.getcwd())
	print("Текущий путь>>" + path)
	print("Ваш кредит равен:", sum_credit,"Время погашения кредита", time_credit)
	income = int(input('Введите ваш ежемесячный заработок>>> '))
	work_experience = int(input('Введите колличество рабочих лет>>> '))
	
	if income >= 70000 and work_experience >= 5:
		print("Вы можете успешно взять потребительский кредит")
		print("Закрепите ваше согласие написав 1, либо 2 если вы решите передумать.")
		reply = input(">>>")
		
		if reply == "1":
			print("Вы взяли кредит. Можете отлеживать его состояние в разделе кредитного конотроля")
			os.chdir(path)
			history_credit_maker(sum_credit, time_credit)
		elif reply == "2":
			print("Вы решили передумать.")
		else:
			print("Неопознанный ответ, повторите попытку.")
			client_audit_consumer_credit(sum_credit, time_credit)
	else:
		print("Сожалеем, но вы не можете взять кредит на данный момент")
		banklogin(path)

def client_audit_business_loan(sum_credit, time_credit):
	path = str(os.getcwd())
	print("Ваш кредит равен:", sum_credit,"Время погашения кредита", time_credit)
	income = int(input('Введите уровень дохода бизнеса в месяц'))
	work_experience = int(input("Введите количество лет существания вашего бизнеса >> "))
	
	if income >= 100000 and work_experience >= 10:
		print("Вы можете успешно взять кредит для бизнеса")
		print("Закрепите ваше согласие написав 1, либо 2 если вы решите передумать.")
		reply = input(">>>")
		
		if reply == "1":
			print("Вы взяли кредит. Можете отлеживать его состояние в разделе кредитного конотроля")
			history_credit_maker(sum_credit, time_credit)
		elif reply == "2":
			print("Вы решили передумать.")
		else:
			print("Неопознанный ответ, повторите попытку.")
			client_audit_business_loan(sum_credit, time_credit)
	else:
		print("Сожалеем, но вы не можете взять кредит на данный момент")
		banklogin(path)

def crypto():
	print("Программа отображает состояние криптовалютной пары.")
	print("Вы вводите поочередно значения Валюты и вам выдается результат.")
	crypto1 = str(input("Введите первое значение >>>"))
	crypto2 = str(input("Введите второе значение >>>"))
	crypto_sum = crypto1 + "-" + crypto2
	print(crypto_sum)
	data=requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=' + crypto_sum)
	print(data.json())
	credit_trade()

def history_credit_maker(sum_credit, time_credit):
	path = str(os.getcwd()) #Значение текущего пути
	print(path)

	if "History_credit" in os.listdir(path):
		print("папка кредитных историй в наличии.")
		print(os.getcwd())
		os.chdir(path + "\\" + "History_credit")
		print(os.getcwd())
		num_credit_file_name = 1
		num_credit_file_name = str(num_credit_file_name) + ".txt"
		print(str(os.listdir()))
		if num_credit_file_name in str(os.listdir()):
			os.chdir(path + "\\" + "History_credit")
			num_credit_file_name = num_credit_file_name[:1] #Срезам .txt
			print(num_credit_file_name)
			num_credit_file_name = int(num_credit_file_name)
			num_credit_file_name = num_credit_file_name + 1
			print("Название файла с кредитом изменено на >>> ", num_credit_file_name)
			history_credit_maker()
			os.chdir(path)
		else:
			os.chdir(path + "\\" + "History_credit")
			credit_data = {"sum_credit":sum_credit, "time_credit":time_credit}
			text_file = open(num_credit_file_name + ".txt", "w", encoding = "utf-8") #Создаем фаил регистрации с данным пользователя.
			text_file.write(str(credit_data))
			text_file.close()
			os.chdir(path)
			print(os.getcwd())
			print("Кредит записан в файле с названием>>> " + num_credit_file_name)
			banklogin()
	else: 
		print(os.getcwd())
		os.makedirs("History_credit")
		history_credit_maker()

def history_credit_chack():
	path = str(os.getcwd()) #Значение текущего пути
	print(path)
	
	if "History_credit" in str(os.listdir(path)):
		os.chdir(path + "\\" + "History_credit")
		print(str(os.listdir(path)))
		files = os.listdir()
		if files == "": #Если в папке нет файлов, то
			print("Кредитные истории не найдены")
			credit_trade()
		else:
			print(str(os.listdir))
			credit_trade()
	else:
		print("Папки кредитных историй не найдено")
		credit_trade()

bankinfo()
print("Программа завершена.")