# ST-ABMS-individueel3

Dit is de code & het document dat hoort bij opdracht 3 van simulation tooling.

# main.py

Hierin wordt de simulatie gerunt, hieruit komen wat grafieken die de
GINI aangeven (een welvaarts indicator; hoeveel het geld verspreidt is, ook meteen
een soort standaarddeviatie). Deze is tot stand gekomen door de tutorial
van mesa (onderaan gelinkt)

# money_model.py

money_model.py bevat alle klasses om tot de simulatie te komen. Hij
bevat een Model klasse (MModel) die over-geerft wordt van de mesa
Model klasse; hierin worden de agents geinitialiseerd en bijgehouden.
Verder is er nog de Agent klasse (MAgent) die over-geerft wordt van de mesa
Agent klasse; deze beschrijft de individuele agents en hier zijn ook nog
attributen bij meegenomen en de verschillende functies die beschreven worden in het verslag.

# Tutorial

De tutorial is hieronder te vinden;

https://mesa.readthedocs.io/en/master/tutorials/intro_tutorial.html 