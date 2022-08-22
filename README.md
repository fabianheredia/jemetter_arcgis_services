# jemetter_arcgis_services

este proyecto esta pensado para reañizar pruebas de cargay estres para servicios dinamicos de ArcGIS server en esta version.

## Requerimientos

* python 3
  * pandas
* jdk

## Instalacion

1. descargue Jmetter y asegurece que ejecute bien [link](https://jmeter.apache.org/download_jmeter.cgi)

para ejecutar jmetter se puede ingresar por consola a la rura `[instalacion]/bin/`
dependiendo la instalacion ejecutar el .bat o el .sh

2. agregue plugins para jmetter [link](https://jmeter-plugins.org/)
   1. [time line](https://jmeter-plugins.org/wiki/CompositeGraph/)
   2. [Throughput Shaping Timer](https://jmeter-plugins.org/wiki/ThroughputShapingTimer/)
   3. [Transactions per Second](https://jmeter-plugins.org/wiki/TransactionsPerSecond/)
   4. [Sample result¶](https://jmeter-plugins.org/wiki/LatenciesOverTime/)
   5. [Response Times vs Threads](https://jmeter-plugins.org/wiki/ResponseTimesVsThreads/)
   6. [Custom Thread Groups](https://jmeter-plugins.org/?search=jpgc-casutg)
   
3. instalar los plugins en el jmeter antes de iniciarlo, para ello se descomprimen los archivos y se ponen en la carpeta lib de jmetter.
![instalacion plugins](/images/plugins.png)

4. Ejecutar jmetter

![jmetter](/images/jmetter.png)

aqui se puede cargar un plan de prueba existente o crear el propio.

5. ejecutar el plan [pln ssa](/dynamic_services/plan_upme/Tessplan)
