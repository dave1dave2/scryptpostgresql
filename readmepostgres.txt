Scrypt de base de données avec postgresql

le scrypt sera effectuer sous un environnement:
Debian 10.6
une base de données postgresql 11.9 

Installer postgresql 

apt-update
apt install postgresql postgresql-contrib
systemctl start postgres

créer un utilisateur pour la base de fonner

l'option d permet d'atrribuer un role à la bae de données et P exiger un mot de passe 
createuser -s -d -P Dave

crée une base de donner et on lu attribut l'utilisateur de cette basse

createdb -O Dave dbd

il faut modifier les paramètres suivant :

log_min_duration_statement: limiter le volume des relevés enregistrés.
log_disconnections: enregistre les déconnexions et le temps passé sur la base de donnée
log_min_messages: les journaux avec un avertissement de gravité (ERREUR, JOURNAL, FATAL, PANIQUE)
log_filename : modèle de nom de fichier journal
log_directory : répertoire où les fichiers journaux sont écrits
log_connections: enregistre les connections à la base sur une seule ligne 
log_min_error_statement: journalisation des instructions associées aux erreurs


configuration du scrypt de connexion à la base de données 
Voir le fichier pysql.py