from datetime import datetime, timedelta


ano = 2025
hora_inicio = 19
hora_fim = 21
intervalo = 1 

data_inicio = datetime(ano, 1, 1)
data_fim = datetime(ano, 12, 31)

op = ""

clients = [
    {"nome": "Bruno", "telefone": "999999999", "email": "bhsantos16@gmail.com", "endereço": "Capão da Canoa"},
    {"nome": "João", "telefone": "888888888", "email": "teste@gmail.com", "endereço": "Capão da Canoa"},
]
services = [
    {"nome": "Corte de Cabelo", "preço": "R$ 30,00", "duração": "00h30min"},
    {"nome": "Barba", "preço": "R$ 20,00", "duração": "00h20min"},
]	
prof = [
    {"nome": "Elisa", "telefone": "999999999", "email": "", "endereço": "Capão da Canoa", "serviços": "Corte de Cabelo"},
]
agend = []
disp_hours = []


def e_dia_util(data):
    return data.weekday() < 5

data_atual = data_inicio
while data_atual <= data_fim:
    if e_dia_util(data_atual):  # Verifica se é dia útil
        hora_atual = hora_inicio
        while hora_atual < hora_fim:
            disp_hours.append({
                "data": data_atual.strftime("%d-%m-%Y"),  # Formata a data como string
                "horario": f"{hora_atual:02}:00 - {hora_atual + intervalo:02}:00",
                "status": "Livre"
            })
            hora_atual += intervalo
    data_atual += timedelta(days=1)

def add_client(list):
    name = input("Digite o nome do cliente:")
    phone = input("Digite o telefone do cliente:")
    email = input("Digite o email do cliente:")
    address = input("Digite o endereço do cliente:")

    if not name or not phone or not email or not address:
        print("Todos os campos são obrigatórios!")
        return
    
    if (name, phone, email, address) in clients:
        print("Cliente já cadastrado!")
        return
    
    clients.append(
        {
            'nome': name,
            'telefone': phone,
            'email': email,
            'endereço': address
        }
    )
    print("Cliente adicionado com sucesso!")
    print()
    return list

def add_service(list):
    name = input("Digite o nome do serviço:")
    print()
    price = input("Digite o preço do serviço:")
    print()
    duration = input("Digite a duração do serviço: (Ex 01h30min) ")

    if not name or not price or not duration:
        print("Todos os campos são obrigatórios!")
        return
    
    if (name, price, duration) in list:
        print("Serviço já cadastrado!")
        return
    
    list.append(
        {
            'nome': name,
            'preço': price,
            'duração': duration
        }
    )
    print("Serviço adicionado com sucesso!")
    print()
    return list

def add_prof(list):
    name = input("Digite o nome do profissional:")
    phone = input("Digite o telefone do profissional:")
    email = input("Digite o email do profissional:")
    address = input("Digite o endereço do profissional:")
    services = input("Digite os serviços prestados pelo profissional:")

    if not name or not phone or not email or not address or not services:
        print("Todos os campos são obrigatórios!")
        return
    if(name, phone, email, address, services) in list:
        print("Profissional já cadastrado!")
        return
    
    list.append(
        {
            'nome': name,
            'telefone': phone,
            'email': email,
            'endereço': address,
            'serviços': services
        }
    )

    print("Profissional adicionado com sucesso!")
    print()
    return list

def list_prof(list):
    for prof in list:
        print(f"Nome: {prof['nome']}")
        print(f"Telefone: {prof['telefone']}")
        print(f"Email: {prof['email']}")
        print(f"Endereço: {prof['endereço']}")
        print(f"Serviços: {prof['serviços']}")
        print("")

def list_clients(clients):
    print("Lista de clientes:")
    for client in clients:
        print(f"Nome: {client['nome']}")
        print(f"Telefone: {client['telefone']}")
        print(f"Email: {client['email']}")
        print(f"Endereço: {client['endereço']}")
        print("")

def check_service(name,list):

    for service in list:
        if name == service['nome']:
            print(name, "cadastrado!")
            return True
    return False

def check_prof(name,list):
    for prof in list:
        if name == prof['nome']:
            print(name, "cadastrado!")
            return True
    return False

def list_hours(list): 
    for hour in list:
        if not hour:
            print("Nenhum agendamento cadastrado!")
            return
        print("")
        print(f"---- Serviços Agendados ----")
        print(f"Cliente: {hour['cliente']}")
        print(f"Serviço: {hour['serviço']}")
        print(f"Data: {hour['data']}")
        print(f"Horário: {hour['hora']}")
        print(f"Status: {hour['status']}")
        print("----------------------------")

def list_hour_disp(list):
    date = input("Digite a data desejada: dd-mm-aaaa: ")

    pesquisa = [item for item in list if item["data"] == date]

    for hour in pesquisa[:10]:
            print("")
            print(f"Data: {hour['data']}")
            print(f"Horário: {hour['horario']}")
            print(f"Status: {hour['status']}")
    if not pesquisa:
            print("Horário indisponível!")
    return

def list_services(list):
    for service in list:
        print(f"Nome: {service['nome']}")
        print(f"Preço: {service['preço']}")
        print(f"Duração: {service['duração']}")
        print("")

def check_hour(date,hour, hour_list):
    for horario in  hour_list:
        if (horario['horario'] == hour and horario['data'] == date):
            if horario['status'] == 'Livre':
                horario['status'] = 'Agendado'
                print(hour, "Agendado com sucesso!")
            return True
    return False

def add_agend(list):
    client = input("Digite o nome do cliente:")
    if not check_name_client(client,clients):
        print("Cliente não cadastrado!")
        print()
        return
    
    
    service = input("Digite o serviço:")
    if not check_service(service,services):
        print("Serviço não cadastrado!")
        list_services(services)
        print()
        return
    
    
    name_prof = input("Digite o nome do profissional:")
    if not check_prof(name_prof,prof):
        print("Profissional não cadastrado!")
        list_prof(prof)
        print()
        return
    
    date = input("Digite a data do agendamento: dd-mm-aaaa: ")
    hour = input("Digite o horário do agendamento: hh:mm - hh:mm: ")
    

    if not check_hour(date,hour,disp_hours):
        print("Horario indisponivel!")
        print()
        return
    
    obs = input("Digite alguma observação:")

    if not client or not service or not prof or not date or not hour:
        print("Todos os campos são obrigatórios!")
        return
    
    list.append(
        {
            'cliente': client,
            'serviço': service,
            'profissional': prof,
            'data': date,
            'hora': hour,
            'status': 'Agendado',
            'observação': obs
        }
    )

    print("Agendamento adicionado com sucesso!")
    print()
    return list

def check_name_client(name,list):
    for client in list:
        if name == client['nome']:
            print(name, "cadastrado!")
            return True
    return False

def list_agend(list):
    for agend in list:
        if not agend:
            print("Nenhum agendamento cadastrado!")
            return
        print(f"---- Agendamentos ----")
        print(f"Cliente: {agend['cliente']}")
        print(f"Serviço: {agend['serviço']}")
        print(f"Profissional: {agend['profissional']}")
        print(f"Data: {agend['data']}")
        print(f"Observação: {agend['observação']}")
        print("")


while (op != 'n' or op != 'N'):
    print()
    print("------ Seja bem vindo ------")
    print()
    print("1 - Adicionar um cliente")
    print("2 - Adicionar um serviço")
    print("3 - Adicionar um profissional")
    print("4 - Pesquisar horarios por data")
    print("5 - Horarios ocupados")
    print("6 - Adicionar um agendamento")
    print()

    num = int(input("Digite a opção desejada: "))
    if num == 1:
        add_client(clients)
        list_clients(clients)
        continue
    if num == 2:
        add_service(services)
        continue
    if num == 3:
        add_prof(prof)
        continue
    if num == 4:
        list_hour_disp(disp_hours)
        continue
    if num == 5:
        list_hours(agend)
        continue
    if num == 6:
        add_agend(agend)
        continue
    
    input('Deseja continuar? [s/n] ')
    if op == 'n' or op == 'N':
        break

