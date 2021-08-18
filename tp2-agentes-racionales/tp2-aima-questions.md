# 2.10

## Can a simple reflex agent be perfectly rational for this environment?

Depende de si nuestro entorno es muy grande o no. Si nuestro entorno es pequeño podríamos resolverlo en pocos movimientos. Pero, cuando el entorno crece necesitamos más movimientos ya que, primero es más grande y segundo podríamos recorrer casillas que ya hemos limpiado.

## What about a reflex agent with state?

En este caso el agente sería más eficiente: al saber qué casillas hemos limpiado, podemos llevar un registro de qué casillas evitar de esa forma ahorramos acciones innecesarias al recorrer casillas que ya limpiamos.

## How do your answers to a and b change if the agent’s percepts give it the clean/dirty status of every square in the environment?

Como sabemos qué casillas tenemos que limpiar podemos ir directamente a las casillas sucias disminuyendo la cantidad de acciones a realizar y no necesitamos mantener un estado con las casillas que hemos limpiado. Así, un agente con estado resulta menos eficiente ya que estaríamos usando memoria innecesariamente.

# 2.11

## Can a simple reflex agent be perfectly rational for this environment?

Sí, podría serlo dependiendo nuevamente de el tamaño de nuestro entorno. Se podría limpiar todo pero a medida que nuestro entorno crece, serán mayor la cantidad de acciones necesarias

## Can a simple reflex agent with a randomized agent function outperform a simple reflex agent?

Podría hacerlo en los casos extremos en el que la combinación de acciones aleatorias da como resultado el camino más eficiente entre las casillas sucias (que de hecho tampoco sabemos donde están). En el resto de los casos, creo que un agente no-aleatorio sería mejor.

## Can you design an environment in which your randomized agent will perform poorly?

Por ejemplo un entorno donde sólo las casillas en las fronteras del mismo están sucias.

## Can a reflex agent with state outperform a simple reflex agent?

En un caso en el que el agente reflexivo simple tiene un algoritmo de recorrido que le impide recorrer casillas ya limpiadas (por ejemplo ir hacia una frontera e ir recorriendo el entorno en "espiral"), este podría superar al agente con estado. En cualquier otro caso, creo que el agente reflexivo simple, es inferior.
