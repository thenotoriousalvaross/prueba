import numpy.random as ran

ARRIVE = 1
DEPART = 0

time_between_arrives = 2
time_serving = 1
total_clients = 1000

#Initialize
clock = 0
events = [(ARRIVE,ran.exponential(time_between_arrives))]
clients_in_queue = 0
cashier_busy = False

#report variables
clients = [clients_in_queue]
time = [clock]
cashier = [cashier_busy]
for i in range(total_clients):
    clock = events[0][1]
    if events[0][0] == ARRIVE:
        events.pop(0)
        events.append((ARRIVE,clock + ran.exponential(time_between_arrives)))
        clients_in_queue += 1
        if cashier_busy == False:
            clients_in_queue -= 1
            cashier_busy = True
            events.append((DEPART,clock + ran.exponential(time_serving)))
        events.sort(key=lambda tup: tup[1])
    elif events[0][0] == DEPART:
        events.pop(0)
        if clients_in_queue > 0:
            cashier_busy = True
            clients_in_queue -=1
            events.append((DEPART,clock + ran.exponential(time_serving)))
            events.sort(key=lambda tup: tup[1])
        else:
            cashier_busy = False
    time.append(clock)
    clients.append(clients_in_queue)
    cashier.append(cashier_busy)

#report
report = open("report.csv","w")
for time, cas, cli in zip(time,cashier,clients):
    report.write(str(time)+","+str(cas)+","+str(cli)+"\n")
report.close()
