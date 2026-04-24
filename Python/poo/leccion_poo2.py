# POO Clase 2 - Métodos y atributos
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar_saldo(self):
        print(f"{self.titular} tiene un saldo de ${self.saldo}")

    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
        print(f"Depósito exitoso. Nuevo saldo: ${self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad
            print(f"Retiro exitoso. Nuevo saldo: ${self.saldo}")
        else:
            print("Saldo insuficiente!")

    def transferir(self, cantidad, destino):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            destino.saldo += cantidad
            print(f"Transferencia de ${cantidad} a {destino.titular} exitosa")
            print(f"Nuevo saldo de {self.titular}: ${self.saldo}")
        else:
            print("Saldo insuficiente!")

# Crear objetos
cuenta_adriano = CuentaBancaria("Adriano", 100000)
cuenta_juan = CuentaBancaria("Juan", 50000)

# Operaciones
cuenta_adriano.mostrar_saldo()
cuenta_juan.mostrar_saldo()
print("---")
cuenta_adriano.transferir(30000, cuenta_juan)
print("---")
cuenta_adriano.mostrar_saldo()
cuenta_juan.mostrar_saldo()

"""
📓 **Anota en tu cuaderno:**
```
Una sola clase → muchos objetos
cuenta_juan es un objeto de CuentaBancaria
no necesita su propia clase
"""




import spacy 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 
# Cargar modelo de spaCy para procesamiento de lenguaje natural 
nlp = spacy.load("es_core_news_sm") 
# Datos de entrenamiento para clasificación de intenciones 
intents = { 
'saludo': ['Hola', 'Hola, ¿cómo estás?', '¡Buen día!'], 
'despedida': ['Adiós', 'Hasta luego', 'Chao'], 
'consulta_tiempo': ['¿Qué tiempo hace hoy?', '¿Cuál es el pronóstico del clima?'], 
'consulta_noticias': ['¿Hay alguna noticia importante hoy?', 'Dime las últimas 
noticias'], 
'consulta_definicion': ['¿Qué significa esta palabra?', 'Explícame qué es'], 
2 
 
3 
 
Anexo  
    'agradecimiento': ['Gracias', '¡Gracias por tu ayuda!', 'Te agradezco mucho'], 
    'despedida_noche': ['Buenas noches', 'Hasta mañana', 'Que descanses'], 
    'consulta_instrucciones': ['¿Cómo puedo usar este chatbot?', 'Necesito ayuda con 
el chatbot'] 
} 
 
# Vectorizador TF-IDF para transformar texto a características numéricas 
vectorizer = TfidfVectorizer() 
 
# Transformar datos de entrenamiento 
train_data = [] 
labels = [] 
for intent, utterances in intents.items(): 
    train_data.extend(utterances) 
    labels.extend([intent] * len(utterances)) 
 
X_train = vectorizer.fit_transform(train_data) 
 
# Función para procesar la entrada del usuario y obtener respuesta 
def obtener_respuesta(input_text): 
    input_vector = vectorizer.transform([input_text]) 
     
    # Comparar similitud de coseno entre la entrada del usuario y los datos de 
entrenamiento 
    similarity_scores = cosine_similarity(input_vector, X_train) 
    max_similarity_index = similarity_scores.argmax() 
    intent = labels[max_similarity_index] 
     
    # Respuestas asociadas a la intención 
    if intent == 'saludo': 
        return "¡Hola! ¿En qué puedo ayudarte?" 
    elif intent == 'despedida': 
        return "Hasta luego. ¡Que tengas un buen día!" 
    elif intent == 'consulta_tiempo': 
        return "Hoy se espera un día soleado, con temperaturas moderadas." 
    elif intent == 'consulta_noticias': 
        return "Las noticias más recientes son sobre..." 
    elif intent == 'consulta_definicion': 
        return "La palabra significa..." 
    elif intent == 'agradecimiento': 
        return "¡De nada! Estoy aquí para ayudarte." 
    elif intent == 'despedida_noche': 
        return "Buenas noches. Descansa bien." 
    elif intent == 'consulta_instrucciones': 
        return "Puedes preguntarme sobre el clima, noticias, definiciones, o 
simplemente saludar." 
    else: 
        return "Lo siento, no entiendo tu pregunta." 
 
# Función principal para interactuar con el usuario 
def main(): 
 
4 
 
Anexo  
    print("¡Bienvenido al chatbot avanzado!") 
    while True: 
        usuario_input = input("Tú: ") 
        if usuario_input.lower() == 'salir': 
            print("¡Hasta luego!") 
            break 
         
        # Procesamiento de lenguaje natural con spaCy 
        doc = nlp(usuario_input) 
         
        # Obtener la respuesta basada en la intención clasificada 
        respuesta = obtener_respuesta(usuario_input) 
        print("Bot:", respuesta) 
 
# Iniciar el chatbot 
if __name__ == "__main__": 
    main(). 
           
           

       
      







