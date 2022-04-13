#!/usr/bin/env python
# coding: utf-8

# In[2]:


##print ("Meta de vendas do mês de Abril")
meta = 5000
print(F' A meta do mês de abril é: {meta:2}\n')
valor_atingido = int(input("Digite o valor atingido:"))
if valor_atingido >= meta:
    print ("Parabéns, meta atingida!")
elif valor_atingido < meta:
     print ("Você não atingiu a meta. Se esforce mais")


# In[ ]:




