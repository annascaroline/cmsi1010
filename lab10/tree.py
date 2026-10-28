def create_people(person_type):
    odi = person_type("Odelie Copele", born="1824", died="1873")
    paul = person_type("Paul Grambois", born="1806")
    eugenie = person_type("Eugénie Granbois", born="1838",
                          died="1907", mom=odi, dad=paul)
    celeste = person_type("Céleste Lamelle", born="1814", died="1877")
    joey_b = person_type("Joey Baquié", born="1811", died="1882")
    ferdinand = person_type("Ferdinand Baquié", born="1837",
                            died="1883", mom=celeste, dad=joey_b)
    louise = person_type("Louise Baquié", born="1868",
                         died="1945", mom=eugenie, dad=ferdinand)
    julie = person_type("Julienne Montreuil", born="1796", died="1833")
    agenor = person_type("Agenor Ramos", born="1803", died="1846")
    marie = person_type("Marie Ramos", born="1826", died="1904",
                        mom=julie, dad=agenor)
    marge = person_type("Marguerite Cadeneth", born="1804", died="1870")
    giacamo = person_type("Giacamo Martino", born="1806", died="1852")
    jacques = person_type("Jacques Martinez", born="1822",
                          died="1891", mom=marge, dad=giacamo)
    joseph = person_type("Joseph Martinez", born="1864",
                         died="1926", mom=marie, dad=jacques)
    mildred = person_type("Mildred Martinez", born="1911",
                          died="1990", mom=louise, dad=joseph)
    jeanne_c = person_type("Jeanne Chauvin", born="1840", died="1866")
    romain = person_type("Romain Prévost", born="1832", died="1879")
    jeanne_p = person_type("Jeanne Prévost", born="1864",
                           mom=jeanne_c, dad=romain)
    louise_a = person_type("Louise Aubin", born="1814", died="1909")
    pierre = person_type("Pierre Fontaine", born="1818", died="1886")
    ernie = person_type("Ernest Fontaine", born="1857",
                        died="1919", mom=louise_a, dad=pierre)
    suzanne = person_type("Suzanne Fontaine", born="1894",
                          died="1979", mom=jeanne_p, dad=ernie)
    vittoria = person_type("Vittoria Trusiano", born="1813", died="1880")
    francesco = person_type("Francesco Alioto", born="c1813", died="c1880")
    maria = person_type("Maria Alioto", born="1834",
                        died=">1908", mom=vittoria, dad=francesco)
    concetta = person_type("Concetta Buccafusca", born="c1795", died="1843")
    giuseppe = person_type("Giuseppe Riggitano", born="c1786", died="1864")
    santo = person_type("Santo Riggitano", born="1824",
                        died="c1898", mom=concetta, dad=giuseppe)
    salvatore = person_type("Salvatore Riggitano", born="1876",
                            died="1960", mom=maria, dad=santo)
    louis = person_type("Louis Prevost", born="1920",
                        died="1997", mom=suzanne, dad=salvatore)
    leo = person_type("Robert Prevost", born="1955", mom=mildred, dad=louis)
    adele = person_type("Adele Martinez", mom=marie, dad=jacques)

    return {
        "odi": odi,
        "paul": paul,
        "eugenie": eugenie,
        "celeste": celeste,
        "joey_b": joey_b,
        "ferdinand": ferdinand,
        "louise": louise,
        "julie": julie,
        "agenor": agenor,
        "marie": marie,
        "marge": marge,
        "giacamo": giacamo,
        "jacques": jacques,
        "joseph": joseph,
        "mildred": mildred,
        "jeanne_c": jeanne_c,
        "romain": romain,
        "jeanne_p": jeanne_p,
        "louise_a": louise_a,
        "pierre": pierre,
        "ernie": ernie,
        "suzanne": suzanne,
        "vittoria": vittoria,
        "francesco": francesco,
        "maria": maria,
        "concetta": concetta,
        "giuseppe": giuseppe,
        "santo": santo,
        "salvatore": salvatore,
        "louis": louis,
        "leo": leo,
        "adele": adele,
    }
