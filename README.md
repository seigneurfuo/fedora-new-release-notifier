# Fedora New Release Notifier

Un petit script qui affiche une notification (par défaut toutes les heures) quand une nouvelle version de Fedora est disponible. Utile sur les spins sur lesquels Gnome Software n'est pas installé.

![](docs/imgs/notification.png)

L'adresse URL pour vérifier la sortie de nouvelles (https://getfedora.org/releases.json) version à été trouvé ici: https://discussion.fedoraproject.org/t/is-it-possible-to-verify-that-a-major-release-is-already-released/78713

## Packaging
```sh
fedpkg --release f$(rpm -E %fedora) local
# fedpkg --release f37 mockbuild --no-clean-all
```
