import ollama

# Define the server URL explicitly, if needed
client = ollama.Client(base_url="http://localhost:port")  # Cambia `port` por el puerto que estés utilizando.

modelfile = '''
FROM llama3
SYSTEM: eres un adivino de palabras
'''

client.create(model='adivino', modelfile=modelfile)

response = client.chat(model='adivino', messages=[
    {
        'role': 'user',
        'content': 'es azul y se ve cada dia'
    }

])
