# http://www.roguebasin.com/index.php?title=Markov_chains_name_generator_in_Python

import random, sys

# from http://www.geocities.com/anvrill/names/cc_goth.html
NAMES = ['afrit', 'alfar', 'amphisbaena', 'ananta', 'anka', 'anthropophagus', 'ant-lion', 'arimaspians', 'aspidoceleon', 'ass centaur', 'astomi', 'barnacle-goose ', 'basilisk', 'bean sidh', 'blemiyeh', 'brownie', 'bucentaur', 'caladrius', 'callitrice', 'canocephalus', 'capricorn', 'caristae', 'catoblepas', 'cecrops', 'centaur', 'cerberus', 'charadrius', 'cheiron', 'chemosit', 'chi lin', 'chimera', 'cinamon bird', 'criosphinx', 'crocotta', 'cockatrice', 'cyclops', 'cynocephali ', 'demon', 'dhampir', 'djinni', 'djinniyeh', 'domovoi', 'dragon, western', 'dragonhorse', 'dryad', 'dwarf', 'echeneis', 'echidna', 'elf', 'ekimmu', 'ercinee', 'ettin', 'faerie', 'faun', 'fenris wolf', 'frost-giant', 'fox-maiden', 'gargoyle', 'garm', 'garuda', 'ghul', 'giant', 'giant ants', 'glaistig', 'glaucus', 'golem', 'gnome', 'griffin', 'grotesque', 'gryllus', 'hags', 'hamadryad', 'harpy', 'hea-bani', 'hengeyokai ', 'hercynian stag', 'hieracosphinx', 'hippocampus', 'hippogriff', 'hippopodes', 'hsien', 'hydrus', 'hydra', 'hydrippus', 'ichthyocentaur', 'incubus', 'jack-in-the-green', 'jormungandr', 'kaliya', 'karkadann', 'kelpie', 'ki-lin', 'ki-rin', 'kobold', 'kraken', 'lamassu', 'lamia', 'leshy', 'leprechaun', 'leucrotta', 'leviathan ', 'lillith', 'lilit    ', 'lindworm', 'lung', 'magyr', 'malebranche demon', 'manticore', 'medusa', 'melusinae', 'mermaid', 'mermicolion', 'midgard serpent', 'the', 'minotaur ', 'monocerus', 'monkfish', 'monopod', 'naga', 'nag-kanya', 'naiad ', 'nasir', 'nemean lion', 'ness monster', 'niluus', 'nixie', 'nuckelavee', 'obour', 'odontotyrannos', 'ogre ', 'ogre', 'onocentaur', 'pan', 'panther of the fresh breath', 'pastinaca', 'pazuzu', 'pegasies', 'pegasus', 'pennaglan', 'perryton', 'phoenix', 'pholos', 'piast', 'pirobolus', 'pooka', 'rakasha', 'roc', 'salamander', 'satyr ', 'sciopod', 'scorpion-men', 'sea-bishop', 'sea-serpent', 'senmurv', 'serra', 'shang yang', 'silenus', 'simurgh', 'sin-you', 'siren', 'skoffin', 'sleipnir', 'sphinx', 'stymphalian birds', 'succubus', 'sun-lizard', 'tarasque', 'tengu', 'tien kou', 'typhon', 'tragelaphs', 'triton', 'troll', 'turtle-asp whale', 'unicorn', 'urisk', 'urobus worm', 'vampire ', 'vegetable lamb', 'vrykolakas', 'werewolf', 'wild-man', 'will-of-the-wisp', 'woose', 'woot', 'wyvern', 'yale', 'yllerion']

###############################################################################
# Markov Name model
# A random name generator, by Peter Corbett
# http://www.pick.ucam.org/~ptc24/mchain.html
# This script is hereby entered into the public domain
###############################################################################
class Mdict:
    def __init__(self):
        self.d = {}
    def __getitem__(self, key):
        if key in self.d:
            return self.d[key]
        else:
            raise KeyError(key)
    def add_key(self, prefix, suffix):
        if prefix in self.d:
            self.d[prefix].append(suffix)
        else:
            self.d[prefix] = [suffix]
    def get_suffix(self,prefix):
        l = self[prefix]
        return random.choice(l)  

class GenName:
    """
    A name from a Markov chain
    """
    def __init__(self, chainlen = 2):
        """
        Building the dictionary
        """
        if chainlen > 10 or chainlen < 1:
            print("Chain length must be between 1 and 10, inclusive")
            sys.exit(0)
    
        self.mcd = Mdict()
        oldnames = []
        self.chainlen = chainlen
    
        for l in NAMES:
            l = l.strip()
            oldnames.append(l)
            s = " " * chainlen + l
            for n in range(0,len(l)):
                self.mcd.add_key(s[n:n+chainlen], s[n+chainlen])
            self.mcd.add_key(s[len(l):len(l)+chainlen], "\n")
    
    def New(self):
        """
        New name from the Markov chain
        """
        prefix = " " * self.chainlen
        name = ""
        suffix = ""
        while True:
            suffix = self.mcd.get_suffix(prefix)
            if suffix == "\n" or len(name) > 9:
                break
            else:
                name = name + suffix
                prefix = prefix[1:] + suffix
        if name.lower() in NAMES:
            GenName().New()
        return name.capitalize()  

#for i in range(100):
    #print(GenName().New())

#def RandomNameGenerator():
    #Prefixes = ["", "bel", "nar", "natr", "ev", "sp", "st", "od", "han", "ryus"]
    #Stems = ["adu", "aes", "ani", "apo", "imac", "educ", "equ", "extr", "gius", "hann", "equi", "amora", "hum", "iac", "ill", "inep", "iuv", "obe", "ocu", "orb", "iu", "en", "id", "il", "on", "et"]
    #Suffixes = ["", "us", "ix", "ox", "ith", "ath", "um", "ator", "or", "axia", "imus", "ais", "itur", "orex", "o", "y", "anus", "inus", "le", "r", "is", "elus", "lo", "ma"]
    #Name = "%s%s%s" % (random.choice(Prefixes), random.choice(Stems), random.choice(Suffixes))
    #Name = Name.capitalize()
    #return Name