# Inteligencia Artificial Débil

Decimos que una IA es débil si pueden *actuar* como si fueran inteligentes.

En 1956 la propuesta que definió el campo de la Inteligencia Artificial, aseguraba que cada aspecto del aprendizaje o cualquier característica de la inteligencia puede ser descrita tan precisamente que se puede crear una máquina para simularla. Es decir, se asumió que la IA débil es posible y así se fundó la Inteligencia Artificial.

Podemos definir a la IA como la búsqueda del mejor programa agente dada una arquitectura. De esta manera una IA es completamente posible ya que para N bits tenemos 2^N posibilidades de programas agente, de manera que lo único se debería hacer es encontrar la mejor versión entre ellos.

La pregunta importante que suele ser planteada en estos debates es: **¿Pueden las máquinas _pensar_?**. Cuando en realidad esto es tan relevante como preguntar si un submarino puede nadar o si un avión puede volar. La pregunta que realmente se debería hacer es si las máquinas pueden pasar un test de comportamiento inteligente, también conocido como el _Test de Turing_.

## El argumento de discapacidad

Este argumento plantea que una máquina no podrá hacer ciertas cosas como: ser amables, amistosas, tener voluntad o sentido del humor entre otras.

La realidad es que los algoritmos tienen desempeños a niveles humanos en tareas que parecerían involucrar al criterio humano: "Aprender de la experiencia" o "diferenciar el bien del mal" según Turing. Paul Meehl, en 1955, estudió los procesos que tienen los expertos en tareas subjetivas tales como predecir ciertos eventos. Y se encontró con que en 19 de 20 estudios observados, simples algoritmos de aprendizaje estadístico predijeron mejor que los expertos.

No es sorpresa que las computadoras pueden hacer muchas cosas al mismo nivel o mejor que los humanos (incluso aquellas tareas que se cree que requiren mucho entendimiento humano). Lo cual no quiere decir que estas entienden lo que están haciendo al realizar estas tareas.

## La objeción matemática

Gracias al trabajo de Turing y Gödel se sabe que ciertas ecuaciones matemáticas no tienen respuesta en algunos sistemas formales. El ejemplo más famoso de esto es el teorema de la incompletud desarrollado por Gödel. Varios filósofos aseguraban que este teorema demuestra la inferioridad mental de las máquinas si se comparan con humanos ya que estas son sistemas formales que están limitados por dicho teorema. Hay 3 problemas con estas afirmaciones:

1. El teorema de la incompletud sólo se aplica a sistemas formales que pueden hacer aritmética. Esto incluye a las máquinas de Turin y la afirmación ya mencionada está basada en que las computadoras son máquinas de Turing. Esto no es verdadero ya que dichas máquinas son infinitas mientras que las computadoras son, ciertamente, finitas y pueden ser descritas como un gran sistema en la lógica proposicional, el cual no está sujeto al teorema planteado por Gödel.

2. Un agente no debería preocuparse de que no puede establecer la verdad de algúna afirmación mientras que otros agentes si pueden. Por ejemplo: ningún humano podría computar la suma de mil millones de números de 10 dígitos en una vida entera pero una computadora realiza esta tarea en segundos. Sin embargo, no pensamos en esto como una limitación del pensar humano.

3. Incluso si damos por hecho que las computadoras tienen limitaciones en lo que pueden demostrar, no hay evidencia de que los humanos son inmunes a dichas limitaciones. Es imposible probar que los humanos no están sujetos al teorema de Gödel porque cualquier prueba requeriría una formalización del pensamiento humano, el cual es informalizable, por lo que se refurataría a sí mismo.

## El argumento de informalidad

Es la afirmación de que el comportamiento humano es en demasía complejo como para ser capturado por cualquier conjunto de reglas y que porque las computadoras no pueden hacer más que seguir uno, no pueden generar comportamiento tan inteligente como el de los humanos. En IA, se conoce como **el problema de calificación** la inabilidad de capturar todo en un set de reglas lógicas.

La posición criticada se hizo conocida como "Good Old-Fashiond AI" ("La IA de la vieja escuela", se podría decir) o GOFAI. Esta se supone que afirma que todo comportamiento inteligente puede ser capturado mediante un sistema que razona lógicamente a partir de un conjunto de hechos y reglas que describen el dominio.

Dreyfus y Dreyfus proponen un proceso de 5 etapas para adquirir experiencia, comenzando con un procesamiento basado en rglas y finalizando con la habilidad de seleccionar respuestas correctas de manera inmediata. Proponen una arquitectura de red neuronal organizada como una biblioteca de casos. Sin embargo algunos problemas fueron encontrados:

1. Una buena generalizaación a partir de ejemplos no puede ser alcanzada sin conocimientos de fondo.

2. El aprendizaje de una red neuronal es una forma de aprendizaje supervisado, lo quie requiere una identificación previa de entradas relevantes y salidas correctas. Pero la realidad es que el aprendizaje puede ser alcanzado mediante _aprendizaje sin supervisión_ y _aprendizaje mediante refuerzo_

3. Los algoritmos de aprendizaje no tienen un buen rendimiento si tienen muchas características, y si se elige un subconjunto de ellas, no hay forma conocida para agregar nuevas características si dicho subconjunto demuestra ser inadecuado. Pero la realidad es que nuevos métodos como máquinas de vectores de soporte pueden manejar un conjunto muy grande de características con un buen desempeño.

4. El cerebro es capaz de dirigir sus sensores en búsqueda de información relevante y procesarla para extraer aspector pertinentes a la situación actual.

Muchos de los problemas en los que se enfocó Dreyfus son importantes y han sido incorporados como standares para el diseño de agentes inteligentes. Esto es una demostración del progreso de las IA.

# Inteligencia Artificial fuerte.

Muchos filósofos han afirmado que una máquina que pasa el test de Turing sigue sin pensar realmente, sino que es más bien una simulación. El profesor Geoffrey Jefferson habla de que una máquina no será equivalente a un cerebro hasta que tenga consciencia y voluntad propia. Turing le llama a esto el _Argumento de la consciencia_. El punto al que quiere llegar el profesor, está relacionado con la fenomenología: el estudio de la experiencia directa, es decir, la máquina tiene que poseer sentimientos. Otros se enfocan en la intencionalidad.

Turing plantea que el problema desaparecerá una vez que las máquinas alcancen un grado de sofisticación particular, lo cual quebraría con las diferencias entre IA débil y fuerte. Sin embargo, contra esto, tenemos un problema: los humanos *si* tienen mentes y las máquinas *pueden tener o no*. Para tratar este problema se debe entender que los humanos tienen mentes *reales*, no simplemente cuerpos que generan procesos neurofisiológicos.

Este problema, fue analizado en profundidad por René Descartes. Él consideró a la actividad de pensar y a los procesos físicos del cuerpo de tal manera que los dos deben existir en reinos separados. Esto da lugar a la **Teoría de la dualidad**.

El fisicalismo evita este problema afirmando que la mente no está separada del cuerpo (los estados mentales son estados físicos). Esto, en principio, nos da la posibilidad de la IA fuerte. El problema yace en explicar cómo los estados físicos pueden ser, al mismo tiempo, estados mentales.

## Estados mentales.

Al intentar explicar lo que significa que una persona esté en un estado mental, los fisicalistas se enfocan en los estados intencionales. Estos son estados que hacen referencia a algún aspecto del mundo exterior.

Si esto es correcto, entonces una descripción apropiada para el estado mental de una persona está determinada por el estado de su cerebro. El ejemplo de comer una hamburguesa y la simulación del estado mental de comer una hamburgesa, contradice el punto de vista que dice que el cerebro domina los estados mentales. Una forma de resolver este dilema es decir que el contenido de los estados mentales pueden ser vistos desde dos puntos:

1. El contenido amplio. Interpreta el estado mental como el punto de vista de un ser externo omnisciente con acceso a toda la situacion quien puede distinguir las diferencias en el mundo. Así, el contenido de los estados mentales involucra al cerebro y a la historia del ambiente. 

2. El contenido estrecho. Este considera sólo el estado del cerebro. La simulación del estado de comer una hamburguesa y comerla realmente, es el mismo.

Si lo que queremos saber es si la IA está realmente pensando y tiene estados mentales, entonces el punto de vista de contenido estrecho es el más apropiado. Este también es importante si estamos pensando en el diseño de las IA ya que es el contenido estrecho del estado del cerebro el que nos determina cual será el siguiente estado del mismo.

## Funcionalismo.

La teoría del funcionalismo sostiene que un estado mentral es el intermediario entre una entrada y una salida. Bajo este criterio, cualesquiera sean dos sistemas con procesos causales isomórficos, tendrían el mismo estado mental. Entonces, una computadora podría tener el mismo estado mental que una persona. Un ejemplo de esto es el experimento del reemplazo de cerebro. De esto salen tres posibles conclusiones:

1. Las causas de la consciencia que genera salidas en cerberos normales siguen funcionando en la versión electrónica por lo que esta es consciente.

2. Los eventos mentales conscientes en el cerebro normal no tienen una conexión causal con el comportamiento y no se encuentran en la versión electrónica por lo que esta no es consciente.

3. El experimento es imposible por lo que la especulación es inútil.

La segunda conclusión lleva la consciencia a lo que se conoce como el rol epifenomenal. Algo que ocurre pero no produce sombra en el mundo observable.

Patricia Churchland nota que los argumentos funcionalistas que operan a nivel neuronal también pueden funcionar al nivel de cualquier otra unidad funcional más grande.

## Naturalismo biológico.

Según el naturalismo biológico, los estados mentales son características emergentes de alto nivel, que son causados por procesos físicos de bajo nivel en las neuronas y que son las propiedades de ellas las que importan. Entonces los estados mentales no pueden ser duplicados sólo basandose en un programa con la misma estructura funcional con el mismo comportamiento de entrada salida. La conclusión de John Searle, a quién se atribuye el naturalismo biológico, concluye que correr el programa apropiado no es suficiente para ser una mente.

Teniendo en cuenta el ejemplo de la sala china, muchos comentadores proponen lo que Searle llama la respuesta del sistema. La objeción es preguntarle al humano si entiende chino es análogo a preguntarle al CPU si entiende raíces cúbicas. En ambos casos la respuesta es no y en ambos casos, de acuerdo con el sistema de respuestas, el sistema entero sí tiene la capacidad requerida.

La afirmación hecha por Searle se basa en 4 axiomas:

1. Los programas de computadora son formales (sintaxis).

2. Las mentes humanas tienen contenidos mentales (semántica).

3. La sintaxis no es constitutiva ni suficiente para la semántica.

4. Los cerebros producen mentes.

De los primeros 3 axiomas Searle concluye que los programas no son suficientes para las mentes. Y del cuarto axioma, concluye que cualquier otro sistema capaz de producir mentes tendría que tener poderes causales equivalentes a aquellos que posee un cerebro. 

## Consciencia, qualia y el vacío explicativo.

Siempre que hablamos de IA está presente el problema de la _consciencia_. Esta generalmente está dividida en aspectos como **entendimiento** y **autoconciencia**. Nos enfocaremos en el aspecto de la _experiencia subjetiva_: porqué se siente algo al tener un estado mental. El término técnico para la naturaleza de las experiencias es **qualia**.

Qualia presenta un desafío para los funcionalistas de la mente porque distintas qualia pueden estar involucradas en distintos procesos causales isomórficos.

Considerando el experimento del espectro invertido, llegamos a la conclusión de que no hay ninguna forma de razonar en la que podríamos llegar desde aquellos hallazgos a la conclusión de que la entidad que posee esas neuronas tiene alguna experiencia subjetiva particular.

El mismo Turing concede que el problema de la consciencia es difícil pero niega que tenga mucha relevancia para los fines prácticos de la IA.

# La ética y los riesgos de desarrollar Inteligencias Artificiales.

Es momento de que consideremos si _deberíamos_ desarrollar inteligencias artificiales. Estas nos traen nuevos problemas en cuanto a ética:

1. *La gente podría perder sus trabajos por la automatización*: Hasta ahora la automatización en general y la IA en particular han creado más trabajos que los que han eliminado. Resultando estos en más interesantes y con mejores pagos.

2. *La gente podría tener demasiado (o demasiado poco) tiempo de ocio*. La IA aumenta la velocidad con la que se innova en la tecnología y por ende contribuye a la tendencia a que la gente trabaje más duro, pero la IA también promete permitirnos tomarnos tiempo de descanso y dejar que ella se encargue de las cosas.

3. *La gente podría perder la sensación de ser únicos*. Esto nace de que la IA podría hacer posible la idea de que los humanos son autómatas, una idea que podría resultar en una pérdida de autonomía o incluso hasta humanidad. Si esta resulta ser exitosa podría ser tan amenazante a la moral de la sociedad moderna como la teoría de la evolución en el siglo XIX.

4. *Las IA podrían ser usadas con fines no deseados*. Cualquier tipo de tecnología de avanzada ha sido utilizada con frecuencia para que los poderosos eliminen a sus rivales. Esto se cumple en todas las ciencias, no sólo para las IA.

5. *El uso de IA podría resultar en una pérdida de responsabilidades*. Resulta difícil saber de quién es la culpa cuando se trata de un fallo por IA. Si un agente se vuelve significativamente más preciso que un humano, quizás los profesionales estén legalmente ligados a usar las recomendaciones de la IA.

6. *El éxito de las IA podría terminar siendo el fin de la raza humana*. Casi toda tecnología tiene el potencial de causar daño si cae en las manos equivocadas, pero con la IA se presenta un nuevo problema: las manos equivocadas podrían ser la propia tecnología. La pregutna es si una sistema de IA posee un mayor riesgo que el software tradicional. Hay tres fuentes de riesgo:

Primero, el sistema de IA podría realizar una estimación incorrecta causando que no tome una buena decisión. La forma correcta de arreglar esto es diseñar un sistema con checkeos y balances.

Segundo, especificar la funcionalidad correcta para un sistema de IA no es tan sencillo. Podríamos desarrollar una IA que frene el sufrimiento humano y que esta razone "si no hay humanos, no hay sufrimiento humano".

Tercero, el sistema de aprendizaje de la IA podría causar que esta evolucione a un sistema con comportamientos no deseados.

Yudkowsky propone diseñar una **IA Amigable**. El asegura que el deseo de no hacer daño a humanos debería plantearse desde un principio pero que los diseñadores deberían considerar que su propio trabajo puede tener errores y que la IA podría evolucionar con el tiempo. Esto podría dar lugar a un razonamiento como "Si los humanos creen moralmente correcto matar insectos molestos porque son, en parte, insectos con cerebros primitivos, entonces es moralmente correcto que yo mate a los humanos ya que su cerebro es primitivo en comparación al mío".

# Opiniones.

Personalmente creo que las IA son tan fascinantes como volátiles. Digo esto justamente por los últimos conceptos tratados, opino que, sin los controles adecuados una IA puede evolucionar de manera inesperada, como lo hizo, por ejemplo, la IA de Microsoft diseñada para hacer Tweets que con el tiempo se volvió racista y tuvieron que darla de baja. 

También, luego de esta lectura, creo que el mejor acercamiento hacia las inteligencias artificiales es el de las IA débiles ya que, al menos como lo veo ahora, no hay necesidad de que una IA sea consciente ni tenga voluntad ya que simplemente se diseñan para facilitar tareas humanas. Tal como dije en el párrafo anterior, que una IA sea consciente de si misma y pueda tener voluntad, al menos por ahora, supone un riesgo sobretodo porque al tener "habilidades superhumanas" podría estar siempre un paso adelante.



