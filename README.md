# Integriertes Forschungsprojekt
Dies sind alle relevanten Dokumente die beim IFP zum Thema *Analyse der Datenstrukturen mit dem Ziel der Erzeugung von Eingabedaten für das Graph Network-based Simulator Framework*
entstanden sind.
## Verzeichnis
#### datasets
Hier werden alle Datensätze abgespeichert. Für den Anfang ist hier nur WaterdropSample enthalten.

#### learning_to_simulate
Hier ist der Code für das GNS Framework abgelegt. Es enthält die selbsterstellte Datei *render_rollout_and_save_to_avi.py*. 
Mit dieser können die animierten Plots entweder als .avi oder als .gif abgespeichert werden.

#### create_avi.py
Hiermit können alle .pkl-Files in einem Ordner animiert und abgespeichert werden. Das Format in dem die Animationen gespeichert werden, 
werden im *create_Dataset.ipnb*-File festgelegt.  
**Hinweis:** Es ist wichtig darauf zu achten, dass der Ordner nur .pfl-Files enthält, sonst kommt es zu einer Fehlermeldung!

#### create_Dataset.ipynb
Mit diesem Code kann ein eigener Datensatz erzeugt werden, bestehend entweder nur aus Wasser oder zusätlich aus sliden Partikeln.
Dieser Code wurde als Funktion auch in das *train.py* Dokument eingefügt um den vorhandenen Datensatz mit dem selbsterzeugten zu überschreiben.

#### IFP_Paper_Rossnagel_Daniel.pdf
Dies ist das erstellte Paper zum IFP.

#### read_tfrecord.ipynb
Mit diesem Notebook kann der Inhalt der Datensätze gelesen werden.
