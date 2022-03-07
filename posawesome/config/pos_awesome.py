from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("POS Vapes Direct"),
			"items": [
				 {
				   "description": "POS Vapes Direct", 
				   "name": "posapp", 
				   "label": "POSAPP", 					
				   "type": "page"
				  }, 

				{
				   "type": "doctype", 
				   "description": "POS Profile", 
				   "name": "POS Profile", 
				  },

				{
				   "type": "doctype", 
				   "description": "POS Opening Shift", 
				   "name": "POS Opening Shift", 
				  },
				{
				   "type": "doctype", 
				   "description": "POS Closing Shift", 
				   "name": "POS Closing Shift", 
				  },
				{
				   "type": "doctype", 
				   "description": "POS Offers", 
				   "name": "POS Offer", 
				  },
            ]

        }
	]
