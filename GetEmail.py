email = input("Ingrese su direccion de email: ")
user_name = email[:email.index("@")]
domain_name = email[email.index("@")+1:email.index(".")]
#print (user_name, domain_name)
popular_domains = {
"gmail": "Google",
"hotmail":"Microsoft",
"yahoo":"Yahoo",
"outlook":"Microsoft"}

if domain_name in popular_domains.keys():
    print(f"Hola {user_name} veo que estas usando un dominio publico de {popular_domains[domain_name]}.")
else:
    print(f"Hola {user_name} veo que estas usando un dominio personalizado de {domain_name.title()}.")
