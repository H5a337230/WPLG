import sys
import requests
import os
import optparse
import re
import codecs


Tversion = 'VERSION 1.0.1'
pglist = []
thlist = []
uniquepg = []
uniqueth = []
def checkwp(addr):
	global webversion
	global wp
	rwp = None
	haddr = '%s/readme.html' %addr
	wp = requests.get(addr , timeout = 5 , stream = True)
	hwp = requests.get(haddr , timeout = 5 , stream = True)   # /readme.html request
	############################
	rwp = re.search('''([Cc][Oo][Nn][Tt][Ee][Nn][Tt])\s*=("[Ww][Oo][Rr][Dd][Pp][Rr][Ee][Ss][Ss].*")\s*''' , wp.text)  # check source-code to findout is it wordpress or not
	if ( rwp != None ):
		arwp = rwp.group(2).split('''"''')
		print 'Worpress Version:\n%s\n' %arwp[1]
		webversion = 1

	elif ( rwp == None and hwp.status_code == 200 ):
		rhwp = re.search( '''([Vv][Ee][Rr][Ss][Ii][Oo][Nn].*)''' , hwp.text)   # check for wordpress version
		if ( rhwp ):
			print 'Wordpress %s\n' %rhwp.group(0)
			webversion = 1
		else:
			print 'Unable To Get Versoin!\nYou Can Also Check Your Target Here : http://www.wpthemedetector.com\n'
			print 'ThankYou For Choosing This Tool To Test Your Website'
			print 'Share Your Feedback Throught Mail With Me\n0x5a337230@protonmail.com\n'
			exit()

	else:
		print 'It Seems That Its Not Wordpress!\nYou Can Also Check Your Target Here : http://www.wpthemedetector.com\n '
		webversion = 0



################################


def checkplg(addr):
	linecount = 0
	tmpF = codecs.open('tmp.txt' , 'w+' , 'utf-8')
	tmpF.write(wp.text)
	tmpF.close()
	if ( webversion == 1 ):
		tmpF = open('tmp.txt' , 'r')
		linZ = tmpF.readlines()
		for line in linZ[0:]:
			plgloc = re.search( '''([Ww][Pp]-[Cc][Oo][Nn][Tt][Ee][Nn][Tt]/[Pp][Ll][Uu][Gg][Ii][Nn][Ss].*)''' , line)     # serach for "wp-content/plugins"
			if ( plgloc != None ):
				pgs = plgloc.group(0).split('/')
				pglist.append(pgs[2])
				linecount = linecount + 1
		uniquepg = list(set(pglist))
		print 'PLUGINS LIST: '
		for num in range(len(uniquepg)):
			print '%s' %uniquepg[num]
	else:
		pass


################################


def checkthm(addr):
	linecount = 0
	if ( webversion == 1 ):
		tmpF = open('tmp.txt' , 'r')
		linZ = tmpF.readlines()
		for line in linZ[0:]:
			thmloc = re.search( '''([Ww][Pp]-[Cc][Oo][Nn][Tt][Ee][Nn][Tt]/[Tt][Hh][Ee][Mm][Ee][Ss].*)''' , line)     # serach for "wp-content/themes"
			if ( thmloc != None ):
				ths = thmloc.group(0).split('/')
				thlist.append(ths[2])
				linecount = linecount + 1
		uniqueth = list(set(thlist))
		print '\nTHEMES LIST: '
		for num in range(len(uniqueth)):
			print '%s' %uniqueth[num]
	else:
		pass


################################


if __name__ == '__main__':
	print '\nSimple Wordpress Plugin & Theme Checker \nCoded By :\n '
	print '''
    		__////////////////_00000000_____///////////__00000000_______________00000000_____////////____00000000
		0_////////////////__00000000___//////////////_00000000_______________00000000___////////////__0000000
		00___________/////___00000000__////______////__00000000_______________00000000__////____//////_000000
		000_________/////_____00000000_________//////___00000000__///////////__00000000_/////_____/////_00000
		0000_______/////_______00000000________////////__00000000_/////////////_00000000_/////_____/////_0000
		00000_____/////_________00000000___________//////_00000000_/////___////__00000000_/////_____/////_000
		000000___/////___________00000000__////______////__00000000_/////_________00000000_//////____////__00
		0000000__////////////////_00000000_//////////////___00000000_/////_________00000000__////////////___0
		00000000_////////////////__00000000___//////////_____00000000_////__________00000000____////////_____\n\n'''
	parser = optparse.OptionParser( version = Tversion )
	parser.add_option("-u" , dest = "addr" , help = "Target URL/IP ( Use With http/https )")
	options,_ = parser.parse_args()
	if ( options.addr ):
		checkwp(options.addr)
		checkplg(options.addr)
		checkthm(options.addr)
		os.remove('tmp.txt')
		print '\nThankYou For Choosing This Tool To Test Your Website'
		print 'Share Your Feedback Throught Mail With Me\n0x5a337230@protonmail.com\n'
	else:
		parser.print_help()