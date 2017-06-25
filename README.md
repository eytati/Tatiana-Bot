# Tatiana-bot

Diseño general de funcionamiento

Tati-bot es un bot web que  cumple conocimientos matematicos ya que las opreraciones matematicas que realiza es sumar, restar, multiplicar, calcular potencias, si un numero es primo o no, formula de pitagoras entre otros. 
EL bot tiene informacion propia y un id que es el identificador unico por medio de un hash. 
El diseño general se basa en el diagrama de flujo presentado anteriormente, este consiste en iniciar cuando se inicia el bot. Este bot aprende un conocimiento despues de ser aprendido puede aplicar el conocimiento, si este no sabe no da una respuesta de lo que se le solicita. Cada conocimiento despues de ser aprendido se puede ejecutar o eliminar, si se elimina el bot debera volver aprenderlo para poder realizar la ejecucion. 

![Imagen no cargada](https://github.com/eytati/Tatiana-bot/blob/master/imagen1.png)


Las arquitectura se basa en una memoria se basa principalmente en una matriz de conocimieto en esta se guardan instancias de lo que el bot aprende, esta matriz tiene que ser creada sobre un patron de diseño llamado singleton. Debe de poder buscar un conocimiento, agregar, borrar, eliminar y expandirse dependiendo de las necesidades de cada bot.La sgunda etapa es una getion de conocimiento que lo que hace es crear una barrera entre el api y lo que esta contenido en la memoria. Esta principalmente esta compuesta de las operaciones CRUD para acceder a la matriz.
El Api esta compuesta del servicio en general, ademas desde aca es donde se da el manejo principal de las rutas por medio d elas cuales se accede y se realiza las funciones que se deben cumplir. Estas rutas tienen sus propios identificadores para saber que hace y que es. Esta arquitectura ademas tiene un log como se mencion anteriormente el cual se guarda en un archivo txt la razon de esto es por que aperte de pantalla es comun encontar log de esta forma. Y en este caso no es necesario el tener una  base dedatos, si el log cumple de forma correcta. 

![Imagen no cargada](https://github.com/eytati/Tatiana-bot/blob/master/imagen2.png)

Modelo analisis

El digrama es la como interactua el cliente con le bot, el bot actua con conocimiento y con el log. El cliente interactua de forma directa con el conocimiento pero de forma indirecta con el log, ya que con este ultimo se puede observar pero no lo   puede editar. El log se va ir a registrando conforme se va interactuando con el api que es por donde tiene acceso a la informacion y el conocimiento.\\

En este caso no hay un manual de usuario ya que de  momento un usuario no podria interactuar directamente con la aplicacion ya que no posee una forma directa para la interaccion usuario aplicacion. 

![Imagen no cargada](https://github.com/eytati/Tatiana-bot/blob/master/imagen3.png)
