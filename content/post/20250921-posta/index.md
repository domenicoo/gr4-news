---
title: Situazione mail UPDATE
description: 
slug: situazione-mail
date: 2025-10-09 00:00:00+0000
categories:
    - Local
tags:
    - INFN
    - italiano
    - local life
weight: 1       # You can add weight to some posts to override the default sorting (date descending)
---

# ‼️  Migrazione a server di posta esterno (9 ottobre)

> Domani mattina (venerdì 10 ottobre) tutti gli indirizzi di posta @to.infn.it saranno migrati su un sistema di emergenza al CNAF, molto simile a quello che sarà poi definitivo.
> 
> In un primo momento sarà possibile accedere solo attraverso il servizio webmail collegandosi a
> 
> https://mail-to.infn.it
> 
> e autenticandosi con le credenziali AAI (le stesse del portale INFN). Successivamente comunicheremo le istruzioni per configurare i client (mail.app, thunderbird eccetera).
> 
> Ci sarà un intervallo di poche ore in cui l’informazione si propaga; in quel periodo alcuni messaggi continueranno ad arrivare al nostro server (e conseguentemente a essere forwardati) mentre altri arriveranno direttamente al nuovo sistema; trascorso il periodo tutta la posta arriverà al nuovo server e i forward non saranno più attivi.
> 
> Per quanto riguarda la posta sul vecchio server, stiamo ancora lavorando al ripristino dello storage e la renderemo accessibile in sola lettura appena possibile.
> 
> Fare riferimento a central-support@to.infn.it per qualunque problema si incontri (central-support ha ricevuto email anche durante tutta la crsisi, è sempre il riferimento per richieste di supporto)

# ℹ️ AGGIORNAMENTO (8 ottobre)

> Allora, abbiamo fatto passi avanti nel debug del sistema, ma la soluzione richiede probabilmente la sostituzione di altri dischi (già ordinati, ma ancora una settimana) e non è detto che basti  
> Quindi abbiamo deciso di procedere con la soluzione di emergenza al CNAF
> domani o al più tardi venerdì mattina migriamo  
> Domani in giornata arrivano istruzioni dettagliate su come procedere  
> Caveat principale: ci sono delle incongruenze tra la lista degli account locali e la lista degli account in AAI
> l’idea è di procedere al più presto in modo da mettere la maggior parte delle persone in grado di lavorare, e sistemare gli altri via via che troviamo i problemi


# ℹ️ AGGIORNAMENTO (8 ottobre)


Purtroppo non ho le buone notizie che mi auguravo.
I dischi sono arrivati, sono stati inseriti ma i problemi rimangono.

Nel frattempo, ho messo su una paginetta per avere sotto controllo la situazione. La trovate qui:

https://domenicoo.github.io/gr4-news/is-it-up

(non è automatico che i server accettino il login anche se sono in funzione).


# ℹ️ AGGIORNAMENTO (3 ottobre)

> È (quasi) tutto pronto per il passaggio al sistema di emergenza. Lunedì arrivano i dischi, gli diamo il tempo di ribilanciare il RAID e martedì mattina se non riparte provvediamo (non credo martedì stesso, ma forse mercoledì).  
> Se il nostro sistema riparte non ha senso passare al sistema di emergenza, aspettiamo quello definitivo nel giro di qualche settimana.  
> Seguiranno istruzioni dettagliate

# TEAMS

L'INFN ha una licenza campus di microsoft teams.
Come detto in CdS, è in questo momento il modo migliore per comunicare con l'amministrazione.

Trovate tutte le istruzioni alla pagina
https://web.infn.it/windows/index.php/istruzioni/24-office-365

In breve: ci si collega a http://www.infn.it/richiesta-o365; si viene autenticati con AAI; se non si è mai fatto richiesta di abilitazione si visualizza un bottone, diversamente l'informazione che si è già stati abilitati.

# ℹ️ AGGIORNAMENTO (2 ottobre)

> - ⁠ufficialmente i dischi arrivano lunedì. Se il problema è davvero quello (ma non sono troppo ottimista) il problema si risolve subito
> - ⁠migrazione al sistema di posta di emergenza potrebbe avvenire  già nel corso della prossima settimana
> - sistema di posta definitivo ai servizi nazionali ottimisticamente tre settimane

Nel frattempo,

- l'accesso alla VPN è chiuso per qualche giorno
- l'accesso alle macchine di login è sospeso. Ci auguriamo che sia ripristinato velocemente.

# Come inoltrare la mail ad un altro indirizzo

> Purtroppo il guasto al sistema di posta persiste e non possiamo abilitare i client di posta (pine, imap, webmail).
> 
> In attesa di risolvere il problema, è possibile configurare un forward a una casella diversa nel seguente modo (sostituite “username” con il vostro username locale e [mioindirizzo@serverdiposta.dacambiare] con l’indirizzo che volete usare):
> ```
> ssh -l username artaban.to.infn.it
> 
> cd
> cp -a .forward .forward-20250925
> echo "\\username, mioindirizzo@serverdiposta.dacambiare" > .forward
> ```
> e controllate il contenuto del file `.forward` con il seguente comando:
> ```
> cat .forward
> ```
> Che deve restituire una riga simile a quella qui sotto (che ovviamente deve essere il vostro; importante il backslah iniziale per mantenere una copia del mail anche nella inbox locale):
> ```
> \bagnasco, stefano.bagnasco@cern.ch
> ```


# English version: how to forward your mail to another address

> Unfortunately, the mail system malfunction persists and we cannot enable the mail clients (pine, imap, webmail).
> 
> While waiting to solve the problem, it is possible to configure a forward to a different mailbox as follows (replace “username” with your local username and [mioindirizzo@serverdiposta.dacambiare] with the address you want to use):
> 
> ```
> ssh -l username artaban.to.infn.it
> 
> cd
> cp -a .forward .forward-20250925
> echo "\\username, mioindirizzo@serverdiposta.dacambiare" > .forward
> ```
> 
> Then check the contents of the `.forward` file with the following command:
> 
> ```
> cat .forward
> ```
> 
> It should return a line similar to the one below (which of course must be yours; the initial backslash is important in order to keep a copy of the mail also in the local inbox):
> 
> ```
> \bagnasco, stefano.bagnasco@cern.ch
> ```
> 



# ℹ️ AGGIORNAMENTO (25 settembre)

> Non ho buone notizie
> Non risuciamo ad avviare stabilmente il servizio IMAP, stiamo cercando di capire la causa
> E per non rischiare di schiantare tutto per ora teniamo disabilitato anche pine
> Per i ricercatori, tra poco apriamo una public login per poterlo mettere in autonomia
 
# ℹ️ AGGIORNAMENTO (25 settembre)

> la ricostruzione è finita stanotte, ma abbiamo ancora problemi che stiamo cercando di capire
> Se entro stasera non risolviamo andiamo nella direzione del forward
> 
# ℹ️ AGGIORNAMENTO (24 settembre)

> Il disco è arrivato e installato, sta ricostruendo la ridondanza. Ci vorranno alcune ore: a questo punto d’accordo con gli altri aspetterei domani mattina per fare ulteriori passi
 
# ℹ️ AGGIORNAMENTO (24 settembre)

> stiamo ancora aspettando il disco (che probabilmente non sarà risolutivo, ma evita  i rischi di perdita di dati), ho sollecitato ma mi dicono che anche loro stanno aspettando il corriere

# ℹ️ AGGIORNAMENTO (22 settembre)

> se con il disco rimpiazzato il sistema sta in piedi e tutto torna come prima, bene
> altrimenti il piano è vedere se si riesce a tenere il sistema in piendi senza IMAP (e senza pine); la posta la gestiremmo attraverso dei forward verso altre caselle (CERN, UNITO, gmail,…) che possimo gestire noi per l’amministrazione, mentre i ricercatori dovrebbero essere in grado di far da soli (con opportune istruzioni)
 
# ℹ️ AGGIORNAMENTO (21 settembre)

> Purtroppo la situazione è peggiorata, è di nuovo crashato il cluster e non si riesce a farlo ripartire. Domani mattina vien un tecnico per cercare di capire se il problema, come sembra, è lo storage.
 
# Messaggio originale:

> Cari coordinatori,
> 
> Se leggete questo mail ho un vostro indirizzo alternativo (non sono sicuro di quello di Domenico).
> 
> Abbiamo un complicato problema hardware, ci abbiamo messo un po’ a capire la situazione (dettagli su richiesta) e ora sto aspettando che mi chiamino dall’assistenza per avere un’idea dei tempi di ripristino. 
> 
> Intanto in realtà il sistema di posta funziona, le mail arrivano e non si perdono, possono essere spedite; solo non possiamo “accendere” IMAP o si schianta tutto, quindi non è possible usare un normale client di posta per leggerle.
> 
> Per chi si ricorda come si fa, pine sulle macchine di public login funziona; un’alternativa, in deroga alle regole, è configurare un forward su un indirizzo diverso (unito, cern, gmail,…), da togliere però finita l’emergenza perché genera potenzialmente altri problemi.
> 
> Mi spiace per il grave disservizio, il sistema ha ovviamente tutte le ridondanze del caso (e infatti non abbiamo perso dati) ma shit happens… vi tengo informati sugli sviluppi.
> 
> Grazie,
> Stefano
> 
