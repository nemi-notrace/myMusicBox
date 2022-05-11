# Musikbox TN 46SK

Die Musikbox für TN46SK ist nicht als Phoniebox konzipiert da die gewünschte Bedienung nicht umsetzbar ist mit dem Konzept der Phoniebox.

Es wurde ein rudimentäres Skript geschrieben und als Service eingebunden welches die Buttons auf Ordner (0,1,2) mapped welche bei Aktivierung im VLC-Player als Playlist gestartet werden. Die Kontrolle der Lautstärke erfolgt über die System Lautstärke mittels ALSA.

Die Aktivierung der „Play-Buttons“ wird mit geloggt über den Service „player-log.service“ dieser lässt sich über ```sudo systemctl disable player-log.service``` deaktivieren oder durch das löschen des log.py Scripts.

Die gewünschte Musik muss in den Ordnern 0-2 abgelegt werden und darf keine Unterordner sowie Sonderzeichen und Umlaute in der Benennung beinhalten.

Um zugriff auf die Daten zu erhalten bzw. die Musik einzurichten kann der Pi mittels Tastatur und Monitor bedient werden, über  das anschließen eines LAN-Kabels via SSH oder durch das entnehmen der Speicherkarte und auslesen an einem anderen Gerät, wichtig hierbei ist das dieses mit dem Dateisystemen EXT2 und EXT4 umgehen können muss (Linux).

Das Passwort ist wie gehabt teilhabe21