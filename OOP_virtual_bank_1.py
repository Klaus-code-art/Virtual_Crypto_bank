class EnterBank():

	bank_info = {'version': 0.2, 'autor' : 'Ladyzhenskiy_nikolay', 'Capital' : 10000,}

	def bank_info(bank_info):

		print("Версия банка >>>", bank_info['version'])
		print("Автор банка>>>", bank_info['autor'])
		print("Капитализация банка>>>", bank_info['Capital'])
		print("____________________________________________")

a = EnterBank()

a.bank_info()