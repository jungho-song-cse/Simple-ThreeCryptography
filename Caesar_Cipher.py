message = 'GURTERNGRFGTYBELVAYVIVATYVRFABGVAARIRESNYYVATOHGVAEVFVATRIRELGVZRJRSNYY.ARYFBAZNAQRYN.GURJNLGBTRGFGNEGRQVFGBDHVGGNYXVATNAQORTVAQBVAT.JNYGQVFARL.LBHEGVZRVFYVZVGRQFBQBABGJNFGRVGYVIVATFBZRBARRYFRFYVSR.QBABGORGENCCRQOLQBTZN.JUVPUVFYVIVATJVGUGURERFHYGFBSBGURECRBCYRFGUVAXVAT.FGRIRWBOF.VSYVSRJRERCERQVPGNOYRVGJBHYQPRNFRGBORYVSRNAQORJVGUBHGSYNIBE.RYRNABEEBBFRIRYG.VSLBHYBBXNGJUNGLBHUNIRVAYVSRLBHJVYYNYJNLFUNIRZBER.VSLBHYBBXNGJUNGLBHQBABGUNIRVAYVSRLBHJVYYYARIREUNIRRABHTU.BCENUJVASERL.VSLBHFRGLBHETBNYFEVQVPHYBHFYLUVTUNAQVGVFNSNVYHERLBHJVYYSNVYNOBIRRIRELBARRYFRFFHPPRFF.WNZRFPNZREBA.YVSRVFJUNGUNCCRAFJURALBHNEROHFLZNXVATBGURECYNAF.WBUAYRAABA.FCERNQYBIRRIRELJURERLBHTB.YRGABBARRIREPBZRGBLBHJVGUBHGYRNIVATUNCCVRE.ZBGUREGRERFN.JURALBHERNPUGURRAQBSLBHEEBCRGVRNXABGVAVGNAQUNATBA.SENAXYVAQ.EBBFRIRYG.NYJNLFERZRZOREGUNGLBHNERNOFBYHGRYLHAVDHR.WHFGYVXRRIRELBARRYFR.ZNETNERGZRNQ.QBABGWHQTRRNPUQNLOLGURUNEIRFGLBHERNCOHGOLGURFRRQFGUNGLBHCYNAG.EBOREGYBHVFFGRIRAFBA.GURSHGHERORYBATFGBGUBFRJUBORYVRIRVAGURORNHGLBSGURVEQERNZF.RYRNABEEBBFRIRYG.GRYYZRNAQVSBETRG.GRNPUZRNAQVERZRZORE.VAIBYIRZRNAQVYRNEA.ORAWNZVASENAXYVA.GURORFGNAQZBFGORNHGVSHYGUVATFVAGURJBEYQPNAABGORFRRABERIRAGBHPURQGURLZHFGORSRYGJVGUGURURNEG.URYRAXRYYRE.VGVFQHEVATBHEQNEXRFGZBZRAGFGUNGJRZHFGSBPHFGBFRRGURYVTUG.NEVFGBGYR.JUBRIREVFUNCCLJVYYZNXRBGUREFUNCCLGBB.NAARSENAX.QBABGTBJURERGURCNGUZNLYRNQTBVAFGRNQJURERGURERVFABCNGUNAQYRNIRNGENVY.ENYCUJNYQBRZREFBA.'
ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#find coincidences by below code
for shift in range(len(message)):
    count = 0
    for i in range(len(message)):
        if(i+1+shift >=len(message)):
            break
        if(message[i]==message[i+1+shift]):
            count += 1
    print(count)
#we found out its key length is 1 by coincidences, so it may be caesar cipher

#break caesar cipher by brute force!
for key in range(len(ALPHABETS)):
   decryptedMessage = ""
   count = 0
   for letter in message:
      if letter in ALPHABETS:
         num = ALPHABETS.find(letter)
         num -= key
         num %= len(ALPHABETS)
         decryptedMessage = decryptedMessage + ALPHABETS[num]
      else:
         decryptedMessage = decryptedMessage + letter
   print('key is #%s, decrypted message: %s' %(ALPHABETS[key], decryptedMessage))
#we founded key is N(13)

#print out decrypted message with key information!!
decryptedMessage = ""
for letter in message:
   key = 13
   num = ALPHABETS.find(letter)
   num += key
   num %= len(ALPHABETS)
   if letter in ALPHABETS:
      decryptedMessage = decryptedMessage + ALPHABETS[num]
   else:
      decryptedMessage = decryptedMessage + letter

print('\nkey is #N, decrypted message: %s' %(decryptedMessage))