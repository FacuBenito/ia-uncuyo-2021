# Inteligencia Artificial 

## Definición

    Una inteligencia artificial se puede definir como un conjunto de algoritmos que intenta simular un nivel de inteligencia igual o superior al del humano promedio. Decimos que "intentan simular" porque las IA no poseen consciencia de sí mismas. Estos algoritmos de alta complejidad tienen una potencia y un potencial tan grande que es fácil creer que son capaces de razonar y tomar decisiones propias, pero la realidad es que simplemente están siguiendo instrucciones y "tomando decisiones" basandose en el análisis de conjuntos de datos quizá más grandes de lo que podamos imaginar. A su vez, afirmamos que simulan un nivel de inteligencia "igual o superior" al humano ya que gracias al poder de cómputo de las computadoras actuales, estos algoritmos pueden realizar tareas a una velocidad impensable o resolver problemas de alta complejidad que podrían tomar años para que una persona humana los resolviera. Además de esta velocidad, dada la altísima disponibilidad de datos hoy en día, con los cuales se suele "alimentar" a estos algoritmos, logran resultados "superhumanos". Siendo que son capaces de mantener en una base de conocimento millones y millones de datos pertinentes a su funcionalidad, esto les da una ventaja muy extensa por sobre la cantidad de datos que puede analizar un humano por unidad de tiempo para encontrar patrones.

## Inteligencia vs Artificial

### Inteligencia

    Según una definición de diccionario, inteligencia es la "facultad de la mente que permite aprender, entender, razonar, tomar decisiones y formarse una idea determinada de la realidad". Nosotros creemos que esta definición solo puede ser alcanzada completamente por los humanos, por lo que el gran logro de los algoritmos a los que llamamos "Inteligencia Artificial" es que son los únicos entes no humanos capaces de dar la ilusión de que alcanzan esa definición en su totalidad. De forma natural, existen otros seres que pueden alcanzar esta definición de forma parcial, ya que los humanos son "animales racionales", otras especies animales pueden alcazar gran parte de esta definición, como ser capaces de aprender, entender y tomar decisiones, pero nunca lograrán razonar, ya que ser racionales es lo que diferencia a los humanos de estas otras especies. Es justamente el hecho de que las IAs parezcan tener la capacidad de razonar y no simplemente "tomar decisiones en base a entradas de datos" es lo que las hace una creación tan interesante y destacable.

### Artificial

    Como primer aproximación, "artificial" se puede entender como aquello creado por el hombre, siendo un antónimo de lo "natural". Aunque a su vez, artificial puede considerarse aquello que es "falso" o no es real. En este contexto, siendo que las IAs son algoritmos creados por humanos, pero que dan la sensación de tener inteligencia propia, pueden tener sentido ambas percepciones de la palabra artificial. Desde un enfoque, las IAs son el resultado los humanos creando inteligencia de forma antinatural, desde el otro enfoque, los humanos creando sistemas que dan la falsa sensación de inteligencia, pero en realidad es una ilusión y pura algoritmia por detrás. La decisión de cuál de los dos enfoques de la palabra es el más apropiado en este contexto, es casi filosófica y depende mayoritariamente también de la opinión que uno mismo tenga acerca de la inteligencia artificial y si es realmente "inteligente" o no. 

## Ejemplos de IAs

### VQGAN+CLIP

    VQGAN+CLIP es una IA que tiene la habilidad de crear imágenes, dibujos y "pinturas" a partir de texto que un usuario desee ingresar en el sistema. El objetivo es que la imagen creada pueda representar de forma fiel el significado o la semántica de la frase que el usuario ingresó, ya sea en un sentido literal o metafórico. 
    La IA mencionada está conformada por 3 redes neuronales separadas en dos subsistemas:
        
        1) CLIP (Contrastive Language-Image Pre-Training): esta red neuronal encuentra imágenes basándose en descripciones de lenguaje natural, es decir, asocia las palabras con su significado en imágenes. Con la información generada por esta red neuronal se alimenta luego a VQGAN.
		2) GAN (Generative Adversarial Networks): los sistemas GAN son aquellos en los que una red neuronal "generadora" sintetiza las imágenes o los datos, mientras que una segunda red neuronal "discriminadora" puntúa cada resultado de acuerdo a algún criterio de aceptación. A partir de esto el sistema se retroalimenta y a través de las sucesivas salidas o resultados busca alcanzar puntuaciones cada vez más altas.
		
	Los resultados dados por esta Inteligencia Artificial son realmente sorprendentes, crea imágenes similares a obras de arte haciendo difícil de creer que fueron creadas por un algoritmo. Lo cual nos lleva a debatir si esto es realmente considerable arte. Particularmente, nosotros consideramos que esto no califica como arte por algunos motivos:
		Primero, aunque las imágenes creadas sean bonitas o bellas, lo que caracteriza a toda obra de arte es que es un reflejo de la emocionalidad humana. Es decir, en el arte hay algún tipo de emoción, la cual lleva a una persona a ejecutar una pieza (ya sea visual, sonora o de cualquier índole). Afirmamos con total seguridad que las IAs no poseen ningún tipo de emoción ni voluntad (a menos que se la haya programado para simular eso, e incluso en ese caso, no es propia). 
		Segundo, carecen de originalidad. Si bien los artistas también suelen tener influencias y/o inspirarse en el trabajo de otros artistas, siempre algo propio de las experiencias del autor queda plasmado en la obra resultante. Para las IAs no es así, estas simplemente recolectan datos previos, buscan patrones y extraen lo mejor de eso. Y, como vemos, en ese proceso no hay nada propio, dadas dos IAs distintas, no podríamos identificar qué IA hizo cuál obra dada una base de conocimiento exactamente igual y programadas con algoritmos similares (es decir, una IA que simula acuarelas y otra que simula dibujo en lapiz claramente serían diferenciables pero por su estilo, no por su "sello propio").

    (Se encuentran en esta misma carpeta algunas imágenes de ejemplo creadas por VQGAN+CLIP).

### Github's Copilot

	El Copiloto de Github es una Inteligencia Artificial desarrollada por Github para ayudar a los programadores a hacer más fácil su tarea. Está basada en Codex, un sistema de IA creado por openAI. Copilot usa el contexto que se le ha proveído y sintetiza el código a devolver. Su confiabilidad radica en que tiene una base de conocimiento extremadamente extensa, ya que puede acceder a todos los repositorios públicos de Github. 
	Respecto a esta IA se ha creado un dilema en torno a si esta reemplazará a los programadores en un futuro. La realidad es que esto es incierto, sin embargo, nosotros somos de la opinión de que no sucederá. Nuestra posición se debe a que esta IA no puede innovar. Puede trabajar con una gran cantidad de código previo para autocompletar código en el que encuentra cierto patrón en que identifica que cierta porción de código es la que se debería escribir, pero no podría inventar o crear nuevas formas de hacer código. Mucho menos crear un nuevo paradigma de programación, los cuales sabemos que son útiles y necesarios para poder adaptar la forma en la que se va a pensar un proyecto. 

