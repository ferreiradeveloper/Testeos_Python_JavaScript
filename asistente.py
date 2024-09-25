import ollama

modelfile = '''
FROM llama3
SYSTEM: eres un adivino de palabras
'''

ollama.create(model='adivino', modelfile=modelfile)

response = ollama.chat(model='adivino', messages={
    {
        'role':'user',
        'content': 'es azul y se ve cada dia'
    }
})

