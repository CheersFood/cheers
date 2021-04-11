import vobject
import base64

def b64_image(filename):
    with open(filename, 'rb') as f:
        b64 = base64.b64encode(f.read())
        return b64.decode('utf-8')

vCard = vobject.vCard()
vCard.add('N').value = vobject.vcard.Name(family='', given='Cheers Insiders')
vCard.add('FN').value = "Cheers"
vCard.add('BDAY').value = '2021-04-13'

vCard.add('URL')
vCard.url.value = 'https://www.textcheers.com'
vCard.url.type_param = 'URL'

vCard.add('Email')
vCard.email.value = 'info@textcheers.com'
vCard.email.type_param = 'Email'

vCard.add('ADR')
vCard.adr.value = vobject.vcard.Address('Birmingham','AL')
vCard.adr.type_param = 'HOME'

vCard.add('TEL')
vCard.tel.value = '+1-205-225-6976'
vCard.tel.type_param = 'Phone'

o = vCard.add('PHOTO;ENCODING=b;TYPE=image/png')
o.value = b64_image('CheersInsiders.png')

with open('CheersInsiders.vcf', 'w') as writer:
        writer.write(vCard.serialize())