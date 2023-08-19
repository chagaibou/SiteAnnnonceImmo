tanger_tetouan_al_hoceima = 'Tanger-Tétouan-Al Hoceïma'
l_oriental = "l'Oriental"
fes_meknes = 'Fès-Meknès'
rabat_sale_kenitra = 'Rabat-Salé-Kénitra'
beni_mellal_khenifra =  'Béni Mellal-Khénifra'
casablanca_settat = 'Casablanca-Settat'
marrakech_safi = 'Marrakech-Safi'
draa_tafilalet = 'Drâa-Tafilalet'
souss_massa =  'Souss-Massa'
guelmim_oued_noun = 'Guelmim-Oued Noun'
laayoune_sakia_el_hamra = 'Laâyoune-Sakia El Hamra'
dakhla_oued_ed_dahab = 'Dakhla-Oued Ed Dahab'



REGION_CHOICES = (
(tanger_tetouan_al_hoceima, 'Tanger-Tétouan-Al Hoceïma'),
 (l_oriental, "l'Oriental"),
 (fes_meknes, 'Fès-Meknès'),
 (rabat_sale_kenitra, 'Rabat-Salé-Kénitra'),
 (beni_mellal_khenifra, 'Béni Mellal-Khénifra'),
 (casablanca_settat, 'Casablanca-Settat'),
 (marrakech_safi, 'Marrakech-Safi'),
 (draa_tafilalet, 'Drâa-Tafilalet'), ('souss_massa', 'Souss-Massa'),
 (guelmim_oued_noun, 'Guelmim-Oued Noun'),
 (laayoune_sakia_el_hamra, 'Laâyoune-Sakia El Hamra'),
 (dakhla_oued_ed_dahab, 'Dakhla-Oued Ed Dahab')
)




JARDIN = 'jardin'
TERASSE = 'terasse'
BALCON = 'balcon'
MEUBLE = "meublé"
CUISINE = "cuisine"
MACHINE_A_LAVER = "machine à laver"
TV = 'tv'
CARACTERISTIQUES_CHOICES = (
        (JARDIN,'jardin'),
        (TERASSE,'terasse'),
        (BALCON , 'balcon'),
        (MEUBLE , "meublé"),
        (CUISINE , "cuisine"),
        (MACHINE_A_LAVER,'machine à laver')
)

CENTRE_VILLE = "centre_ville"
MEDINA = "medina"
MOULAY_ISMAIL = "moulay_ismail"
JAWHARA = "jawhara"
SIDI_BOUZID = "sidi_bouzid"
BIR_RAMI = "bir_rami"
MEHDIYA = "mehdiya"
MANSOURIA = "mansouria"
VAL_FLEURI = "val_fleuri"
IBN_TACHFINE = "ibn_tachfine"
EL_OULFA = "el_oulfa"
HASSAN_II = "hassan_ii"
AL_QODS = "al_qods"
AL_AMAL = "al_amal"
AL_MANAR = "al_manar"
VILLE_HAUTE = "ville_haute"
DOHA = "doha"
MAAMORA = "maamora"
SAKNIA = "saknia"

QUARTIERS_KENITRA_CHOICES = (
    (CENTRE_VILLE, "centre_ville"),
    (MEDINA, "medina"),
    (MOULAY_ISMAIL, "moulay_ismail"),
    (JAWHARA, "jawhara"),
    (SIDI_BOUZID, "sidi_bouzid"),
    (BIR_RAMI, "bir_rami"),
    (MEHDIYA, "mehdiya"),
    (MANSOURIA, "mansouria"),
    (VAL_FLEURI, "val_fleuri"),
    (IBN_TACHFINE, "ibn_tachfine"),
    (EL_OULFA, "el_oulfa"),
    (HASSAN_II, "hassan_ii"),
    (AL_QODS, "al_qods"),
    (AL_AMAL, "al_amal"),
    (AL_MANAR, "al_manar"),
    (VILLE_HAUTE, "ville_haute"),
    (DOHA, "doha"),
    (MAAMORA, "maamora"),
    (SAKNIA, "saknia")
)

APPARTEMENT = "appartement"
VILLA = "villa"
STUDIO = "studio"
CHAMBRE = "chambre"
BUREAU = "bureau"

CATEGORIES_CHOICES = (
    (APPARTEMENT, "appartement"),
    (VILLA, "villa"),
    (STUDIO, "studio"),
    (CHAMBRE, "chambre"),
    (BUREAU, "bureau")
)

NOUVEAU = 'nouveau'
BONETAT = 'bon etat'
ETAT_CHOICES = (
    (NOUVEAU,'nouveau'),
    (BONETAT,'bon état')
)
