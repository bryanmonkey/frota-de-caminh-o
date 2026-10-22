frota = []
 
def normalizar(texto):
    return texto.strip().lower()
 
 
def normalizar_estado(estado):
   
    estado = estado.strip().lower()
   
   
    estados = {
        "são paulo": "SP",
        "sao paulo": "SP",
        "sp": "SP",
       
        "Paraná": "PR",
        "parana": "PR",
        "pr": "PR",
       
        "minas gerais": "MG",
        "mg": "MG",
       
        "rio de janeiro": "RJ",
        "rj": "RJ",
       
        "rio grande do sul": "RS",
        "rs": "RS",
       
        "bahia": "BA",
        "ba": "BA",
       
        "goiás": "GO",
        "goias": "GO",
        "go": "GO"
       
       
    }
   
   
    if estado in estados:
 
     return estado.upper()
 
def ler_ano():
   
    while True:
       
        try:
           
              ano = int(input("Ano do caminhão: "))
             
              if ano <= 0:
                  print("Digite um ano válido!")
                 
              else:
                  return ano
             
        except ValueError:
            print("Digite apenas números para o ano!")    
           
 
           
# Cadastrando o caminhao
 
 
 
def cadastrar_caminhao():
   
    placa = input("Placa: ")
    modelo = input("Modelo: ")
    motorista = input("Motorista: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    carga = input("Tipo de carga: ")
   
   
   
   
# o ano e lido através da função q tem o try/except
     
    ano = ler_ano()
 
   
    placa = normalizar("Placa: ")
    modelo = normalizar("Modelo: ")
    motorista = normalizar("Motorista: ")
    cidade = normalizar("Cidade: ")
    estado = normalizar_estado("Estado: ")
    carga = normalizar("Tipo de carga: ")
   
   
   
    placa_existe = False
   
 
 
for caminhao in frota:
   
    if caminhao["Placa"] == placa:
        placa_existe = True
        break
   
   
if placa_existe:
    print("\nEssa placa já está cadastrada!")
   
   
#Criando o caminhao
caminhao = {
    "Placa": placa,
    "Modelo": modelo,
    "Motorista": motorista,
    "Cidade": cidade,
    "estado": estado,
    "carga": carga,
    "Ano": ano
}
frota.append(caminhao)
 
print("Caminhão cadastrado com sucesso!")
 
def listar_caminhoes():
   
   
    print("\n============ LISTA DE CAMINHÕES ===============")
   
    if len(frota) == 0:
       
        print("Nenhum caminhão cadastrado.")
        return
   
   
    for numero in range(len(frota)):
       
        caminhao = frota[numero]
       
       
        print("\n--------------------------------------")
        print("Caminhão", numero +1)
        print("Placa:", caminhao["placa"])
        print("Modelo:", caminhao["modelo"])
        print("Motorista:", caminhao["motorista"])
        print("Cidade:", caminhao["cidade"])
        print("Carga:", caminhao["carga"])
        print("Ano:", caminhao["ano"])
       
       
       
    def procurar_placa():
       
        print("\n============= PESQUISAR POR PLACA ============")
       
       
        placa = input("Digite a placa: ")
        placa = normalizar(placa)
       
       
        encontrou = False
       
        for caminhao in frota:
           
            if caminhao["placa"] == placa:
               
                print("\nCaminhão encontrado!")
                print("Placa:", caminhao["placa"])
                print("Modelo:", caminhao["modelo"])
                print("Motorista:", caminhao["motorista"])
                print("Cidade:", caminhao["cidade"])
                print("Estado:", caminhao["carga"])
                print("Carga:", caminhao["carga"])
                print("Ano:", caminhao["ano"])
               
               
               
                encontrou = True
                break

