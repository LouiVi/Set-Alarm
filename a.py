from native import app
import json

tabs = None

def OnStart():
	global tabs

	lay = app.CreateLayout( "linear", "VCenter, FillXY" )
	lay.SetChildMargins( 0, 0, 0, 8, "px" )

	btn4 = app.AddButton( lay, "Open Alarm Setup", 0.6 )
	btn4.SetOnTouch( btn4_OnTouch )

	app.AddLayout( lay )

	tabs = app.CreateCustomTabs()


def btn4_OnTouch():
	hour = 11
	minutes = 49
	message = "ToDo"

	action = "android.intent.action.SET_ALARM"
	extras = json.dumps([
		{ "name": "android.intent.extra.alarm.HOUR", "type": "int", "value": hour },
		{ "name": "android.intent.extra.alarm.MINUTES", "type": "int", "value": minutes },
		{ "name": "android.intent.extra.alarm.MESSAGE", "type": "string", "value": message }
	])

	app.SendIntent( None, None, action, None, None, None, extras)
