##############################################################################
#
#    Novak Conversions custom module:
#	 Extends Account_Invoice and Account_Voucher to integrate MeS PayEverywhere
#	 gateway, and our internet database.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import osv,fields

class res_partner(osv.osv):
	_inherit = 'res.partner'
		
	def onchange_phone(self,cr,uid,ids,phone,context=None):
		n = u''+str(phone)
		formatN = ""
		for c in n: #strip number of existing non-numeric characters, including .'s spaces -'s ()'s.
				if c.isdigit():
					formatN += c
		n = formatN
			# if number is less than 7 digits, or more than 11, or create an alert telling the user to stop entering bad phone numbers.
		if len(n) >= 7 and len(n) <= 11:
			
			#if number is 7 digits or more, add a - between the 5th and 4th from last digit.
			if len(n) >= 7:
				finalFour = n[-4:]
				prefix = n[-7:-4]
				formatN = prefix + "-" +finalFour
			#if number is 10 digits or more, add a ( )
			if len(n) >=10:
				areaCode = n[-10:-7]
				formatN = n[:-10]+" ("+areaCode+") "+formatN
			print formatN
		
		return {'value':{'phone':formatN}}