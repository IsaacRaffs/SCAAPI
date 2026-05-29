from django.db import models


ESPECIE_CHOICE = (
    ("CACHORRO", "Cachorro"),
    ("GATO", "Gato"),
)

SEXO_CHOICE = (
    ("MACHO", "Macho"),
    ("FEMEA", "Fêmea"),
)

RACA_CHOICE = (
    ("SRD", "SRD (Sem Raça Definida)"),
    ("POODLE", "Poodle"),
    ("LABRADOR", "Labrador"),
    ("BULLDOG", "Bulldog"),
    ("SHIH-TZU", "Shih-Tzu"),
    ("SIAMES", "Siamês"),
    ("PERSA", "Persa"),
    ("MAINE-COON", "Maine Coon"),
    ("OUTRO", "Outro"),
)

PELAGEM_CHOICE = (
    ("CURTA", "Pelagem Curta"),
    ("MEDIA", "Pelagem Média"),
    ("LONGA", "Pelagem Longa"),
    ("AUSENTE", "Sem Pelagem"),
)

STATUS_CHOICE = (
    ("VIVO", "Vivo"),
    ("MORTO", "Morto"),
)

ESTERILIZACAO_CHOICE = (
    ("SIM", "Sim"),
    ("NAO", "Não"),
)


class Animal(models.Model):
    especie = models.CharField('espécie', max_length=20, choices=ESPECIE_CHOICE, default="CACHORRO")
    nome = models.CharField('nome', max_length=80)
    sexo = models.CharField('sexo', max_length=20, choices=SEXO_CHOICE, default="MACHO")
    esterilizacao = models.CharField('esterilização', max_length=20, choices=ESTERILIZACAO_CHOICE, default="NAO")
    nascimento = models.DateField('data de nascimento', null=True, blank=True)
    raca = models.CharField('raça', max_length=80, choices=RACA_CHOICE, default="SRD")
    pelagem = models.CharField('pelagem', max_length=20, choices=PELAGEM_CHOICE, default="CURTA")
    status = models.CharField('status', max_length=20, choices=STATUS_CHOICE, default="VIVO")

    def __str__(self):
        return f"{self.nome} ({self.tipo})"


class Adotante(models.Model):
    nome = models.CharField('nome', max_length=120)
    email = models.EmailField('email', blank=True)
    telefone = models.CharField('telefone', max_length=30, blank=True)
    endereco = models.TextField('endereço', blank=True)
    criado_em = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Adotante'
        verbose_name_plural = 'Adotantes'

    def __str__(self):
        return self.nome
