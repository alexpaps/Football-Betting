
def game():
   from math import fabs,sqrt
   
   hw=float(input("Nikes gipedouxou :"))
   hd=float(input("isopalies gipedouxou :"))
   hl=float(input("Ittes gipedouxou :"))
           
   aw=float(input("Nikes filoksenumenu :"))
   ad=float(input("isopalies filoksenumenu :")) 
   al=float(input("ittes filoksenumenu :"))
   
   m1 = hw + hd + hl
   m2 = aw + ad + al

   #Υπολογισμός Συχνότητας Νίκης/Ισοπαλίας/Ήττας
   SixnotitaNikisHome = hw / m1
   SixnotitaIsopaliasHome = hd / m1
   SixnotitaIttasHome = hl / m1
   SixnotitaNikisAway = aw / m2
   SixnotitaIsopaliasAway = ad / m2
   SixnotitaIttasAway = al / m2

   #Μέσος όρος
   MesosOrosHome = (3*hw + 1*hd + 0*hl)/m1 #Βαθμοί που κερδίζεις ανάλογα το αποτέλεσμα
   MesosOrosAway = (3*aw + 1*ad + 0*al)/m2

   #Διακύμανση ή Διασπορά
   s2home = (hw * (3 - MesosOrosHome)**2 + hw * (1 - MesosOrosHome)**2 + hw * MesosOrosHome**2)/m1
   s2away = (aw * (3 - MesosOrosAway)**2 + aw * (1 - MesosOrosAway)**2 + aw * MesosOrosAway**2)/m2 
 
   #Τυπική Απόλιση - Πόσο σταθερή είναι η ομάδα
   shome = sqrt(s2home)
   saway = sqrt(s2away)
    
   #Μετατρέπω τα σε ποσοστά
   hw = (hw*100)/(m1)
   hd = (hd*100)/(m1)
   hl = (hl*100)/(m1)

   aw = (aw*100)/(m2)
   ad = (ad*100)/(m2)
   al = (al*100)/(m2)

   #Υπολογισμός των Αρχικών Ποσοστών Σύμφωνα Με την Αγωνιστική Κατάσταση των Ομάδων
   i=1
   while i < 6:
      Apotg =input("Pente teleftaia match gipedouxou (w for win/d for draw/l for loose):")
      last_op = int(input("Ti vathmologiki thesi eixe o antipalos sou? : "))

      if Apotg != 'w' and Apotg != 'd' and Apotg != 'l' :
          continue
      if Apotg=='w':
         hw=hw + (21-last_op)/2
         hl=hl-last_op/2
         hd=hd-((21-last_op)/2-last_op/2)
         i=i+1          
         
      elif(Apotg=='l'):
         hw=hw-last_op/2
         hl=hl+(21-last_op)/2
         hd=hd-((21-last_op)/2-last_op/2)
         i=i+1
         
      elif(Apotg=='d'):
        hw=(hw-2.5)
        hl=hl-2.5
        hd=hd + 5
        i=i+1

   i=1
   while i < 6 :

     Apotf = input("Pente teleftaia match filoksenoumenou (w for win/d for draw/l for loose):")
     last_op = int(input("Ti vathmologiki thesi eixe o antipalos sou? : "))

     if Apotf != 'w' and Apotf != 'd' and Apotf != 'l' :
      continue
             
     if(Apotf=='w'):
         aw=aw+(21-last_op)/2
         al=al-last_op/2
         ad=ad-((21-last_op)/2-last_op/2)
         i=i+1
         
     elif(Apotf=='l'):
         aw=aw-last_op/2
         al=al+(21-last_op)/2
         ad=ad-((21-last_op)/2-last_op/2)
         i=i+1
         
     elif(Apotf=='d'):
       aw=(aw-2.5)
       al=al-2.5
       ad=ad+5
       i=i+1

   i=1
   while i < 4:

     Apot3 = input("tria teleftaia metaksi tous match(h for HomeWin/d for draw/a for AwayWin) :")

     if Apot3 != 'h' and Apot3 != 'd' and Apot3 != 'a' :
       continue
                 
     if(Apot3=='h'):
       aw=aw-2.5
       hw=hw+5
       al=al+5
       hl=hl-2.5
       ad=ad-2.5
       hd=hd-2.5
       i=i+1
         
     elif(Apot3=='a'):
       aw=aw+5
       hw=hw-2.5
       al=al-2.5
       hl=hl+5
       ad=ad-2.5
       hd=hd-2.5
       i=i+1
         
     elif(Apot3=='d'):
       aw=aw-2.5
       hw=hw-2.5
       al=al-2.5
       hl=hl-2.5
       ad=ad+5
       hd=hd+5
       i=i+1 

   ask1 = input("Write yes an o gipedouxos exei dinati edra :")
   if ask1 == "yes":
       aw=aw-10
       hw=hw+5
       al=al+5
       hl=hl-10
       ad=ad+5
       hd=hd+5

   # Μέσο Όρο Πιθανοτήτων
   MOP1 = (hw + al)/2
   MOPd = (hd + ad)/2
   MOP2 = (hl + aw)/2
   # Φαβορί
   F1 = ((hw + al)**2) / (((hw + al)**2) + ((hd + ad)**2) + ((hl + aw)**2))
   Fd = ((hd + ad)**2) / (((hw + al)**2) + ((hd + ad)**2) + ((hl + aw)**2))
   F2 = ((hl + aw)**2) / (((hw + al)**2) + ((hd + ad)**2) + ((hl + aw)**2))
   # Συντελεστής Αναλογίας Φαβορί
   SAF1 = fabs(F1 - (Fd+F2))
   SAFd = fabs(Fd - (F1-F2))
   SAF2 = fabs(F2 - (Fd+F1))
   # Κατανομή
   Kat1 = (F1*SAF1)+(MOP1*(100-SAF1))
   Katd = (Fd*SAFd)+(MOPd*(100-SAFd))
   Kat2 = (F2*SAF2)+(MOP2*(100-SAF2))
   #Τελική κατανομή πιθανοτήτων
   TelKat1 = Kat1 *100/ ( Kat1+Katd+Kat2)
   TelKatd = Katd *100/ ( Kat1+Katd+Kat2)
   TelKat2 = Kat2 *100/ ( Kat1+Katd+Kat2)
   #Υπολογισμός Αποδόσεων
   Apodosi1 = fabs(100 / TelKat1)
   Apodosid = fabs(100 / TelKatd)
   Apodosi2 = fabs(100 / TelKat2)

   print("\nWinHome :{}\nDraw :{}\nWinAway :{}\n".format((TelKat1+33.33)/2,(TelKatd+33.33)/2,(TelKat2+33.33)/2))
   print("ApodosiAssou :{}\nApodosiIsopoalias :{}\nApodosiDiplou :{} ".format(Apodosi1,Apodosid,Apodosi2))
   print("SixnotitaNikisHome :{}\tSixnotitaIsopaliasHome :{}\tSixnotitaIttasHome: {}".format(SixnotitaNikisHome*100,SixnotitaIsopaliasHome*100,SixnotitaIttasHome*100))
   print("SixnotitaNikisAway :{}\tSixnotitaIsopaliasHome :{}\tSixnotitaIttasAway :{} ".format(SixnotitaNikisAway*100,SixnotitaIsopaliasAway*100,SixnotitaIttasAway*100))
   print("MesosOrosHome :{}\tMesosOrosAway :{}".format(MesosOrosHome,MesosOrosAway))
   print("ApoklisiHome :{}\tApoklisiAway :{}".format(shome,saway))

