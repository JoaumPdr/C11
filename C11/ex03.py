while True:
    sexo = input("Digite o sexo (M para masculino ou F para feminino): ").strip().upper()

    if sexo == "M":
        print("Você é do sexo masculino.")
        break
    elif sexo == "F":
        print("Você é do sexo feminino.")
        break
    else:
        print("Sexo inválido! Por favor, digite M ou F.")
