import vobject
import base64

def b64_image(filename):
    with open(filename, 'rb') as f:
        b64 = base64.b64encode(f.read())
        return b64.decode('utf-8')

vCard = vobject.vCard()
vCard.add('N').value = vobject.vcard.Name(family='Food', given='Cheers')
vCard.add('FN').value = "Cheers"
vCard.add('BDAY').value = '2021'

vCard.add('EMAIL')
vCard.email.value = 'cheersfoodapp@gmail.com'
vCard.email.type_param = 'Email'

o = vCard.add('PHOTO;ENCODING=b;TYPE=image/png')
o.value = b64_image('cheers_logo.PNG')

# vCard.add('ADR')
# vCard.adr.value = vobject.vcard.Address('742 Evergreen Terrace','Springfield','OR','58008','U.S.A.')
# vCard.adr.type_param = 'HOME'

vCard.add('TEL')
vCard.tel.value = '+1-205-852-2477'
vCard.tel.type_param = 'HOME'

with open('CheersFood.vcf', 'w') as writer:
        writer.write(vCard.serialize())