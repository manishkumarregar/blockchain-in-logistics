import datetime as date


#############################################################################
# Utility for generating requrement request for sending to warehouse
#Transcation 1 : transaction from a truck to warehouse in json format for repair
# {
#  "from": id1,
#  "to": id2,
#  "data": ["item":quatity]
#  "time": timenow
#}

def requiremets(sender_id, receiver_id, type):
  trans = {"sender_id":sender_id, "receiver_id":receiver_id, "data":[{"tyre":1, "lightbulb":2}], "time":date.datetime.now()}
  return trans

# Utility for generating parking request for particular date 
#Transcation 2 : transaction from a truck to warehouse in json format for parking
# {
#  "from": id1,
#  "to": id2,
#  "parking": parking date
#  "time": timenow
#}

def parking(sender_id, receiver_id, date):
  trans = {"sender_id":sender_id, "receiver_id":receiver_id, "parking":date, "time":date.datetime.now()}
  return trans

