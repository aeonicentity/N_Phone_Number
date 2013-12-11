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
	#pooler = self.pool.get('res.partner')
	_inherit = 'res.partner'
	
	#_columns = {
    #    'Telephone': fields.char('Telephone', size=17, help="Phone Numbers auto formatted in this field.")
	#	}
		
	def onchange_phone(self,cr,uid,ids,currentNumber,context=None):
		#currentNumber = str( self.pool.get('res.partner').read(cr,uid,ids,['phone'],context=None)[0]['phone'] )
		curretNumber = str(currentNumber)
		if currentNumber == '223':
			currentNumber = '111'
		self.pool.get('res.partner').write(cr,uid,ids,{'phone' : currentNumber},context=None)
		
		return {'phone':currentNumber}