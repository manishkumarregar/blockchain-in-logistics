import transactions as tran

class Truck:
	def __init__():
		#auth function will validate the node and provide an id
		#also inform other nodes about this new node
		self.node_id = auth()
		blockchain = acquire_bc()
		#get blockchains of all other nodes.
		#verify the chains for any descipencies
		#update own chain


	#requirements in dictionary
	def send_requirements():
		#read data from stdin
		data = {"tyre":1, "lightbulb":2}
		receiver_id = find_warehouse(data)
		if(not receiver_id):
			print("Transaction failed due to non availability")
			return
		transact_dict = tran.requirements(self.node_id, receiver_id, data, 1)
		broadcast(transact_dict)
		#broadcast this transaction
		#miner will receive this and make block

	# #parking in dictionary
	# def send_parking(receiver_id, parking):
	# 	transact_dict = tran.requirements(self.node_id, parking)
	# 	broadcast(transact_dict)
	# 	#broadcast this transaction
	# 	#miner will receive this and make block

	#loop on all the blockchain and find suitable warehouse with all the requirements available
	def find_warehouse(data):
		#loop on all the blockchain and find suitable warehouse with all the requirements available
		return receiver_id

class Warehouse:
	def __init__():
		self.tyre = 100
		self.bulb = 100
		self.battery = 100
		#auth function will validate the node and provide an id
		#also inform other nodes about this new node
		self.node_id = auth()
		blockchain = acquire_bc()
		#get blockchains of all other nodes.
		#verify the chains for any descipencies
		#update own chain

	def add_resources():
		#read data from stdin
		data = {"tyre":10, "bulb":10}
		transact_dict = tran.add_res(self.node_id, data, 1)
		broadcast(transact_dict)
		#broadcast this transaction
		#miner will receive this and make block