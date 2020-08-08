
class Enterbank:

	def bank_info():
		bank_info = {'version': 0.2, 'autor' : 'Ladyzhenskiy_nikolay', 'Capital' : 10000,}
		print("Версия банка >>>", bank_info['version'])
		print("Автор банка>>>", bank_info['autor'])
		print("Капитализация банка>>>", bank_info['Capital'])
		print("____________________________________________")


	def main_menu():

		inter_message = input("Если вы хотите войти, ввведите 1, если зарегистрироваться, введите 2 >>> ")
		return inter_message

class Autotification(inter_message):

	print(user_inter_message)


bank_start = Enterbank


bank_start.bank_info()
login_in = Autotification
num = login_in(inter_message)

print(str(num))