from sencore import EnVocabParser, EsVocabParser
import json
from tests.lib import *

def test_en_vocab_parser():
  lang = "en"
  senfile = "test_source/{}_test.json".format(lang)
  with open(senfile, encoding="utf8") as f:
    sentences = json.loads(f.read())

  p = EnVocabParser(lang)
  for s in sentences:
    doc = p._nlp(s)
    print(s)
    print("="*20)
    print_doc(doc)
    graph(doc, lang)
    print("="*20)
    vocabs = p.digest(s)
    print(vocabs)
    assert isinstance(vocabs, list) == True

sentences = [
  "No se me ahogue en un vaso de agua, señorita Quiroga, por favor, que seguro que al problema de la vivienda le encontramos remedio.",
  "Sí. Así que ya puede espabilarse y sacar el dinero de debajo de las piedras si hace falta, pero de forma limpia. ¿Queda claro?",
  "Déjese de milongas, el tránsito del Estrecho lleva semanas cortado y por allí no cruza ni las gaviotas.",
  "Descuide, mi comisario, que la Candelaria se encarga de todo.",
  "Vean, y ándese con ojo.",
  "Mire, no me fío ni un pelo de ninguna de las dos, así que las tendré vigiladas bien de cerca.",
  "Como me entere de algo extraño, me las llevo a comisaría y de allí no las saca ni el Sursum corda.",
  "Y al calabozo me las llevo como me entere de algo extraño.",
  "Ay, maldito alzamiento, a ver si se acaba de una vez este jaleo y podemos volver a la vida normal.",
  "Bueno, aquí te vas a quedar. ¿Qué te parece?",
  "Tú vete acomodándote, yo voy a salir, que tengo unos asuntos pendientes, pero a la hora de comer me lo tienes que contar todo despacio.",
  "Señorita, no se preocupe, Jamila recoge todo esto.",
  "Sagrario, se ahorra usted los comentarios sarcásticos.",
  "A sentarse y a callar.",
  "Siéntate.",
  "Esta... ¿Cómo te llamas, niña?",
  "El estofado me ha quedado de rechupete, si es que los trato como una madre y después se quejan. Ay.",
  "Qué lástima, tantos buenos mozos que se habrán sacrificado por el Gobierno de la República.",
  "Que te calles, que me tienes harta.",
  "Cállate.",
  "No te rías, Juanito, que reírse seca las entendederas.",
  "Por eso se ha tenido que levantar el Ejército, para acabar con tanta risa, con tanta alegría y con tanto libertinaje, que estaban llevando a España a la ruina.",
  "Cállese ya, tía vinagres, que es una tía vinagres.",
  "¡Se acabó! ¡Se acabó! ¡Se acabó!",
  "Y, niña, un baño tampoco te va a matar, hija, que estaremos en África, pero aquí la gente también se lava.",
  "Venga, levántate, que se enfría el desayuno.",
  "Dile a la señora Candelaria que ya he engordado los 3 kg que me pidió.",
  "El caso es que he engordado. Pues ya está Sigo con las patatas yo.",
  "Es que todavía no me encuentro con fuerzas. Antes estaba …",
  "¿Andrés a qué se dedica?",
  "¡Anda! No me digas que hay alguien que se está olvidando ya de su enamorado.",
  "Deben pasar años para que yo me ponga a pensar en hombres.",
  "¿Cuántas veces te he dicho que no entres a limpiar en mi habitación, que de eso me encargo yo?",
  "Usted tampoco vio nada. No se meta en líos.",
  "Se equivoca. Yo no soy la manera, créame.",
  "Pues nada, que he pensado que ya va a ser hora de que me busque un trabajito.",
  "Se ha quedado mucha gente atrapada aquí y sobran personas para trabajar.",
  "Bueno, bueno, todo se andará.",
  "Es que hay días que una se levanta con cualquier cosa …",
  "¡Me cago en todos mis muertos!",
  "Es la tercera falda que me cargo en una semana.",
  "Anda, niña, sigue con el desayuno mientras yo me cambio.",
  "A ver qué trapo me pongo ahora.",
  "Se han vuelto locos. Ya puedes administrarla bien, Jamila.",
  "Pruébese esto.",
  "Pues si el señorito no está a gusto, se puede mudar al hotel Nacional.",
  "Pero no se nos suba a la Parra, Candelaria.",
  "No me digan que se han apuntado de voluntarias en el frente.",
  "Pero ¿tú no vas a misa diaria y te encomiendas a los curas?",
  "Y cuidadito con mancharse los vestidos, que todavía no están pagados.",
  "Cuando me entere, te lo cuento, ¿eh?",
  "Que esas señorones se juntan con las coronelas y las generalas y no sabes el estilo que se gastan.",
  "¿Y por qué iba a quitarme el vestido para alguien que no quiere ayudarme a volver a mi casa?",
  "Palomares. Cuánto honor. ¿A qué se debe su visita?",
  "Palomares, yo le juro por lo más sagrado que ninguno sabía a qué se dedicaba este señor.",
  "Ya, pero el caso es que se alojaba en esta pensión, ¿no?",
  "Mira, tú cállate que tú y yo ya hablaremos largo y tendido.",
  "¿Qué quieres? ¿Quedarte a pasar la vida aquí para los restos?",
  "¿Se te ha olvidado la deuda de Tánger? ¿Y tu madre?",
  "Si nos pillan nos vamos las dos putitas a la cárcel o al cementerio civil.",
  "Y si se dan las circunstancias, hacer negocios.",
  "Pero si esto no tiene ni balas. Que nosotras no nos vamos a liar aquí a tiros con todo el mundo.",
  "Vosotras no os marcháis a ningún lado.",
  "Tú no sufras, mi alma, de eso me encargo yo.",
  "Acuéstate, prenda, que cuando despiertes mañana ya he vuelto con el dinero y nos ha cambiado la vida.",
  "Entonces usted se tiene que quedar en la pensión toda la noche, por si acaso.",
  "Niña, si no lo haces, lo perdemos todo. Olvídate de tu taller, de traer a tu madre. ¿Eso es lo que quieres?",
  "Listo. Ahora te pinto los ojos y te visto con un jaique, que dentro cabe el universo entero.",
  "Nada, que se me ha caído un vaso de agua al suelo.",
  "Métase en la cama.",
  "Como no se meta ahoro mismo en la cama, mañana por la mañana lo primero que hago es decirle a la Benita que se está usted viendo con el practicante los viernes en la cornisa.",
  "Una vez fuera, olvídate de quién eres.",
  "Si te encuentras con alguien, arrastra los pies como si fueras una vieja.",
  "No se preocupe, todo va a salir bien.",
  "A todo el mundo español, no a los musulmanes, que no te enteras, macho.",
  "Como el sargento se entere de que has andado molestando a una pobre marroquí, te vas a comer tres días de arresto en la alcazaba como tres soles, chaval.",
  "¿Se lo puede quitar usted misma?",
  "No estoy acostumbrada a que me desnude un desconocido.",
  "Me llamo Roberto.",
  "Vístase, rápido, hay que salir de aquí.",
  "Sí, madre, no se preocupe, que yo puedo solo.",
  "Sí, pero se ha ido con un buen palmo de narices.",
  "Olvídese de Palomares ya.",
  "Dese prisa, matutera.",
  "Candelaria, no se meta. Señorita Quiroga, le advertí que no me causara ningún problema. A la más mínima jugarreta …",
  "¿Se encuentra usted bien?",
  "Usted tiene razón, pero no es cómo se imagina.",
  "Sí, ya sabe, si me portaba bien con él.",
  "Voy a la lumbre a poner dos ollas con agua para que te des un baño y a prepararte unas compresas con un linimento para esos pies.",
  "Bueno, pues entonces... A lo Alejandro Dumas. Nos inventamos una versión romántica de tus peripecias.",
  "Ah, claro. Me llamo Rosalinda Fox.",
  "Me temo que esta pulsera ya tiene dueño.",
  "Si Ramiro se las llevó con él a Argentina, usted me lo dijo.",
]
def test_es_vocab_parser():
  lang = "es"
  #senfile = "test_source/{}_test.json".format(lang)
  #with open(senfile, encoding="utf8") as f:
  #  sentences = json.loads(f.read())

  p = EsVocabParser(lang)
  for s in sentences:
    doc = p._nlp(s)
    print(s)
    print("="*20)
    print_doc(doc)
    graph(doc, lang)
    print("="*20)
    vocabs = p.digest(s)
    print(vocabs)
    assert isinstance(vocabs, list) == True


