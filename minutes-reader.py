# -*- coding: utf-8 -*-
# Chase,
#
# This gets the text from Columbia City Council minutes and write the contents to a single text file
# Then, performs a search for key terms such as race, racism, discrimiantion, campus
# PdfToText doesn't seem to work on Windows, so I used a library called
# PDFMiner, which apparently doesn't work unless you import each tool separately.
# Cheers,
#
# Will Schmitt | 12/02/2015
#
# Start script:
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from cStringIO import StringIO
import re

printer = StringIO()
manager = PDFResourceManager()
laparams = LAParams()

a = file('minutes/cm15_aug17.pdf', 'rb')
adate = 'CCC Meeting Aug. 17:\n\n'
aug17 = PDFParser(a)
aug17doc = PDFDocument(aug17)
aug17object = TextConverter(manager, printer, laparams=laparams)
aug17subject = PDFPageInterpreter(manager, aug17object)

for page in PDFPage.get_pages(a):
	aug17subject.process_page(page)
	atext = printer.getvalue()

#the adate, bdate, etc. variables are appended to break up the results by meeting. 

b = file('minutes/cm15_sept8.pdf', 'rb')
bdate = 'CCC Meeting Sept. 8:\n\n'
sept8 = PDFParser(b)
sept8doc = PDFDocument(aug17)
sept8object = TextConverter(manager, printer, laparams=laparams)
sept8subject = PDFPageInterpreter(manager, sept8object)

for page in PDFPage.get_pages(b):
	sept8subject.process_page(page)
	btext = printer.getvalue()	

c = file('minutes/cm15_sept21.pdf', 'rb')
cdate = 'CCC Meeting Sept. 21:\n\n'
sept21 = PDFParser(c)
sept21doc = PDFDocument(sept21)
sept21object = TextConverter(manager, printer, laparams=laparams)
sept21subject = PDFPageInterpreter(manager, sept21object)

for page in PDFPage.get_pages(c):
	sept21subject.process_page(page)
	ctext = printer.getvalue()

d = file('minutes/cm15_oct5.pdf', 'rb')
ddate = 'CCC Meeting Oct. 5:\n\n'
oct5 = PDFParser(d)
oct5doc = PDFDocument(oct5)
oct5object = TextConverter(manager, printer, laparams=laparams)
oct5subject = PDFPageInterpreter(manager, oct5object)

for page in PDFPage.get_pages(d):
	oct5subject.process_page(page)
	dtext = printer.getvalue()

e = file('minutes/cm15_oct19.pdf', 'rb')
edate = 'CCC Meeting Oct. 19:\n\n'
oct19 = PDFParser(e)
oct19doc = PDFDocument(oct19)
oct19object = TextConverter(manager, printer, laparams=laparams)
oct19subject = PDFPageInterpreter(manager, oct19object)

for page in PDFPage.get_pages(e):
	oct19subject.process_page(page)
	etext = printer.getvalue()

f = file('minutes/cm15_nov2.pdf', 'rb')
fdate = 'CCC Meeting Nov. 2:\n\n'
nov2 = PDFParser(f)
nov2doc = PDFDocument(nov2)
nov2object = TextConverter(manager, printer, laparams=laparams)
nov2subject = PDFPageInterpreter(manager, nov2object)

for page in PDFPage.get_pages(f):
	nov2subject.process_page(page)
	ftext = printer.getvalue()

minutes = open('minutes.txt', 'w')
# minutes.writelines('{0},{1},{2},{3},{4},{5}'.format(atext, btext, ctext, dtext, etext, ftext))
minutes.writelines('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}'.format(adate,atext,bdate,btext,cdate,ctext,ddate,dtext,edate,etext,fdate,ftext))
minutes.close

minutes = open('minutes.txt', 'r')
hits = open('hits.txt', 'w')
mentions = []
counter = 0
for x in minutes:
	if re.search('CCC Meeting \w+\D \d+', x):
		print x + '\n'
		hits.write(x + '\n')
	if re.search('Rac\w+', x):
		print x
		hits.write(x + '\n')
		counter += 1
	if re.search('campus', x):
		print x
		hits.write(x + '\n')
		counter += 1
	if re.search('discriminat\w+', x):
		print x
		hits.write(x + '\n')
		counter += 1
	mentions.append(counter)

print "Total hits: " + str(mentions[-1])
print "About " + str((mentions[-1]/6)) + " hits per meeting"

minutes.close
hits.close

# P.S. — This spits back a bunch of text, and it can be adapted to 
# search for whatever keywords you're seeking. mentions is defined
# as a list and not as an integer because I originally  wanted to 
# create a six-item list (one item for each meeting), but I 
# couldn't figure out how to properly iterate through the minutes
# and create a running total of regex hits. 
# I was hoping to output something  like this after the text:
#
# Mentions in meeting 1
# Mentions in meeting 2
# Mentions in meeting 3
# 
# ...but I couldn't work it out. Any help would be cool...figuring
# this out is frustrating me, and I'm too stubborn to drop it.